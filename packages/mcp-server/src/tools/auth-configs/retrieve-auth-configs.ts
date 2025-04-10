// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'auth_configs',
  operation: 'read',
  tags: [],
};

export const tool: Tool = {
  name: 'retrieve_auth_configs',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      nanoid: {
        type: 'string',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { nanoid } = args;
  return client.authConfigs.retrieve(nanoid);
};

export default { metadata, tool, handler };
