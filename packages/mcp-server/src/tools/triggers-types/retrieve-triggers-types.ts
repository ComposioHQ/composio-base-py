// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'triggers_types',
  operation: 'read',
  tags: [],
};

export const tool: Tool = {
  name: 'retrieve_triggers_types',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      slug: {
        type: 'string',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { slug } = args;
  return client.triggersTypes.retrieve(slug);
};

export default { metadata, tool, handler };
