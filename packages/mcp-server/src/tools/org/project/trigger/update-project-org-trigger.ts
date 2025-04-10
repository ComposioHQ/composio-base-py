// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../../../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'org.project.trigger',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'update_project_org_trigger',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      enabled: {
        type: 'boolean',
        description: 'Enabled',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.org.project.trigger.update(body);
};

export default { metadata, tool, handler };
