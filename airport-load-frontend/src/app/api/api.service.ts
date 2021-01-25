import {Injectable} from '@angular/core';
import {AirportService, GlobalService, Configuration} from '../../clients/airport-load';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {AdminService} from '../../clients/auth';
import {environment} from '../../environments/environment';

export function generateConfiguration(): Configuration {
  const configuration = new Configuration();
  configuration.credentials = {};
  return configuration;
}


@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private globalServiceP: GlobalService;
  private airportServiceP: AirportService;
  private accessToken: string;

  public get airportService(): AirportService {
    return this.airportServiceP;
  }

  public get globalService(): GlobalService {
    return this.globalServiceP;
  }

  constructor(private httpClient: HttpClient) {

    const headers = {
      'Cache-Control': 'no-cache, no-store, must-revalidate, post-check = 0, pre-check = 0', Pragma: 'no-cache', Expires: '0'
    };


    this.airportServiceP = new AirportService(httpClient, environment.airportLoadApiBasePath, generateConfiguration());
    this.globalServiceP = new GlobalService(httpClient, environment.airportLoadApiBasePath, generateConfiguration());

    this.globalServiceP.defaultHeaders = new HttpHeaders(headers);
    this.airportServiceP.defaultHeaders = new HttpHeaders(headers);

  }
}
