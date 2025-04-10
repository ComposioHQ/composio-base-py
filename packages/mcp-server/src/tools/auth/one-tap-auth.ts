// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'auth',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'one_tap_auth',
  description: '',
  inputSchema: {
    type: 'object',
    anyOf: [
      {
        type: 'object',
        properties: {
          provider_name: {
            type: 'string',
            enum: ['github', 'google'],
          },
          data: {
            type: 'object',
            properties: {
              jwt: {
                type: 'string',
              },
            },
            required: ['jwt'],
          },
          type: {
            type: 'string',
            enum: ['jwt'],
          },
        },
      },
      {
        type: 'object',
        properties: {
          provider_name: {
            type: 'string',
            enum: ['github', 'google'],
          },
          data: {
            type: 'object',
            properties: {
              authCode: {
                type: 'string',
              },
            },
            required: ['authCode'],
          },
          type: {
            type: 'string',
            enum: ['auth-code'],
          },
        },
      },
    ],
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { provider_name, ...body } = args;
  return client.auth.oneTap(provider_name, body);
};

export default { metadata, tool, handler };
