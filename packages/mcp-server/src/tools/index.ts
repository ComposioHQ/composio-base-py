// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ComposioSDK from 'composio-sdk';
import { Tool } from '@modelcontextprotocol/sdk/types.js';

import create_auth_configs from './auth-configs/create-auth-configs';
import retrieve_auth_configs from './auth-configs/retrieve-auth-configs';
import update_auth_configs from './auth-configs/update-auth-configs';
import list_auth_configs from './auth-configs/list-auth-configs';
import delete_auth_configs from './auth-configs/delete-auth-configs';
import update_status_auth_configs from './auth-configs/update-status-auth-configs';
import create_connected_accounts from './connected-accounts/create-connected-accounts';
import retrieve_connected_accounts from './connected-accounts/retrieve-connected-accounts';
import list_connected_accounts from './connected-accounts/list-connected-accounts';
import delete_connected_accounts from './connected-accounts/delete-connected-accounts';
import refresh_connected_accounts from './connected-accounts/refresh-connected-accounts';
import update_status_connected_accounts from './connected-accounts/update-status-connected-accounts';
import log_trigger from './trigger/log-trigger';
import log_action_execution from './action-execution/log-action-execution';
import retrieve_fields_action_execution from './action-execution/retrieve-fields-action-execution';
import retrieve_log_action_execution from './action-execution/retrieve-log-action-execution';
import retrieve_org_api_key from './org/api-key/retrieve-org-api-key';
import regenerate_org_api_key from './org/api-key/regenerate-org-api-key';
import create_org_project from './org/project/create-org-project';
import retrieve_org_project from './org/project/retrieve-org-project';
import list_org_project from './org/project/list-org-project';
import delete_org_project from './org/project/delete-org-project';
import create_project_org_api_keys from './org/project/api-keys/create-project-org-api-keys';
import list_project_org_api_keys from './org/project/api-keys/list-project-org-api-keys';
import delete_project_org_api_keys from './org/project/api-keys/delete-project-org-api-keys';
import create_api_key_project_org_api_keys from './org/project/api-keys/create-api-key-project-org-api-keys';
import retrieve_project_org_webhook from './org/project/webhook/retrieve-project-org-webhook';
import update_project_org_webhook from './org/project/webhook/update-project-org-webhook';
import delete_project_org_webhook from './org/project/webhook/delete-project-org-webhook';
import refresh_project_org_webhook from './org/project/webhook/refresh-project-org-webhook';
import update_project_org_trigger from './org/project/trigger/update-project-org-trigger';
import list_project_org_trigger from './org/project/trigger/list-project-org-trigger';
import update_team_members from './team-members/update-team-members';
import list_team_members from './team-members/list-team-members';
import invite_team_members from './team-members/invite-team-members';
import remove_team_members from './team-members/remove-team-members';
import retrieve_toolkits from './toolkits/retrieve-toolkits';
import list_toolkits from './toolkits/list-toolkits';
import retrieve_categories_toolkits from './toolkits/retrieve-categories-toolkits';
import retrieve_tools from './tools/retrieve-tools';
import list_tools from './tools/list-tools';
import retrieve_enum_tools from './tools/retrieve-enum-tools';
import run_tools from './tools/run-tools';
import get_input_tools_execute from './tools/execute/get-input-tools-execute';
import proxy_tools_execute from './tools/execute/proxy-tools-execute';
import list_active_trigger_instances from './trigger-instances/list-active-trigger-instances';
import remove_upsert_trigger_instances from './trigger-instances/remove-upsert-trigger-instances';
import update_status_trigger_instances from './trigger-instances/update-status-trigger-instances';
import upsert_trigger_instances from './trigger-instances/upsert-trigger-instances';
import retrieve_trigger_instances_handle from './trigger-instances/handle/retrieve-trigger-instances-handle';
import execute_trigger_instances_handle from './trigger-instances/handle/execute-trigger-instances-handle';
import retrieve_triggers_types from './triggers-types/retrieve-triggers-types';
import list_triggers_types from './triggers-types/list-triggers-types';
import retrieve_enum_triggers_types from './triggers-types/retrieve-enum-triggers-types';

