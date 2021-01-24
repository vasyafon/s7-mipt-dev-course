import {Injectable, OnInit} from '@angular/core';
import {OAuthService} from 'angular-oauth2-oidc';
import {ActivatedRoute, Router} from '@angular/router';
import {authConfig} from './auth.config';
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
              private oauthService: OAuthService,
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

    // this.accessToken = sessionStorage.getItem('accessToken');
    // this.accessTokenExpirationDate = new Date(sessionStorage.getItem('accessTokenExpirationDate'));
    // if (!this.isAuthenticated()) {
    //   this.accessToken = undefined;
    //   this.accessTokenExpirationDate = undefined;
    // } else {
    //   this.authServiceAPI.configuration.credentials.BearerAuth = this.accessToken;
    // }
    this.refreshSubject = new Subject<string>();
    this.refreshToken = sessionStorage.getItem('refreshToken');
    this.refreshTokenExpirationDate = new Date(sessionStorage.getItem('refreshTokenExpirationDate'));
    if (this.refreshToken) {
      this.refresherAPI.configuration.credentials.RefreshAuth = this.refreshToken;
      // this.refresh().subscribe;
    }

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


  // private refreshToken: string;
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
    this.route.url.subscribe(url => {
      console.log('url', url);
      this.oauthService.configure(authConfig);
      this.oauthService.initCodeFlow(targetUrl);
    });
  }

  // public authenticate(): Observable<string> {
  //   return new Observable<string>((ob) => {
  //     if (this.isAuthenticated()) {
  //       ob.next(this.accessToken);
  //       ob.complete();
  //       return;
  //     }
  //     console.log('trying to refresh');
  //     this.refresh().subscribe(accessToken => {
  //       if (accessToken) {
  //         ob.next(accessToken);
  //         ob.complete();
  //       } else {
  //         console.log('trying to oauth login');
  //         this.oauthLogin(undefined);
  //         ob.complete();
  //       }
  //     });
  //
  //
  //     ob.next('foo');
  //     ob.complete();
  //   });
  // }


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
      // console.log(this.refresherAPI.configuration);
      this.refresherAPI.refresh().subscribe(tokenResponse => {
        const accessToken = tokenResponse.token;
        this.accessToken = accessToken;
        this.accessTokenExpirationDate = new Date(tokenResponse.expiresAt);
        // sessionStorage.setItem('accessToken', accessToken);
        // sessionStorage.setItem('accessTokenExpirationDate', tokenResponse.expiresAt);
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

  backendLogin(params: SSOResponse, redirectUrl?: string): void {
    this.loginAttempt = true;
    const codeVerifier = sessionStorage.getItem('PKCE_verifier');
    const nonce = sessionStorage.getItem('nonce');
    if (!codeVerifier || !nonce) {
      console.log('Login error PKCI_verifier / nonce');
      this.router.navigateByUrl('/');
    } else {
      sessionStorage.removeItem('PKCE_verifier');
      sessionStorage.removeItem('nonce');
      // console.log('LOGIN', {
      //   code: params.code,
      //   codeVerifier,
      //   redirectUri: environment.applicationBaseUrl,
      //   nonce
      // });
      console.log('login');
      this.authServiceAPI.login({
        code: params.code,
        codeVerifier,
        redirectUri: environment.applicationBaseUrl,
        nonce
      }).subscribe(tokens => {
        console.log(tokens);
        const accessToken = tokens.accessToken.token;
        this.accessToken = accessToken;
        this.refreshToken = tokens.refreshToken.token;
        this.refreshTokenExpirationDate = new Date(tokens.refreshToken.expiresAt);
        // sessionStorage.setItem('accessToken', accessToken);
        // sessionStorage.setItem('accessTokenExpirationDate', tokens.accessToken.expiresAt);
        sessionStorage.setItem('refreshToken', this.refreshToken);
        sessionStorage.setItem('refreshTokenExpirationDate', tokens.refreshToken.expiresAt);
        this.refresherAPI.configuration.credentials.RefreshAuth = this.refreshToken;
        this.authServiceAPI.configuration.credentials.BearerAuth = accessToken;
        console.log(this.refresherAPI.configuration.credentials);
        this.authServiceAPI.getUserInfo().subscribe(userInfo => {
          // sessionStorage.setItem('userInfo', JSON.stringify(userInfo));
          this.userInfoP = userInfo;
          this.userInfo$.next(this.userInfoP);
          this.router.navigateByUrl(redirectUrl);
        });
      }, (error: HttpErrorResponse) => {
        console.log(error);
        if (error.status === 403 || error.status === 401) {
          const errorMsg = 'Your username is not allowed to login. Please ask admins to add you.';
          this.notificationsService.error('Unauthorized', errorMsg);
        } else {
          console.log('ERROR');
        }
      });
    }
  }
}
