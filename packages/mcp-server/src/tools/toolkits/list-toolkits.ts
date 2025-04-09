// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'toolkits',
  operation: 'read',
  tags: [],
};

export const tool: Tool = {
  name: 'list_toolkits',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      category: {
        type: 'string',
      },
      is_local: {
        type: 'boolean',
      },
      managed_by: {
        type: 'string',
        enum: ['all', 'composio_managed', 'project_managed'],
      },
      sort_by: {
        type: 'string',
        enum: ['usage', 'alphabetically'],
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.toolkits.list(body);
};

export default { metadata, tool, handler };
