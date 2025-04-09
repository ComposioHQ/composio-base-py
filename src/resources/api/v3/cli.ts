// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../core/resource';
import { APIPromise } from '../../../core/api-promise';
import { RequestOptions } from '../../../internal/request-options';

export class Cli extends APIResource {
  createSession(options?: RequestOptions): APIPromise<CliCreateSessionResponse> {
    return this._client.post('/api/v3/cli/create-session', options);
  }

  linkSession(body: CliLinkSessionParams, options?: RequestOptions): APIPromise<CliLinkSessionResponse> {
    return this._client.put('/api/v3/cli/link-session', { body, ...options });
  }

  retrieveSession(
    query: CliRetrieveSessionParams,
    options?: RequestOptions,
  ): APIPromise<CliRetrieveSessionResponse> {
    return this._client.get('/api/v3/cli/get-session', { query, ...options });
  }
}

export interface CliCreateSessionResponse {
  /**
   * Unique identifier for the CLI session
   */
  id: string;

  /**
   * Temporary code to use for CLI login
   */
  code: string;

  /**
   * Expiration time of the session
   */
  expiresAt: string;

  /**
   * Current status of the session
   */
  status: 'pending' | 'linked';
}

export interface CliLinkSessionResponse {
  /**
   * Unique identifier for the CLI session
   */
  id: string;

  /**
   * Information about the linked account
   */
  account: CliLinkSessionResponse.Account;

  /**
   * Temporary code used for CLI login
   */
  code: string;

  /**
   * Expiration time of the session
   */
  expiresAt: string;

  /**
   * Current status of the session
   */
  status: 'pending' | 'linked';
}

export namespace CliLinkSessionResponse {
  /**
   * Information about the linked account
   */
  export interface Account {
    /**
     * ID of the linked account
     */
    id: string;

    /**
     * Email of the linked account
     */
    email: string;

    /**
     * Name of the linked account
     */
    name: string;
  }
}

export interface CliRetrieveSessionResponse {
  /**
   * Unique identifier for the CLI session
   */
  id: string;

  /**
   * Information about the linked account, if any
   */
  account: CliRetrieveSessionResponse.Account | null;

  /**
   * Temporary code used for CLI login
   */
  code: string;

  /**
   * Expiration time of the session
   */
  expiresAt: string;

  /**
   * Current status of the session
   */
  status: 'pending' | 'linked';
}

export namespace CliRetrieveSessionResponse {
  /**
   * Information about the linked account, if any
   */
  export interface Account {
    /**
     * ID of the linked account
     */
    id: string;

    /**
     * Email of the linked account
     */
    email: string;

    /**
     * Name of the linked account
     */
    name: string;
  }
}

export interface CliLinkSessionParams {
  /**
   * CLI session ID or code to link
   */
  id: string;
}

export interface CliRetrieveSessionParams {
  /**
   * CLI session ID or code to check
   */
  id: string;
}

export declare namespace Cli {
  export {
    type CliCreateSessionResponse as CliCreateSessionResponse,
    type CliLinkSessionResponse as CliLinkSessionResponse,
    type CliRetrieveSessionResponse as CliRetrieveSessionResponse,
    type CliLinkSessionParams as CliLinkSessionParams,
    type CliRetrieveSessionParams as CliRetrieveSessionParams,
  };
}
