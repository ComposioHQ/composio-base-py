// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'connected_accounts',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'update_status_connected_accounts',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      nanoId: {
        type: 'string',
      },
      enabled: {
        type: 'boolean',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { nanoId, ...body } = args;
  return client.connectedAccounts.updateStatus(nanoId, body);
};

export default { metadata, tool, handler };
