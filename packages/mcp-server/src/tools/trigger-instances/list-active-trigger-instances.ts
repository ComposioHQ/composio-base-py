// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'trigger_instances',
  operation: 'read',
  tags: [],
};

export const tool: Tool = {
  name: 'list_active_trigger_instances',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      authConfigIds: {
        type: 'string',
        description: 'Comma-separated list of auth config IDs to filter triggers by',
      },
      connectedAccountIds: {
        type: 'string',
        description: 'Comma-separated list of connected account IDs to filter triggers by',
      },
      limit: {
        type: 'number',
        description: 'Number of items to return per page.',
      },
      page: {
        type: 'number',
        description: 'Page number for pagination. Starts from 1.',
      },
      showDisabled: {
        type: 'boolean',
        description: 'When set to true, includes disabled triggers in the response.',
      },
      triggerIds: {
        type: 'string',
        description: 'Comma-separated list of trigger IDs to filter triggers by',
      },
      triggerNames: {
        type: 'string',
        description: 'Comma-separated list of trigger names to filter triggers by',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.triggerInstances.listActive(body);
};

export default { metadata, tool, handler };
