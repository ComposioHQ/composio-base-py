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
  name: 'list_triggers_types',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      auth_config_id: {
        type: 'string',
      },
      connected_account_id: {
        type: 'string',
      },
      cursor: {
        type: 'string',
      },
      limit: {
        type: 'number',
      },
      toolkit_slugs: {
        type: 'string',
        description: 'Comma separated list of toolkit slugs',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.triggersTypes.list(body);
};

export default { metadata, tool, handler };
