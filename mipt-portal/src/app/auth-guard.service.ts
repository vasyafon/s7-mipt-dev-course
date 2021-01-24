import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, Router, RouterStateSnapshot} from '@angular/router';
import {AuthService} from './auth/auth.service';
import {Observable, Subscription} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthGuardService {

  constructor(public auth: AuthService, public router: Router) {
  }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean> {
    return new Observable<boolean>(ob => {
      this.auth.login(state.url).subscribe(accessToken => {
        if (accessToken) {
          ob.next(true);
          ob.complete();
        } else {
          ob.next(false);
          ob.complete();
        }
      });
    });
  }
}

