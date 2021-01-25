export * from './airport.service';
import { AirportService } from './airport.service';
export * from './global.service';
import { GlobalService } from './global.service';
export * from './health.service';
import { HealthService } from './health.service';
export const APIS = [AirportService, GlobalService, HealthService];
