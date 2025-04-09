// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'admin',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'identify_admin',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      hash: {
        type: 'string',
      },
      adminToken: {
        type: 'string',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.admin.identify(body);
};

export default { metadata, tool, handler };
