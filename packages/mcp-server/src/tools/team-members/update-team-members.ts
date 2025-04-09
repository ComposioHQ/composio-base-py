// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'team_members',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'update_team_members',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      id: {
        type: 'string',
      },
      email: {
        type: 'string',
      },
      name: {
        type: 'string',
      },
      role: {
        type: 'string',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { id, ...body } = args;
  return client.teamMembers.update(id, body);
};

export default { metadata, tool, handler };