export type HandlerFunction = (client: ComposioSDK, args: any) => Promise<any>;

export type Metadata = {
  resource: string;
  operation: 'read' | 'write';
  tags: string[];
};

export type Endpoint = {
  metadata: Metadata;
  tool: Tool;
  handler: HandlerFunction;
};

export const endpoints: Endpoint[] = [];

function addEndpoint(endpoint: Endpoint) {
  endpoints.push(endpoint);
}

addEndpoint(create_auth_configs);
addEndpoint(retrieve_auth_configs);
addEndpoint(update_auth_configs);
addEndpoint(list_auth_configs);
addEndpoint(delete_auth_configs);
addEndpoint(update_status_auth_configs);
addEndpoint(create_connected_accounts);
addEndpoint(retrieve_connected_accounts);
addEndpoint(list_connected_accounts);
addEndpoint(delete_connected_accounts);
addEndpoint(refresh_connected_accounts);
addEndpoint(update_status_connected_accounts);
addEndpoint(log_trigger);
addEndpoint(log_action_execution);
addEndpoint(retrieve_fields_action_execution);
addEndpoint(retrieve_log_action_execution);
addEndpoint(retrieve_org_api_key);
addEndpoint(regenerate_org_api_key);
addEndpoint(create_org_project);
addEndpoint(retrieve_org_project);
addEndpoint(list_org_project);
addEndpoint(delete_org_project);
addEndpoint(create_project_org_api_keys);
addEndpoint(list_project_org_api_keys);
addEndpoint(delete_project_org_api_keys);
addEndpoint(create_api_key_project_org_api_keys);
addEndpoint(retrieve_project_org_webhook);
addEndpoint(update_project_org_webhook);
addEndpoint(delete_project_org_webhook);
addEndpoint(refresh_project_org_webhook);
addEndpoint(update_project_org_trigger);
addEndpoint(list_project_org_trigger);
addEndpoint(update_team_members);
addEndpoint(list_team_members);
addEndpoint(invite_team_members);
addEndpoint(remove_team_members);
addEndpoint(retrieve_toolkits);
addEndpoint(list_toolkits);
addEndpoint(retrieve_categories_toolkits);
addEndpoint(retrieve_tools);
addEndpoint(list_tools);
addEndpoint(retrieve_enum_tools);
addEndpoint(run_tools);
addEndpoint(get_input_tools_execute);
addEndpoint(proxy_tools_execute);
addEndpoint(list_active_trigger_instances);
addEndpoint(remove_upsert_trigger_instances);
addEndpoint(update_status_trigger_instances);
addEndpoint(upsert_trigger_instances);
addEndpoint(retrieve_trigger_instances_handle);
addEndpoint(execute_trigger_instances_handle);
addEndpoint(retrieve_triggers_types);
addEndpoint(list_triggers_types);
addEndpoint(retrieve_enum_triggers_types);

export type Filter = {
  type: 'resource' | 'operation' | 'tag' | 'tool';
  op: 'include' | 'exclude';
  value: string;
};

export function query(filters: Filter[], endpoints: Endpoint[]): Endpoint[] {
  if (filters.length === 0) {
    return endpoints;
  }
  const allExcludes = filters.every((filter) => filter.op === 'exclude');

  return endpoints.filter((endpoint: Endpoint) => {
    let included = false || allExcludes;

    for (const filter of filters) {
      if (match(filter, endpoint)) {
        included = filter.op === 'include';
      }
    }

    return included;
  });
}

function match({ type, value }: Filter, endpoint: Endpoint): boolean {
  switch (type) {
    case 'resource': {
      const regexStr = '^' + normalizeResource(value).replace(/\*/g, '.*') + '$';
      const regex = new RegExp(regexStr);
      return regex.test(normalizeResource(endpoint.metadata.resource));
    }
    case 'operation':
      return endpoint.metadata.operation === value;
    case 'tag':
      return endpoint.metadata.tags.includes(value);
    case 'tool':
      return endpoint.tool.name === value;
  }
}

function normalizeResource(resource: string): string {
  return resource.toLowerCase().replace(/[^a-z.*\-_]*/g, '');
}
