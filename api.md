# AuthConfigs

Types:

- <code><a href="./src/resources/auth-configs.ts">AuthConfigCreateResponse</a></code>
- <code><a href="./src/resources/auth-configs.ts">AuthConfigRetrieveResponse</a></code>
- <code><a href="./src/resources/auth-configs.ts">AuthConfigUpdateResponse</a></code>
- <code><a href="./src/resources/auth-configs.ts">AuthConfigListResponse</a></code>
- <code><a href="./src/resources/auth-configs.ts">AuthConfigDeleteResponse</a></code>
- <code><a href="./src/resources/auth-configs.ts">AuthConfigUpdateStatusResponse</a></code>

Methods:

- <code title="post /api/v3/auth_configs">client.authConfigs.<a href="./src/resources/auth-configs.ts">create</a>({ ...params }) -> AuthConfigCreateResponse</code>
- <code title="get /api/v3/auth_configs/{nanoid}">client.authConfigs.<a href="./src/resources/auth-configs.ts">retrieve</a>(nanoid) -> AuthConfigRetrieveResponse</code>
- <code title="patch /api/v3/auth_configs/{nanoid}">client.authConfigs.<a href="./src/resources/auth-configs.ts">update</a>(nanoid, { ...params }) -> AuthConfigUpdateResponse</code>
- <code title="get /api/v3/auth_configs">client.authConfigs.<a href="./src/resources/auth-configs.ts">list</a>({ ...params }) -> AuthConfigListResponse</code>
- <code title="delete /api/v3/auth_configs/{nanoid}">client.authConfigs.<a href="./src/resources/auth-configs.ts">delete</a>(nanoid) -> AuthConfigDeleteResponse</code>
- <code title="patch /api/v3/auth_configs/{nanoid}/{status}">client.authConfigs.<a href="./src/resources/auth-configs.ts">updateStatus</a>(status, { ...params }) -> AuthConfigUpdateStatusResponse</code>

# ConnectedAccounts

Types:

- <code><a href="./src/resources/connected-accounts.ts">ConnectedAccountCreateResponse</a></code>
- <code><a href="./src/resources/connected-accounts.ts">ConnectedAccountRetrieveResponse</a></code>
- <code><a href="./src/resources/connected-accounts.ts">ConnectedAccountListResponse</a></code>
- <code><a href="./src/resources/connected-accounts.ts">ConnectedAccountDeleteResponse</a></code>
- <code><a href="./src/resources/connected-accounts.ts">ConnectedAccountRefreshResponse</a></code>
- <code><a href="./src/resources/connected-accounts.ts">ConnectedAccountUpdateStatusResponse</a></code>

Methods:

- <code title="post /api/v3/connected_accounts">client.connectedAccounts.<a href="./src/resources/connected-accounts.ts">create</a>({ ...params }) -> ConnectedAccountCreateResponse</code>
- <code title="get /api/v3/connected_accounts/{nanoid}">client.connectedAccounts.<a href="./src/resources/connected-accounts.ts">retrieve</a>(nanoid) -> ConnectedAccountRetrieveResponse</code>
- <code title="get /api/v3/connected_accounts">client.connectedAccounts.<a href="./src/resources/connected-accounts.ts">list</a>({ ...params }) -> ConnectedAccountListResponse</code>
- <code title="delete /api/v3/connected_accounts/{nanoid}">client.connectedAccounts.<a href="./src/resources/connected-accounts.ts">delete</a>(nanoid) -> ConnectedAccountDeleteResponse</code>
- <code title="post /api/v3/connected_accounts/{nanoid}/refresh">client.connectedAccounts.<a href="./src/resources/connected-accounts.ts">refresh</a>(nanoid) -> ConnectedAccountRefreshResponse</code>
- <code title="patch /api/v3/connected_accounts/{nanoId}/status">client.connectedAccounts.<a href="./src/resources/connected-accounts.ts">updateStatus</a>(nanoID, { ...params }) -> ConnectedAccountUpdateStatusResponse</code>

# Trigger

Types:

- <code><a href="./src/resources/trigger.ts">TriggerLogResponse</a></code>

Methods:

- <code title="post /api/v3/internal/trigger/logs">client.trigger.<a href="./src/resources/trigger.ts">log</a>({ ...params }) -> TriggerLogResponse</code>

# ActionExecution

Types:

