// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import * as MagicLinkAPI from './magic-link';
import {
  MagicLink,
  MagicLinkSendParams,
  MagicLinkSendResponse,
  MagicLinkVerifyParams,
  MagicLinkVerifyResponse,
} from './magic-link';
import * as SessionAPI from './session';
import { Session, SessionLogoutResponse, SessionRetrieveInfoResponse } from './session';
import { APIPromise } from '../../core/api-promise';
import { buildHeaders } from '../../internal/headers';
import { RequestOptions } from '../../internal/request-options';
import { path } from '../../internal/utils/path';

export class Auth extends APIResource {
  magicLink: MagicLinkAPI.MagicLink = new MagicLinkAPI.MagicLink(this._client);
  session: SessionAPI.Session = new SessionAPI.Session(this._client);

  login(
    providerName: string,
    query: AuthLoginParams | null | undefined = {},
    options?: RequestOptions,
  ): APIPromise<void> {
    return this._client.get(path`/api/v3/auth/${providerName}/login`, {
      query,
      ...options,
      headers: buildHeaders([{ Accept: '*/*' }, options?.headers]),
    });
  }

  oneTap(
    providerName: 'github' | 'google',
    body: AuthOneTapParams,
    options?: RequestOptions,
  ): APIPromise<AuthOneTapResponse> {
    return this._client.post(path`/api/v3/auth/${providerName}/one-tap`, { body, ...options });
  }

  retrieveCallback(
    providerName: 'github' | 'google',
    query: AuthRetrieveCallbackParams | null | undefined = {},
    options?: RequestOptions,
  ): APIPromise<AuthRetrieveCallbackResponse> {
    return this._client.get(path`/api/v3/auth/${providerName}/callback`, { query, ...options });
  }
}

export interface AuthOneTapResponse {
  apiKey: string | null;

  clientId: string | null;

  email: string | null;

  orgId: string | null;
}

export interface AuthRetrieveCallbackResponse {
  data: AuthRetrieveCallbackResponse.Data;

  message: string;
}

export namespace AuthRetrieveCallbackResponse {
  export interface Data {
    jwtToken: string;

    userData: Data.UserData;
  }

  export namespace Data {
    export interface UserData {
      email: string;
    }
  }
}

export interface AuthLoginParams {
  redirectUri?: string;
}

export type AuthOneTapParams = AuthOneTapParams.Variant0 | AuthOneTapParams.Variant1;

export declare namespace AuthOneTapParams {
  export interface Variant0 {
    data: Variant0.Data;

    type: 'jwt';
  }

  export namespace Variant0 {
    export interface Data {
      jwt: string;
    }
  }

  export interface Variant1 {
    data: Variant1.Data;

    type: 'auth-code';
  }

  export namespace Variant1 {
    export interface Data {
      authCode: string;
    }
  }
}

export interface AuthRetrieveCallbackParams {
  authCode?: string;

  code?: string;

  error?: string;

  error_description?: string;

  state?: string;
}

Auth.MagicLink = MagicLink;
Auth.Session = Session;

export declare namespace Auth {
  export {
    type AuthOneTapResponse as AuthOneTapResponse,
    type AuthRetrieveCallbackResponse as AuthRetrieveCallbackResponse,
    type AuthLoginParams as AuthLoginParams,
    type AuthOneTapParams as AuthOneTapParams,
    type AuthRetrieveCallbackParams as AuthRetrieveCallbackParams,
  };

  export {
    MagicLink as MagicLink,
    type MagicLinkSendResponse as MagicLinkSendResponse,
    type MagicLinkVerifyResponse as MagicLinkVerifyResponse,
    type MagicLinkSendParams as MagicLinkSendParams,
    type MagicLinkVerifyParams as MagicLinkVerifyParams,
  };

  export {
    Session as Session,
    type SessionLogoutResponse as SessionLogoutResponse,
    type SessionRetrieveInfoResponse as SessionRetrieveInfoResponse,
  };
}
