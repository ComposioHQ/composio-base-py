// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { Tool } from '@modelcontextprotocol/sdk/types.js';
import type { Metadata } from '../../';
import ComposioSDK from 'composio-sdk';

export const metadata: Metadata = {
  resource: 'tools.execute',
  operation: 'write',
  tags: [],
};

export const tool: Tool = {
  name: 'input_tools_execute',
  description: '',
  inputSchema: {
    type: 'object',
    properties: {
      actionName: {
        type: 'string',
      },
      text: {
        type: 'string',
        description:
          'The use-case description for the action, this will give context to LLM to generate the correct inputs for the action.',
      },
      customDescription: {
        type: 'string',
        description:
          'The custom description for the action, use this to provide customised context about the action to the LLM to suit your use-case.',
      },
      systemPrompt: {
        type: 'string',
        description:
          'The system prompt to be used by LLM, use this to control and guide the behaviour of the LLM.',
      },
      version: {
        type: 'string',
      },
    },
  },
};

export const handler = (client: ComposioSDK, args: any) => {
  const { actionName, ...body } = args;
  return client.tools.execute.input(actionName, body);
};

export default { metadata, tool, handler };
