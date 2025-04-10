// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'org.project',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'create_org_project',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      name: {
        type: 'string',
        description: 'Name of the project',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.org.project.create(body);
};

export default { metadata, tool, handler };
