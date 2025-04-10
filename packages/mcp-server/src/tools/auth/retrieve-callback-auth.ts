// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'auth',
  operation: 'read',
  tags: [],
};

export const tool: Tool = {
  name: 'retrieve_callback_auth',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      provider_name: {
        type: 'string',
        enum: ['github', 'google'],
      },
      authCode: {
        type: 'string',
      },
      code: {
        type: 'string',
      },
      error: {
        type: 'string',
      },
      error_description: {
        type: 'string',
      },
      state: {
        type: 'string',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { provider_name, ...body } = args;
  return client.auth.retrieveCallback(provider_name, body);
};

export default { metadata, tool, handler };
