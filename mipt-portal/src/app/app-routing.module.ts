import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {IndexComponent} from "./index/index.component";
import {ErrorPageComponent} from "./error-page/error-page.component";
import {CatalogComponent} from "./catalog/catalog.component";
import {AuthGuardService} from "./auth-guard.service";

const routes: Routes = [
  {
    path: 'catalog',
    component: CatalogComponent,
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
