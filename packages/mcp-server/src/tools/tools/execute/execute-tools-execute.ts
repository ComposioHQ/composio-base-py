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
  name: 'execute_tools_execute',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      action: {
        type: 'string',
        description: 'The name of the action',
      },
      allow_tracing: {
        type: 'boolean',
      },
      arguments: {
        type: 'object',
      },
      connected_account_id: {
        type: 'string',
      },
      entity_id: {
        type: 'string',
      },
      text: {
        type: 'string',
      },
      version: {
        type: 'string',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { action, ...body } = args;
  return client.tools.execute.execute(action, body);
};

export default { metadata, tool, handler };
