// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'action_execution',
  operation: 'read',
  tags: [],
};

export const tool: Tool = {
  name: 'retrieve_log_action_execution',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      id: {
        type: 'string',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { id } = args;
  return client.actionExecution.retrieveLog(id);
};

export default { metadata, tool, handler };
