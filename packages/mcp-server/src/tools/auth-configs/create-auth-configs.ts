// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'auth_configs',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'create_auth_configs',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      toolkit: {
        type: 'object',
        properties: {
          slug: {
            type: 'string',
            description: 'List of app unique keys to filter by',
          },
        },
        required: ['slug'],
      },
      auth_config: {
        anyOf: [
          {
            type: 'object',
            properties: {
              type: {
                type: 'string',
                enum: ['use_composio_managed_auth'],
              },
              credentials: {
                type: 'object',
              },
              name: {
                type: 'string',
                description: 'The name of the integration',
              },
            },
            required: ['type'],
          },
          {
            type: 'object',
            properties: {
              authScheme: {
                type: 'string',
                enum: [
                  'OAUTH2',
                  'OAUTH1',
                  'OAUTH1A',
                  'API_KEY',
                  'BASIC',
                  'BILLCOM_AUTH',
                  'BEARER_TOKEN',
                  'GOOGLE_SERVICE_ACCOUNT',
                  'NO_AUTH',
                  'BASIC_WITH_JWT',
                  'COMPOSIO_LINK',
                  'CALCOM_AUTH',
                  'SNOWFLAKE',
                ],
              },
              credentials: {
                type: 'object',
              },
              type: {
                type: 'string',
                enum: ['use_custom_auth'],
              },
              name: {
                type: 'string',
                description: 'The name of the integration',
              },
            },
            required: ['authScheme', 'credentials', 'type'],
          },
        ],
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.authConfigs.create(body);
};

export default { metadata, tool, handler };
