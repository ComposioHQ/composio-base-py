// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import { APIPromise } from '../../core/api-promise';
import { RequestOptions } from '../../internal/request-options';
import { path } from '../../internal/utils/path';

export class TeamMembers extends APIResource {
  update(
    id: string,
    body: TeamMemberUpdateParams,
    options?: RequestOptions,
  ): APIPromise<TeamMemberUpdateResponse> {
    return this._client.put(path`/api/v3/team-members/update/${id}`, { body, ...options });
  }

  list(options?: RequestOptions): APIPromise<TeamMemberListResponse> {
    return this._client.get('/api/v3/team-members/list', options);
  }

  invite(body: TeamMemberInviteParams, options?: RequestOptions): APIPromise<TeamMemberInviteResponse> {
    return this._client.post('/api/v3/team-members/invite', { body, ...options });
  }

  remove(id: string, options?: RequestOptions): APIPromise<TeamMemberRemoveResponse> {
    return this._client.delete(path`/api/v3/team-members/remove/${id}`, options);
  }
}

export interface TeamMemberUpdateResponse {
  id: string;

  createdAt: string;

  email: string;

  name: string;

  role: string;

  updatedAt: string;
}

export interface TeamMemberListResponse {
  items: Array<TeamMemberListResponse.Item>;
}

export namespace TeamMemberListResponse {
  export interface Item {
    id: string;

    createdAt: string;

    email: string;

    name: string;

    role: string;

    updatedAt: string;
  }
}

export interface TeamMemberInviteResponse {
  id: string;

  createdAt: string;

  email: string;

  name: string;

  role: string;

  updatedAt: string;
}

export interface TeamMemberRemoveResponse {
  message: string;

  success: boolean;
}

export interface TeamMemberUpdateParams {
  email: string;

  name: string;

  role: string;
}

export interface TeamMemberInviteParams {
  email: string;

  name: string;

  role: string;

  verifyHost?: string;
}

export declare namespace TeamMembers {
  export {
    type TeamMemberUpdateResponse as TeamMemberUpdateResponse,
    type TeamMemberListResponse as TeamMemberListResponse,
    type TeamMemberInviteResponse as TeamMemberInviteResponse,
    type TeamMemberRemoveResponse as TeamMemberRemoveResponse,
    type TeamMemberUpdateParams as TeamMemberUpdateParams,
    type TeamMemberInviteParams as TeamMemberInviteParams,
  };
}
