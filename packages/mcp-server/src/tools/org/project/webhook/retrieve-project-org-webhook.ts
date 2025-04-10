// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../../../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'org.project.webhook',
  operation: 'read',
  tags: [],
};

export const tool: Tool = {
  name: 'retrieve_project_org_webhook',
  description: 'Get the webhook URL for a project',
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
  return client.org.project.webhook.retrieve(body);
};

export default { metadata, tool, handler };
