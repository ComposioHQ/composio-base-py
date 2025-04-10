// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'payments',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'create_session_payments',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      applyDiscount: {
        type: 'boolean',
        description: 'Whether to apply discount coupon',
      },
      plan: {
        type: 'string',
        description: 'Subscription plan to purchase',
        enum: ['HOBBY', 'STARTER', 'GROWTH'],
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.payments.createSession(body);
};

export default { metadata, tool, handler };
