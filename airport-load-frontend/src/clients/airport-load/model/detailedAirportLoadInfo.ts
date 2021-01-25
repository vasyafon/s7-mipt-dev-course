/**
 * API to show passenger load in airports
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { FlightAirportLoadInfo } from './flightAirportLoadInfo';


export interface DetailedAirportLoadInfo { 
    airportCode: string;
    paxYLoad?: number;
    paxCLoad?: number;
    childrenYLoad?: number;
    childrenCLoad?: number;
    infantsYLoad?: number;
    infantsCLoad?: number;
    latitude?: number;
    longititude?: number;
    flights?: Array<FlightAirportLoadInfo>;
}

