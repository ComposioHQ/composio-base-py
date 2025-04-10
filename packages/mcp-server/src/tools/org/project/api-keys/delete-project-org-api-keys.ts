// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../../../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'org.project.api_keys',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'delete_project_org_api_keys',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      projectId: {
        type: 'string',
        description: 'Project ID',
      },
      id: {
        type: 'string',
        description: 'API key ID',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { id, ...body } = args;
  return client.org.project.apiKeys.delete(id, body);
};

export default { metadata, tool, handler };
