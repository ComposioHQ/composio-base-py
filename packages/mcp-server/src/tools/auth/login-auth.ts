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
  name: 'login_auth',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      provider_name: {
        type: 'string',
      },
      redirectUri: {
        type: 'string',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { provider_name, ...body } = args;
  return client.auth.login(provider_name, body);
};

export default { metadata, tool, handler };
