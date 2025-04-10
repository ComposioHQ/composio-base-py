// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'trigger_instances.handle',
  operation: 'read',
  tags: [],
};

export const tool: Tool = {
  name: 'retrieve_trigger_instances_handle',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      slug: {
        type: 'string',
        description: 'The slug of the trigger instance',
      },
      projectId: {
        type: 'string',
        description: 'The project ID',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { projectId, ...body } = args;
  return client.triggerInstances.handle.retrieve(projectId, body);
};

export default { metadata, tool, handler };
