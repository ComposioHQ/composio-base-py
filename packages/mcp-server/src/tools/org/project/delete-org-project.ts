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
  name: 'delete_org_project',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      projectId: {
        type: 'string',
        description: 'Project ID',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { projectId } = args;
  return client.org.project.delete(projectId);
};

export default { metadata, tool, handler };
