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
    this.auth.login('/').subscribe(isLoggedIn => {
      if (isLoggedIn) {
        this.router.navigateByUrl('catalog');
      }
    });
  }
}
