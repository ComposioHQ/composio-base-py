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
  name: 'create_connected_accounts',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      auth_config: {
        type: 'object',
        properties: {
          id: {
            type: 'string',
            description: 'The auth config id of the app (must be a valid auth config id)',
          },
        },
        required: ['id'],
      },
      connection: {
        type: 'object',
        properties: {
          data: {
            type: 'object',
            description: 'Initial data to pass to the connected account',
          },
          redirect_uri: {
            type: 'string',
            description: 'The URL to redirect to after connection completion',
          },
          user_id: {
            type: 'string',
            description: 'The user id of the connected account',
          },
        },
        required: [],
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.connectedAccounts.create(body);
};

export default { metadata, tool, handler };
