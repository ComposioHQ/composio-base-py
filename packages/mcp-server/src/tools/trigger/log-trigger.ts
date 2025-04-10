// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'trigger',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'log_trigger',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      cursor: {
        type: 'string',
        description: 'cursor that can be used to paginate through the logs',
      },
      entityId: {
        type: 'string',
      },
      integrationId: {
        type: 'string',
      },
      limit: {
        type: 'number',
        description: 'number of logs to return',
      },
      search: {
        type: 'string',
        description: 'Search term to filter logs',
      },
      status: {
        type: 'string',
        description: 'Filter logs by their status level',
        enum: ['all', 'success', 'error'],
      },
      time: {
        type: 'string',
        description: 'Return logs from the last N time units',
        enum: ['5m', '30m', '6h', '1d', '1w', '1month', '1y'],
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.trigger.log(body);
};

export default { metadata, tool, handler };
