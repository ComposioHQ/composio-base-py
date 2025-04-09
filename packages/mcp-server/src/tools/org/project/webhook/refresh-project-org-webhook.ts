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
  name: 'refresh_project_org_webhook',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {},
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const {} = args;
  return client.org.project.webhook.refresh();
};

export default { metadata, tool, handler };
