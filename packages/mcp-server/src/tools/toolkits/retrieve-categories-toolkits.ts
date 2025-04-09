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
  name: 'retrieve_categories_toolkits',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {},
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const {} = args;
  return client.toolkits.retrieveCategories();
};

export default { metadata, tool, handler };
