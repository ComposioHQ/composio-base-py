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
  name: 'remove_upsert_trigger_instances',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      slug: {
        type: 'string',
        description: 'The slug of the trigger instance',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { slug } = args;
  return client.triggerInstances.removeUpsert(slug);
};

export default { metadata, tool, handler };
