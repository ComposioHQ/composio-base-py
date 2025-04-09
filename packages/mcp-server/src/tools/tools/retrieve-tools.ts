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
  name: 'retrieve_tools',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      tool_slug: {
        type: 'string',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { tool_slug } = args;
  return client.tools.retrieve(tool_slug);
};

export default { metadata, tool, handler };
