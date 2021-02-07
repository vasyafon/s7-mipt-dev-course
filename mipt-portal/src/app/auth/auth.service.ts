import {Injectable, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {environment} from '../../environments/environment';
import {BehaviorSubject, Observable, Subject, Subscription, throwError} from 'rxjs';
import {HttpClient, HttpErrorResponse, HttpHeaders} from '@angular/common/http';
import {AuthService as AuthServiceAPI, Configuration, TokenResponse, UserInfo} from '../../clients/auth';
import {finalize, switchMap} from 'rxjs/operators';
import {NotificationsService} from 'angular2-notifications';

export interface SSOResponse {
  code: string;
  state: string;
  sessionState: string;
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private authServiceAPI: AuthServiceAPI;
  private refresherAPI: AuthServiceAPI;

  private refreshTokenExpirationDate: Date;
  private accessTokenExpirationDate: Date;

  private userInfoP: UserInfo;
  public userInfo$ = new BehaviorSubject<UserInfo>(undefined);
  private accessToken: string;
  private refreshSubject: Subject<string>;
  private isRefreshing = false;
  private refreshToken: string;
  private loginAttempt = false;

  constructor(private route: ActivatedRoute,
              private router: Router,
              private httpClient: HttpClient,
              private notificationsService: NotificationsService) {

    this.authServiceAPI = new AuthServiceAPI(httpClient, environment.authApiBasePath, new Configuration());
    this.authServiceAPI.configuration.credentials = {};
    this.authServiceAPI.defaultHeaders = new HttpHeaders();
    this.authServiceAPI.defaultHeaders = this.authServiceAPI.defaultHeaders.append('handleError', 'onService');

    this.refresherAPI = new AuthServiceAPI(httpClient, environment.authApiBasePath, new Configuration());
    this.refresherAPI.configuration.credentials = {};
    this.refresherAPI.defaultHeaders = new HttpHeaders();
    this.refresherAPI.defaultHeaders = this.authServiceAPI.defaultHeaders.append('handleError', 'onService');

    this.refreshSubject = new Subject<string>();
    this.refreshToken = 'None';
    this.refresherAPI.configuration.credentials.RefreshAuth = this.refreshToken;
  }

  public get userInfo() {
    if (this.checkUserInfo()) {
      return this.userInfoP;
    } else {
      this.userInfoP = undefined;
      this.userInfo$.next(undefined);
      sessionStorage.setItem('userInfo', undefined);
      this.login(this.route.snapshot.toString());
    }
  }

  public resetAuthentication() {
    this.userInfoP = undefined;
    this.accessToken = undefined;
    this.accessTokenExpirationDate = undefined;

  }

  public get isAdmin(): boolean {
    return this.userInfoP.globalRole === 'ADMIN';
  }

  public isAuthenticated(): boolean {
    return this.accessToken && new Date(this.accessTokenExpirationDate).getTime() > new Date().getTime() + 60000;
  }

  login(targetUrl: string) {
    return new Observable<string>(ob => {
      if (this.isAuthenticated()) {
        ob.next(this.accessToken);
        ob.complete();
      } else {
        this.refresh().subscribe(accessToken => {
          if (accessToken) {
            this.authServiceAPI.getUserInfo().subscribe(userInfo => {
              this.userInfoP = userInfo;
              this.userInfo$.next(userInfo);
              sessionStorage.setItem('userInfo', JSON.stringify(userInfo));
              ob.next(this.accessToken);
              ob.complete();
            });
          } else {
            if (!this.loginAttempt) {
              this.oauthLogin(targetUrl);
            }

            ob.next(undefined);
            ob.complete();
          }
        });
      }
    });
  }

  oauthLogin(targetUrl: string): void {
    console.log('Logging into OAuth');
    this.authServiceAPI.login(targetUrl).subscribe(loginUrl => {
      window.location.href = loginUrl.url;
    });
  }

  public refresh(): Observable<string> {
    return new Observable<string>(ob => {
      this.refreshP();
      this.refreshSubject.subscribe((accessToken) => {
        ob.next(accessToken);
        ob.complete();
      });
    });
  }

  public refreshP() {
    if (!this.isRefreshing) {
      this.isRefreshing = true;
      this.refresherAPI.refresh().subscribe(tokenResponse => {
        const accessToken = tokenResponse.token;
        this.accessToken = accessToken;
        this.accessTokenExpirationDate = new Date(tokenResponse.expiresAt);
        this.authServiceAPI.configuration.credentials.BearerAuth = accessToken;
        this.refreshSubject.next(accessToken);
        this.isRefreshing = false;
      }, (error) => {
        this.refreshSubject.next(undefined);
        this.isRefreshing = false;
      });
    }
  }

  public getAccessToken(): string {
    if (this.isAuthenticated()) {
      return this.accessToken;
    }
    return undefined;
  }


  checkUserInfo(): boolean {
    return this.isAuthenticated();
  }

  authenticate() {
    this.refresh().subscribe(() => {
      this.authServiceAPI.getUserInfo().subscribe(userInfo => {
        this.userInfoP = userInfo;
        this.userInfo$.next(this.userInfoP);
        const redirectUrl = '/';
        this.router.navigateByUrl(redirectUrl);
      });
    });


  }

}
