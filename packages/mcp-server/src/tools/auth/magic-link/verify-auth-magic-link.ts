// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'auth.magic_link',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'verify_auth_magic_link',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      token: {
        type: 'string',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.auth.magicLink.verify(body);
};

export default { metadata, tool, handler };