- <code><a href="./src/resources/action-execution.ts">ActionExecutionLogResponse</a></code>
- <code><a href="./src/resources/action-execution.ts">ActionExecutionRetrieveFieldsResponse</a></code>
- <code><a href="./src/resources/action-execution.ts">ActionExecutionRetrieveLogResponse</a></code>

Methods:

- <code title="post /api/v3/internal/action_execution/logs">client.actionExecution.<a href="./src/resources/action-execution.ts">log</a>({ ...params }) -> ActionExecutionLogResponse</code>
- <code title="get /api/v3/internal/action_execution/fields">client.actionExecution.<a href="./src/resources/action-execution.ts">retrieveFields</a>() -> ActionExecutionRetrieveFieldsResponse</code>
- <code title="get /api/v3/internal/action_execution/log/{id}">client.actionExecution.<a href="./src/resources/action-execution.ts">retrieveLog</a>(id) -> ActionExecutionRetrieveLogResponse</code>

# Org

## APIKey

Types:

- <code><a href="./src/resources/org/api-key.ts">APIKeyRetrieveResponse</a></code>
- <code><a href="./src/resources/org/api-key.ts">APIKeyRegenerateResponse</a></code>

Methods:

- <code title="get /api/v3/org/api_key">client.org.apiKey.<a href="./src/resources/org/api-key.ts">retrieve</a>() -> APIKeyRetrieveResponse</code>
- <code title="post /api/v3/org/api_key/regenerate">client.org.apiKey.<a href="./src/resources/org/api-key.ts">regenerate</a>() -> APIKeyRegenerateResponse</code>

## Project

Types:

- <code><a href="./src/resources/org/project/project.ts">ProjectCreateResponse</a></code>
- <code><a href="./src/resources/org/project/project.ts">ProjectRetrieveResponse</a></code>
- <code><a href="./src/resources/org/project/project.ts">ProjectListResponse</a></code>
- <code><a href="./src/resources/org/project/project.ts">ProjectDeleteResponse</a></code>

Methods:

- <code title="post /api/v3/org/project/new">client.org.project.<a href="./src/resources/org/project/project.ts">create</a>({ ...params }) -> ProjectCreateResponse</code>
- <code title="get /api/v3/org/project/{projectId}">client.org.project.<a href="./src/resources/org/project/project.ts">retrieve</a>(projectID) -> ProjectRetrieveResponse</code>
- <code title="get /api/v3/org/project/list">client.org.project.<a href="./src/resources/org/project/project.ts">list</a>() -> ProjectListResponse</code>
- <code title="delete /api/v3/org/project/delete/{projectId}">client.org.project.<a href="./src/resources/org/project/project.ts">delete</a>(projectID) -> ProjectDeleteResponse</code>

### APIKeys

Types:

- <code><a href="./src/resources/org/project/api-keys.ts">APIKeyCreateResponse</a></code>
- <code><a href="./src/resources/org/project/api-keys.ts">APIKeyListResponse</a></code>
- <code><a href="./src/resources/org/project/api-keys.ts">APIKeyDeleteResponse</a></code>
- <code><a href="./src/resources/org/project/api-keys.ts">APIKeyCreateAPIKeyResponse</a></code>

Methods:

- <code title="post /api/v3/org/project/{projectId}/api_keys/create">client.org.project.apiKeys.<a href="./src/resources/org/project/api-keys.ts">create</a>(projectID, { ...params }) -> APIKeyCreateResponse</code>
- <code title="get /api/v3/org/project/{projectId}/api_keys/list">client.org.project.apiKeys.<a href="./src/resources/org/project/api-keys.ts">list</a>(projectID) -> APIKeyListResponse</code>
- <code title="delete /api/v3/org/project/{projectId}/api_keys/remove/{id}">client.org.project.apiKeys.<a href="./src/resources/org/project/api-keys.ts">delete</a>(id, { ...params }) -> APIKeyDeleteResponse</code>
- <code title="post /api/v3/org/project/{projectId}/api_keys/create-api-key">client.org.project.apiKeys.<a href="./src/resources/org/project/api-keys.ts">createAPIKey</a>(projectID) -> APIKeyCreateAPIKeyResponse</code>

### Webhook

Types:

