import {Injectable} from '@angular/core';
import {HttpErrorResponse, HttpEvent, HttpHandler, HttpInterceptor, HttpRequest} from '@angular/common/http';
import {BehaviorSubject, Observable, throwError} from 'rxjs';
import {NotificationsService} from 'angular2-notifications';
import {catchError, filter, finalize, switchMap, take, tap} from 'rxjs/operators';
import {AuthService} from '../auth/auth.service';

@Injectable()
export class HttpErrorInterceptorService implements HttpInterceptor {
  isRefreshingToken = false;
  tokenSubject: BehaviorSubject<string> = new BehaviorSubject<string>(null);

  constructor(private notificationsService: NotificationsService,
              private auth: AuthService) {
  }

  addToken(req: HttpRequest<any>): HttpRequest<any> {
    if (req.headers.get('handleError') === 'onService') {
      return req;
    }
    const token = this.auth.getAccessToken();
    console.log(token);
    if (token) {
      return req.clone({setHeaders: {Authorization: 'Bearer ' + token}});
    } else {
      return req;
    }
  }

  handleAddingToken(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    if (req.headers.get('handleError') === 'onService') {
      return next.handle(req);
    }
    if (this.auth.isAuthenticated()) {
      const newReq = req.clone({setHeaders: {Authorization: 'Bearer ' + this.auth.getAccessToken()}});
      return next.handle(newReq);
    } else {
      return this.auth.refresh().pipe(switchMap(accessToken => {
        const newReq = req.clone({setHeaders: {Authorization: 'Bearer ' + accessToken}});
        return next.handle(newReq);
      }));

    }
  }


  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    return this.handleAddingToken(req, next).pipe(tap((event: HttpEvent<any>) => {
    }, (err: HttpErrorResponse) => {
      let errorMsg = '';
      if (err.error instanceof ErrorEvent) {
        console.log('this is client side error');
        errorMsg = `Error: ${err.error.message}`;
      } else {
        if (req.headers.get('handleError') === 'onService') {
          return;
        } else {
          console.log('this is server side error');
          errorMsg = `Error Code: ${err.status},  Message: ${err.message}`;
        }
      }
      console.log(errorMsg);
      this.notificationsService.error('Something wrong', errorMsg);
      return throwError(errorMsg);
    }));

    // return this.handleAddingToken(req, next).pipe(catchError((err: HttpErrorResponse) => {
    //     let errorMsg = '';
    //     if (err.error instanceof ErrorEvent) {
    //       console.log('this is client side error');
    //       errorMsg = `Error: ${err.error.message}`;
    //     } else {
    //       if (req.headers.get('handleError') === 'onService') {
    //         console.log('Interceptor does nothing...');
    //         return next.handle(req);
    //       } else {
    //         console.log('this is server side error');
    //         errorMsg = `Error Code: ${err.status},  Message: ${err.message}`;
    //       }
    //     }
    //     console.log(errorMsg);
    //     this.notificationsService.error('Something wrong', errorMsg);
    //     return throwError(errorMsg);
    //   })
    // );
  }

  // handle401Error(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
  //   console.log('401 processing');
  //   if (!this.isRefreshingToken) {
  //     this.isRefreshingToken = true;
  //
  //     // Reset here so that the following requests wait until the token
  //     // comes back from the refreshToken call.
  //     // this.tokenSubject.next(null);
  //
  //     return this.auth.refresh().pipe(switchMap((newToken: string) => {
  //       if (newToken) {
  //         return next.handle(this.addToken(req));
  //       }
  //       // return this.logoutUser();
  //     })).pipe(catchError(error => {
  //         // If there is an exception calling 'refreshToken', bad news so logout.
  //         // this.cookieService.delete('auth_session');
  //         // this.auth.resetAuthentication();
  //         // this.auth.login(undefined).subscribe();
  //         // console.log(error);
  //         return next.handle(req);
  //         // return this.logoutUser();
  //       }),
  //     )
  //       .pipe(finalize(() => {
  //           this.isRefreshingToken = false;
  //         })
  //       );
  //   } else {
  //     return this.tokenSubject.pipe(filter(token => token != null))
  //       .pipe(take(1))
  //       .pipe(switchMap(token => {
  //         return next.handle(this.addToken(req));
  //       }));
  //   }
  // }

}
