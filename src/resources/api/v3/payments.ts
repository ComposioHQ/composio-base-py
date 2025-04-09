// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../core/resource';
import { APIPromise } from '../../../core/api-promise';
import { RequestOptions } from '../../../internal/request-options';

export class Payments extends APIResource {
  createSession(
    body: PaymentCreateSessionParams,
    options?: RequestOptions,
  ): APIPromise<PaymentCreateSessionResponse> {
    return this._client.post('/api/v3/payments/session', { body, ...options });
  }

  manageSubscription(
    body?: PaymentManageSubscriptionParams | null | undefined,
    options?: RequestOptions,
  ): APIPromise<PaymentManageSubscriptionResponse> {
    return this._client.post('/api/v3/payments/manage-subscription', { body, ...options });
  }
}

export interface PaymentCreateSessionResponse {
  /**
   * ID of the created payment session
   */
  sessionId: string;

  /**
   * URL to the payment page
   */
  url: string;
}

export interface PaymentManageSubscriptionResponse {
  /**
   * ID of the created billing portal session
   */
  sessionId: string;

  /**
   * URL to the Stripe billing portal
   */
  url: string;
}

export interface PaymentCreateSessionParams {
  /**
   * Whether to apply discount coupon
   */
  applyDiscount: boolean;

  /**
   * Subscription plan to purchase
   */
  plan: 'HOBBY' | 'STARTER' | 'GROWTH';
}

export interface PaymentManageSubscriptionParams {}

export declare namespace Payments {
  export {
    type PaymentCreateSessionResponse as PaymentCreateSessionResponse,
    type PaymentManageSubscriptionResponse as PaymentManageSubscriptionResponse,
    type PaymentCreateSessionParams as PaymentCreateSessionParams,
    type PaymentManageSubscriptionParams as PaymentManageSubscriptionParams,
  };
}
