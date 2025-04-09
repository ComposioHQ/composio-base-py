// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../../../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'org.project.webhook',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'delete_project_org_webhook',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      type: {
        type: 'string',
        description: 'Type of the webhook',
        enum: ['trigger', 'event'],
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.org.project.webhook.delete(body);
};

export default { metadata, tool, handler };
