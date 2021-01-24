import {AfterViewInit, Component} from '@angular/core';
import {AuthService} from './auth/auth.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements AfterViewInit {
  title = 'mipt-portal';
  userId: string;

  constructor(private router: Router, private auth: AuthService) {
  }

  ngAfterViewInit(): void {
    this.auth.userInfo$.subscribe(userInfo => {
      console.log(userInfo);

      this.userId = userInfo?.userId;
    });

  }


}
