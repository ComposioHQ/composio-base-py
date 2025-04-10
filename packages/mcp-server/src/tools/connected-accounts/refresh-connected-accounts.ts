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
  name: 'refresh_connected_accounts',
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
  return client.connectedAccounts.refresh(nanoid);
};

export default { metadata, tool, handler };
