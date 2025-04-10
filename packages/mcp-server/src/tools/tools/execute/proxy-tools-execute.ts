// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'tools.execute',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'proxy_tools_execute',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      endpoint: {
        type: 'string',
      },
      method: {
        type: 'string',
        enum: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
      },
      body: {
        type: 'object',
      },
      connected_account_id: {
        type: 'string',
      },
      parameters: {
        type: 'array',
        items: {
          type: 'object',
          properties: {
            name: {
              type: 'string',
            },
            type: {
              type: 'string',
              enum: ['header', 'query'],
            },
            value: {
              type: 'string',
            },
          },
          required: ['name', 'type', 'value'],
        },
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.tools.execute.proxy(body);
};

export default { metadata, tool, handler };
