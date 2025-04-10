// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'action_execution',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'log_action_execution',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      cursor: {
        type: 'number',
        description: 'cursor_that_can_be_used_to_paginate_through_the_logs',
      },
      case_sensitive: {
        type: 'boolean',
        description: 'whether_the_search_is_case_sensitive_or_not',
      },
      from: {
        type: 'number',
        description: 'start_time_of_the_logs_in_epoch_time',
      },
      limit: {
        type: 'number',
        description: 'number_of_logs_to_return',
      },
      search_params: {
        type: 'array',
        items: {
          type: 'object',
          properties: {
            field: {
              type: 'string',
            },
            operation: {
              type: 'string',
            },
            value: {
              type: 'string',
            },
          },
          required: [],
        },
      },
      to: {
        type: 'number',
        description: 'end_time_of_the_logs_in_epoch_time',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { ...body } = args;
  return client.actionExecution.log(body);
};

export default { metadata, tool, handler };