- <code><a href="./src/resources/org/project/webhook.ts">WebhookRetrieveResponse</a></code>
- <code><a href="./src/resources/org/project/webhook.ts">WebhookUpdateResponse</a></code>
- <code><a href="./src/resources/org/project/webhook.ts">WebhookDeleteResponse</a></code>
- <code><a href="./src/resources/org/project/webhook.ts">WebhookRefreshResponse</a></code>

Methods:

- <code title="get /api/v3/org/project/webhook">client.org.project.webhook.<a href="./src/resources/org/project/webhook.ts">retrieve</a>({ ...params }) -> WebhookRetrieveResponse</code>
- <code title="post /api/v3/org/project/webhook/update">client.org.project.webhook.<a href="./src/resources/org/project/webhook.ts">update</a>({ ...params }) -> WebhookUpdateResponse</code>
- <code title="delete /api/v3/org/project/webhook">client.org.project.webhook.<a href="./src/resources/org/project/webhook.ts">delete</a>({ ...params }) -> WebhookDeleteResponse</code>
- <code title="post /api/v3/org/project/webhook/refresh">client.org.project.webhook.<a href="./src/resources/org/project/webhook.ts">refresh</a>() -> WebhookRefreshResponse</code>

### Trigger

Types:

- <code><a href="./src/resources/org/project/trigger.ts">TriggerUpdateResponse</a></code>
- <code><a href="./src/resources/org/project/trigger.ts">TriggerListResponse</a></code>

Methods:

- <code title="patch /api/v3/org/project/trigger">client.org.project.trigger.<a href="./src/resources/org/project/trigger.ts">update</a>({ ...params }) -> TriggerUpdateResponse</code>
- <code title="get /api/v3/org/project/trigger">client.org.project.trigger.<a href="./src/resources/org/project/trigger.ts">list</a>() -> TriggerListResponse</code>

# TeamMembers

Types:

- <code><a href="./src/resources/team-members.ts">TeamMemberUpdateResponse</a></code>
- <code><a href="./src/resources/team-members.ts">TeamMemberListResponse</a></code>
- <code><a href="./src/resources/team-members.ts">TeamMemberInviteResponse</a></code>
- <code><a href="./src/resources/team-members.ts">TeamMemberRemoveResponse</a></code>

Methods:

- <code title="put /api/v3/team-members/update/{id}">client.teamMembers.<a href="./src/resources/team-members.ts">update</a>(id, { ...params }) -> TeamMemberUpdateResponse</code>
- <code title="get /api/v3/team-members/list">client.teamMembers.<a href="./src/resources/team-members.ts">list</a>() -> TeamMemberListResponse</code>
- <code title="post /api/v3/team-members/invite">client.teamMembers.<a href="./src/resources/team-members.ts">invite</a>({ ...params }) -> TeamMemberInviteResponse</code>
- <code title="delete /api/v3/team-members/remove/{id}">client.teamMembers.<a href="./src/resources/team-members.ts">remove</a>(id) -> TeamMemberRemoveResponse</code>

# Toolkits

Types:

- <code><a href="./src/resources/toolkits.ts">ToolkitRetrieveResponse</a></code>
- <code><a href="./src/resources/toolkits.ts">ToolkitListResponse</a></code>
- <code><a href="./src/resources/toolkits.ts">ToolkitRetrieveCategoriesResponse</a></code>

Methods:

- <code title="get /api/v3/toolkits/{slug}">client.toolkits.<a href="./src/resources/toolkits.ts">retrieve</a>(slug) -> ToolkitRetrieveResponse</code>
- <code title="get /api/v3/toolkits">client.toolkits.<a href="./src/resources/toolkits.ts">list</a>({ ...params }) -> ToolkitListResponse</code>
- <code title="get /api/v3/toolkits/categories">client.toolkits.<a href="./src/resources/toolkits.ts">retrieveCategories</a>() -> ToolkitRetrieveCategoriesResponse</code>

# Tools

Types:

- <code><a href="./src/resources/tools.ts">ToolRetrieveResponse</a></code>
- <code><a href="./src/resources/tools.ts">ToolListResponse</a></code>
- <code><a href="./src/resources/tools.ts">ToolExecuteResponse</a></code>
- <code><a href="./src/resources/tools.ts">ToolGetInputResponse</a></code>
- <code><a href="./src/resources/tools.ts">ToolProxyResponse</a></code>
- <code><a href="./src/resources/tools.ts">ToolRetrieveEnumResponse</a></code>

