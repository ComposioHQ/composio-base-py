// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'tools',
  operation: 'read',
  tags: [],
};

export const tool: Tool = {
  name: 'list_tools',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      cursor: {
        type: 'string',
        description: 'The cursor to paginate through the results',
      },
      important: {
        type: 'string',
        description: 'Whether to filter by important tools',
      },
      limit: {
        type: 'string',
        description: 'The number of results to return',
      },
      search: {
        type: 'string',
        description: 'The search query to filter by',
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
  return client.tools.list(body);
};

export default { metadata, tool, handler };
