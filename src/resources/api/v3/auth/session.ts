// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../../core/resource';
import { APIPromise } from '../../../../core/api-promise';
import { RequestOptions } from '../../../../internal/request-options';

export class Session extends APIResource {
  logout(options?: RequestOptions): APIPromise<SessionLogoutResponse> {
    return this._client.post('/api/v3/auth/session/logout', options);
  }

  retrieveInfo(options?: RequestOptions): APIPromise<SessionRetrieveInfoResponse> {
    return this._client.get('/api/v3/auth/session/info', options);
  }
}

export interface SessionLogoutResponse {
  /**
   * Status message
   */
  message: string;
}

export interface SessionRetrieveInfoResponse {
  apiKey: SessionRetrieveInfoResponse.APIKey | null;

  org_member: SessionRetrieveInfoResponse.OrgMember;

  project: SessionRetrieveInfoResponse.Project | null;
}

export namespace SessionRetrieveInfoResponse {
  export interface APIKey {
    id: string;

    autoId: number;

    createdAt: string;

    deleted: boolean;

    deletedAt: string | null;

    key: string;

    name: string;

    orgMemberId: string;

    projectId: string;

    updatedAt: string;
  }

  export interface OrgMember {
    id: string;

    email: string;

    name: string;

    role: string;
  }

  export interface Project {
    id: string;

    autoId: number;

    createdAt: string;

    deleted: boolean;

    email: string;

    eventWebhookURL: string | null;

    isNewWebhook: boolean;

    lastSubscribedAt: string | null;

    name: string;

    nanoId: string;

    org: Project.Org;

    orgId: string;

    triggersEnabled: boolean;

    updatedAt: string;

    webhookSecret: string | null;

    webhookURL: string | null;
  }

  export namespace Project {
    export interface Org {
      id: string;

      name: string;

      orgMembers: Array<Org.OrgMember>;

      plan: string;
    }

    export namespace Org {
      export interface OrgMember {
        id: string;

        autoId: number;

        createdAt: string;

        deletedAt: string | null;

        email: string;

        name: string;

        orgId: string;

        role: string;

        updatedAt: string;

        metadata?: unknown;
      }
    }
  }
}

export declare namespace Session {
  export {
    type SessionLogoutResponse as SessionLogoutResponse,
    type SessionRetrieveInfoResponse as SessionRetrieveInfoResponse,
  };
}
