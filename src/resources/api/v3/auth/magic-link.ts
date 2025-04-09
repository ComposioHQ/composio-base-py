// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../../core/resource';
import { APIPromise } from '../../../../core/api-promise';
import { RequestOptions } from '../../../../internal/request-options';

export class MagicLink extends APIResource {
  send(body: MagicLinkSendParams, options?: RequestOptions): APIPromise<MagicLinkSendResponse> {
    return this._client.post('/api/v3/auth/magic_link/send', { body, ...options });
  }

  verify(body: MagicLinkVerifyParams, options?: RequestOptions): APIPromise<MagicLinkVerifyResponse> {
    return this._client.post('/api/v3/auth/magic_link/verify', { body, ...options });
  }
}

export interface MagicLinkSendResponse {
  status: string;
}

export interface MagicLinkVerifyResponse {
  data: MagicLinkVerifyResponse.Data;

  message: string;
}

export namespace MagicLinkVerifyResponse {
  export interface Data {
    email: string;

    jwtToken: string;

    memberId: string;

    orgId: string;
  }
}

export interface MagicLinkSendParams {
  email: string;

  verifyHost?: string;
}

export interface MagicLinkVerifyParams {
  token: string;
}

export declare namespace MagicLink {
  export {
    type MagicLinkSendResponse as MagicLinkSendResponse,
    type MagicLinkVerifyResponse as MagicLinkVerifyResponse,
    type MagicLinkSendParams as MagicLinkSendParams,
    type MagicLinkVerifyParams as MagicLinkVerifyParams,
  };
}
