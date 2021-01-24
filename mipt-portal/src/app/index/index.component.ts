import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {AuthService} from '../auth/auth.service';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: []
})
export class IndexComponent implements OnInit {
  constructor(private route: ActivatedRoute, private auth: AuthService, private router: Router) {
  }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      if (params.code && params.state) {
        const stateParams = params.state.split(';');
        let redirectUrl = '/';
        if (stateParams.length > 1) {
          redirectUrl = decodeURIComponent(stateParams[1]);
        }
        this.auth.backendLogin({
          code: params.code,
          sessionState: params.session_state,
          state: params.state,
        }, redirectUrl);
      } else {
        this.auth.login('/').subscribe(isLoggedIn => {
          if (!isLoggedIn) {
            console.error('error');
            this.router.navigateByUrl('/error');
          } else {
            this.router.navigateByUrl('catalog');
          }
        });
      }
    });
  }

}
