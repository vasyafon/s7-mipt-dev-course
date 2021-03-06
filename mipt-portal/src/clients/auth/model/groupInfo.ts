/**
 * Auth server
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export interface GroupInfo { 
    groupId?: string;
    description?: string;
    mode?: GroupInfo.ModeEnum;
}
export namespace GroupInfo {
    export type ModeEnum = 'READ' | 'WRITE' | 'ADMIN';
    export const ModeEnum = {
        Read: 'READ' as ModeEnum,
        Write: 'WRITE' as ModeEnum,
        Admin: 'ADMIN' as ModeEnum
    };
}


