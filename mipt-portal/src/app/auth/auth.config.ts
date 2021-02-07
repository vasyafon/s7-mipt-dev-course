// This api will come in the next version

import {AuthConfig} from 'angular-oauth2-oidc';
import {environment} from '../../environments/environment';

// const wsoUrl = 'https://accounts.google.com';
// export const authConfig: AuthConfig = {
//   clientId: '196213007228-btl13tj6vteaahk0114ijr5de4ii6ab2.apps.googleusercontent.com',
//   redirectUri: environment.applicationBaseUrl,
//   postLogoutRedirectUri: '',
//   loginUrl: `${wsoUrl}/o/oauth2/v2/auth`,
//   scope: 'openid profile email',
//   resource: '',
//   rngUrl: '',
//   oidc: true,
//   requestAccessToken: true,
//   options: null,
//   issuer: wsoUrl,
//   clearHashAfterLogin: true,
//   tokenEndpoint: `https://oauth2.googleapis.com/token`,
//   userinfoEndpoint: `https://openidconnect.googleapis.com/v1/userinfo`,
//   silentRefreshRedirectUri: window.location.origin + '/silent-refresh.html',
//   showDebugInformation: true,
//   responseType: 'code',
//   dummyClientSecret: null,
//   requireHttps: 'remoteOnly',
//   strictDiscoveryDocumentValidation: false,
//   sessionChecksEnabled: true,
// };

export const wsoUrl = environment.ssoMainUrl;
export const authConfig: AuthConfig = {
  clientId: environment.ssoClientId,
  redirectUri: environment.applicationBaseUrl,
  postLogoutRedirectUri: '',
  loginUrl: `${wsoUrl}/oauth2/authorize`,
  scope: 'openid profile email offline_access api',
  resource: '',
  rngUrl: '',
  oidc: true,
  requestAccessToken: true,
  options: null,
  issuer: wsoUrl,
  clearHashAfterLogin: true,
  tokenEndpoint: `${wsoUrl}/oauth2/token`,
  userinfoEndpoint: `${wsoUrl}/oauth2/userInfo`,
  silentRefreshRedirectUri: window.location.origin + '/silent-refresh.html',
  showDebugInformation: true,
  responseType: 'code',
  dummyClientSecret: null,
  requireHttps: 'remoteOnly',
  strictDiscoveryDocumentValidation: false,
  sessionChecksEnabled: true,
};
