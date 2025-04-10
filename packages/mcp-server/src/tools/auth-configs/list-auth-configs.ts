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
  name: 'list_auth_configs',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      cursor: {
        type: 'string',
        description: 'The cursor to paginate through the auth configs',
      },
      is_composio_managed: {
        anyOf: [
          {
            type: 'string',
          },
          {
            type: 'boolean',
          },
        ],
        description: 'Whether to filter by composio managed auth configs',
      },
      limit: {
        type: 'string',
        description: 'The number of auth configs to return',
      },
      toolkit_slug: {
        type: 'string',
        description: 'The slug of the toolkit to filter by',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.authConfigs.list(body);
};

export default { metadata, tool, handler };
