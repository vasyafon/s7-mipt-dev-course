import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {IndexComponent} from "./index/index.component";
import {ErrorPageComponent} from "./error-page/error-page.component";
import {AuthGuardService} from "./auth-guard.service";
import {AirportLoadComponent} from './airport-load/airport-load.component';

const routes: Routes = [
  {
    path: 'airportLoad',
    component: AirportLoadComponent,
    canActivate: [AuthGuardService]
  },
  {
    path: '',
    component: IndexComponent,
    pathMatch: 'full'
  },
  {
    path: 'error',
    component: ErrorPageComponent,
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
