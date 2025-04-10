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
  name: 'update_status_auth_configs',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      nanoid: {
        type: 'string',
      },
      status: {
        type: 'string',
        enum: ['ENABLED', 'DISABLED'],
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { status, ...body } = args;
  return client.authConfigs.updateStatus(status, body);
};

export default { metadata, tool, handler };
