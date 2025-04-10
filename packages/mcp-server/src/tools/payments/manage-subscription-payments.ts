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
  name: 'manage_subscription_payments',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {},
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.payments.manageSubscription(body);
};

export default { metadata, tool, handler };
