// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'auth_configs',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'update_auth_configs',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      nanoid: {
        type: 'string',
      },
      auth_config: {
        type: 'object',
        properties: {
          credentials: {
            type: 'object',
            description: 'Authentication configuration',
          },
        },
        required: [],
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { nanoid, ...body } = args;
  return client.authConfigs.update(nanoid, body);
};

export default { metadata, tool, handler };
