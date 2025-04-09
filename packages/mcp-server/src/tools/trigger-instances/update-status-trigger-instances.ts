// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'trigger_instances',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'update_status_trigger_instances',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      slug: {
        type: 'string',
        description: 'The slug of the trigger instance',
      },
      status: {
        type: 'string',
        description: 'The new status of the trigger',
        enum: ['enable', 'disable'],
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { status, ...body } = args;
  return client.triggerInstances.updateStatus(status, body);
};

export default { metadata, tool, handler };
