export * from './admin.service';
import { AdminService } from './admin.service';
export * from './auth.service';
import { AuthService } from './auth.service';
export * from './health.service';
import { HealthService } from './health.service';
export const APIS = [AdminService, AuthService, HealthService];
