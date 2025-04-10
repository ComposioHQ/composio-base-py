// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'org.api_key',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'regenerate_org_api_key',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {},
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const {} = args;
  return client.org.apiKey.regenerate();
};

export default { metadata, tool, handler };
