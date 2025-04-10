// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'connected_accounts',
  operation: 'read',
  tags: [],
};

export const tool: Tool = {
  name: 'list_connected_accounts',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      auth_config_id: {
        type: 'string',
        description: 'The auth config id of the connected account',
      },
      cursor: {
        type: 'number',
        description: 'The cursor to paginate through the connected accounts',
      },
      limit: {
        type: 'number',
        description: 'The limit of the connected accounts to return',
      },
      order_by: {
        type: 'string',
        description: 'The order by of the connected accounts',
        enum: ['created_at', 'updated_at'],
      },
      status: {
        type: 'string',
        description: 'The status of the connected account',
        enum: ['ACTIVE', 'INACTIVE', 'DELETED', 'INITIATED', 'EXPIRED', 'FAILED'],
      },
      toolkit_slug: {
        type: 'string',
        description: 'The toolkit slug of the connected account',
      },
      user_id: {
        type: 'string',
        description: 'The user id of the connected account',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.connectedAccounts.list(body);
};

export default { metadata, tool, handler };