Methods:

- <code title="get /api/v3/tools/{tool_slug}">client.tools.<a href="./src/resources/tools.ts">retrieve</a>(toolSlug) -> ToolRetrieveResponse</code>
- <code title="get /api/v3/tools">client.tools.<a href="./src/resources/tools.ts">list</a>({ ...params }) -> ToolListResponse</code>
- <code title="post /api/v3/tools/execute/{action}">client.tools.<a href="./src/resources/tools.ts">execute</a>(action, { ...params }) -> ToolExecuteResponse</code>
- <code title="post /api/v3/tools/execute/{actionName}/input">client.tools.<a href="./src/resources/tools.ts">getInput</a>(actionName, { ...params }) -> ToolGetInputResponse</code>
- <code title="post /api/v3/tools/execute/proxy">client.tools.<a href="./src/resources/tools.ts">proxy</a>({ ...params }) -> ToolProxyResponse</code>
- <code title="get /api/v3/tools/enum">client.tools.<a href="./src/resources/tools.ts">retrieveEnum</a>() -> string</code>

# TriggerInstances

Types:

- <code><a href="./src/resources/trigger-instances/trigger-instances.ts">TriggerInstanceListActiveResponse</a></code>
- <code><a href="./src/resources/trigger-instances/trigger-instances.ts">TriggerInstanceRemoveUpsertResponse</a></code>
- <code><a href="./src/resources/trigger-instances/trigger-instances.ts">TriggerInstanceUpdateStatusResponse</a></code>
- <code><a href="./src/resources/trigger-instances/trigger-instances.ts">TriggerInstanceUpsertResponse</a></code>

Methods:

- <code title="get /api/v3/trigger_instances/active">client.triggerInstances.<a href="./src/resources/trigger-instances/trigger-instances.ts">listActive</a>({ ...params }) -> TriggerInstanceListActiveResponse</code>
- <code title="delete /api/v3/trigger_instances/{slug}/upsert">client.triggerInstances.<a href="./src/resources/trigger-instances/trigger-instances.ts">removeUpsert</a>(slug) -> TriggerInstanceRemoveUpsertResponse</code>
- <code title="patch /api/v3/trigger_instances/{slug}/status/{status}">client.triggerInstances.<a href="./src/resources/trigger-instances/trigger-instances.ts">updateStatus</a>(status, { ...params }) -> TriggerInstanceUpdateStatusResponse</code>
- <code title="post /api/v3/trigger_instances/{slug}/upsert">client.triggerInstances.<a href="./src/resources/trigger-instances/trigger-instances.ts">upsert</a>(slug, { ...params }) -> TriggerInstanceUpsertResponse</code>

## Handle

Types:

- <code><a href="./src/resources/trigger-instances/handle.ts">HandleRetrieveResponse</a></code>
- <code><a href="./src/resources/trigger-instances/handle.ts">HandleExecuteResponse</a></code>

Methods:

- <code title="get /api/v3/trigger_instances/{slug}/{projectId}/handle">client.triggerInstances.handle.<a href="./src/resources/trigger-instances/handle.ts">retrieve</a>(projectID, { ...params }) -> string</code>
- <code title="post /api/v3/trigger_instances/{slug}/{projectId}/handle">client.triggerInstances.handle.<a href="./src/resources/trigger-instances/handle.ts">execute</a>(projectID, { ...params }) -> string</code>

# TriggersTypes

Types:

- <code><a href="./src/resources/triggers-types.ts">TriggersTypeRetrieveResponse</a></code>
- <code><a href="./src/resources/triggers-types.ts">TriggersTypeListResponse</a></code>
- <code><a href="./src/resources/triggers-types.ts">TriggersTypeRetrieveEnumResponse</a></code>

Methods:

- <code title="get /api/v3/triggers_types/{slug}">client.triggersTypes.<a href="./src/resources/triggers-types.ts">retrieve</a>(slug) -> TriggersTypeRetrieveResponse</code>
- <code title="get /api/v3/triggers_types">client.triggersTypes.<a href="./src/resources/triggers-types.ts">list</a>({ ...params }) -> TriggersTypeListResponse</code>
- <code title="get /api/v3/triggers_types/list/enum">client.triggersTypes.<a href="./src/resources/triggers-types.ts">retrieveEnum</a>() -> string</code>
