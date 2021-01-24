import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {OAuthModule, OAuthStorage} from 'angular-oauth2-oidc';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {Options, SimpleNotificationsModule} from "angular2-notifications";
import {IndexComponent} from "./index/index.component";
import {HttpErrorInterceptorService} from "./lib/http-error-interceptor.service";
import { ErrorPageComponent } from './error-page/error-page.component';
import { CatalogComponent } from './catalog/catalog.component';
import {MatCardModule} from "@angular/material/card";

const simpleNotificationOptions: Options = {
  theClass: 'app-simple-notification',
  timeOut: 0
};

@NgModule({
  declarations: [
    AppComponent,
    IndexComponent,
    ErrorPageComponent,
    CatalogComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    OAuthModule.forRoot(),
    SimpleNotificationsModule.forRoot(simpleNotificationOptions),
    MatCardModule,
  ],
  providers: [
    {provide: OAuthStorage, useValue: sessionStorage},
    {provide: HTTP_INTERCEPTORS, useClass: HttpErrorInterceptorService, multi: true},
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
