# API

## Auth

Types:

- <code><a href="./src/resources/api/auth/auth.ts">AuthOneTapResponse</a></code>
- <code><a href="./src/resources/api/auth/auth.ts">AuthRetrieveCallbackResponse</a></code>

Methods:

- <code title="get /api/v3/auth/{provider_name}/login">client.api.auth.<a href="./src/resources/api/auth/auth.ts">login</a>(providerName, { ...params }) -> void</code>
- <code title="post /api/v3/auth/{provider_name}/one-tap">client.api.auth.<a href="./src/resources/api/auth/auth.ts">oneTap</a>(providerName, { ...params }) -> AuthOneTapResponse</code>
- <code title="get /api/v3/auth/{provider_name}/callback">client.api.auth.<a href="./src/resources/api/auth/auth.ts">retrieveCallback</a>(providerName, { ...params }) -> AuthRetrieveCallbackResponse</code>

### MagicLink

Types:

- <code><a href="./src/resources/api/auth/magic-link.ts">MagicLinkSendResponse</a></code>
- <code><a href="./src/resources/api/auth/magic-link.ts">MagicLinkVerifyResponse</a></code>

Methods:

- <code title="post /api/v3/auth/magic_link/send">client.api.auth.magicLink.<a href="./src/resources/api/auth/magic-link.ts">send</a>({ ...params }) -> MagicLinkSendResponse</code>
- <code title="post /api/v3/auth/magic_link/verify">client.api.auth.magicLink.<a href="./src/resources/api/auth/magic-link.ts">verify</a>({ ...params }) -> MagicLinkVerifyResponse</code>

### Session

Types:

- <code><a href="./src/resources/api/auth/session.ts">SessionLogoutResponse</a></code>
- <code><a href="./src/resources/api/auth/session.ts">SessionRetrieveInfoResponse</a></code>

Methods:

- <code title="post /api/v3/auth/session/logout">client.api.auth.session.<a href="./src/resources/api/auth/session.ts">logout</a>() -> SessionLogoutResponse</code>
- <code title="get /api/v3/auth/session/info">client.api.auth.session.<a href="./src/resources/api/auth/session.ts">retrieveInfo</a>() -> SessionRetrieveInfoResponse</code>

## Admin

Types:

- <code><a href="./src/resources/api/admin.ts">AdminIdentifyResponse</a></code>

Methods:

- <code title="post /api/v3/admin/identify">client.api.admin.<a href="./src/resources/api/admin.ts">identify</a>({ ...params }) -> AdminIdentifyResponse</code>

## AuthConfigs

Types:

- <code><a href="./src/resources/api/auth-configs.ts">AuthConfigCreateResponse</a></code>
- <code><a href="./src/resources/api/auth-configs.ts">AuthConfigRetrieveResponse</a></code>
- <code><a href="./src/resources/api/auth-configs.ts">AuthConfigUpdateResponse</a></code>
- <code><a href="./src/resources/api/auth-configs.ts">AuthConfigListResponse</a></code>
- <code><a href="./src/resources/api/auth-configs.ts">AuthConfigDeleteResponse</a></code>
- <code><a href="./src/resources/api/auth-configs.ts">AuthConfigUpdateStatusResponse</a></code>

Methods:

- <code title="post /api/v3/auth_configs">client.api.authConfigs.<a href="./src/resources/api/auth-configs.ts">create</a>({ ...params }) -> AuthConfigCreateResponse</code>
- <code title="get /api/v3/auth_configs/{nanoid}">client.api.authConfigs.<a href="./src/resources/api/auth-configs.ts">retrieve</a>(nanoid) -> AuthConfigRetrieveResponse</code>
- <code title="patch /api/v3/auth_configs/{nanoid}">client.api.authConfigs.<a href="./src/resources/api/auth-configs.ts">update</a>(nanoid, { ...params }) -> AuthConfigUpdateResponse</code>
- <code title="get /api/v3/auth_configs">client.api.authConfigs.<a href="./src/resources/api/auth-configs.ts">list</a>({ ...params }) -> AuthConfigListResponse</code>
- <code title="delete /api/v3/auth_configs/{nanoid}">client.api.authConfigs.<a href="./src/resources/api/auth-configs.ts">delete</a>(nanoid) -> AuthConfigDeleteResponse</code>
- <code title="patch /api/v3/auth_configs/{nanoid}/{status}">client.api.authConfigs.<a href="./src/resources/api/auth-configs.ts">updateStatus</a>(status, { ...params }) -> AuthConfigUpdateStatusResponse</code>

## Cli

Types:

- <code><a href="./src/resources/api/cli.ts">CliCreateSessionResponse</a></code>
- <code><a href="./src/resources/api/cli.ts">CliLinkSessionResponse</a></code>
- <code><a href="./src/resources/api/cli.ts">CliRetrieveSessionResponse</a></code>

Methods:

- <code title="post /api/v3/cli/create-session">client.api.cli.<a href="./src/resources/api/cli.ts">createSession</a>() -> CliCreateSessionResponse</code>
- <code title="put /api/v3/cli/link-session">client.api.cli.<a href="./src/resources/api/cli.ts">linkSession</a>({ ...params }) -> CliLinkSessionResponse</code>
- <code title="get /api/v3/cli/get-session">client.api.cli.<a href="./src/resources/api/cli.ts">retrieveSession</a>({ ...params }) -> CliRetrieveSessionResponse</code>

## ConnectedAccounts

Types:

- <code><a href="./src/resources/api/connected-accounts.ts">ConnectedAccountCreateResponse</a></code>
- <code><a href="./src/resources/api/connected-accounts.ts">ConnectedAccountRetrieveResponse</a></code>
- <code><a href="./src/resources/api/connected-accounts.ts">ConnectedAccountListResponse</a></code>
- <code><a href="./src/resources/api/connected-accounts.ts">ConnectedAccountDeleteResponse</a></code>
- <code><a href="./src/resources/api/connected-accounts.ts">ConnectedAccountRefreshResponse</a></code>
- <code><a href="./src/resources/api/connected-accounts.ts">ConnectedAccountUpdateStatusResponse</a></code>

Methods:

- <code title="post /api/v3/connected_accounts">client.api.connectedAccounts.<a href="./src/resources/api/connected-accounts.ts">create</a>({ ...params }) -> ConnectedAccountCreateResponse</code>
- <code title="get /api/v3/connected_accounts/{nanoid}">client.api.connectedAccounts.<a href="./src/resources/api/connected-accounts.ts">retrieve</a>(nanoid) -> ConnectedAccountRetrieveResponse</code>
- <code title="get /api/v3/connected_accounts">client.api.connectedAccounts.<a href="./src/resources/api/connected-accounts.ts">list</a>({ ...params }) -> ConnectedAccountListResponse</code>
- <code title="delete /api/v3/connected_accounts/{nanoid}">client.api.connectedAccounts.<a href="./src/resources/api/connected-accounts.ts">delete</a>(nanoid) -> ConnectedAccountDeleteResponse</code>
- <code title="post /api/v3/connected_accounts/{nanoid}/refresh">client.api.connectedAccounts.<a href="./src/resources/api/connected-accounts.ts">refresh</a>(nanoid) -> ConnectedAccountRefreshResponse</code>
- <code title="patch /api/v3/connected_accounts/{nanoId}/status">client.api.connectedAccounts.<a href="./src/resources/api/connected-accounts.ts">updateStatus</a>(nanoID, { ...params }) -> ConnectedAccountUpdateStatusResponse</code>

## Internal

### Trigger

Types:

- <code><a href="./src/resources/api/internal/trigger.ts">TriggerLogResponse</a></code>

Methods:

- <code title="post /api/v3/internal/trigger/logs">client.api.internal.trigger.<a href="./src/resources/api/internal/trigger.ts">log</a>({ ...params }) -> TriggerLogResponse</code>

### ActionExecution

Types:

- <code><a href="./src/resources/api/internal/action-execution.ts">ActionExecutionLogResponse</a></code>
- <code><a href="./src/resources/api/internal/action-execution.ts">ActionExecutionRetrieveFieldsResponse</a></code>
- <code><a href="./src/resources/api/internal/action-execution.ts">ActionExecutionRetrieveLogResponse</a></code>

Methods:

- <code title="post /api/v3/internal/action_execution/logs">client.api.internal.actionExecution.<a href="./src/resources/api/internal/action-execution.ts">log</a>({ ...params }) -> ActionExecutionLogResponse</code>
- <code title="get /api/v3/internal/action_execution/fields">client.api.internal.actionExecution.<a href="./src/resources/api/internal/action-execution.ts">retrieveFields</a>() -> ActionExecutionRetrieveFieldsResponse</code>
- <code title="get /api/v3/internal/action_execution/log/{id}">client.api.internal.actionExecution.<a href="./src/resources/api/internal/action-execution.ts">retrieveLog</a>(id) -> ActionExecutionRetrieveLogResponse</code>

## OpenAPI

### Specs

Types:

- <code><a href="./src/resources/api/openapi/specs.ts">SpecCreateResponse</a></code>
- <code><a href="./src/resources/api/openapi/specs.ts">SpecListResponse</a></code>
- <code><a href="./src/resources/api/openapi/specs.ts">SpecDeleteResponse</a></code>
- <code><a href="./src/resources/api/openapi/specs.ts">SpecRetrieveStatusResponse</a></code>

Methods:

- <code title="post /api/v3/openapi/specs/create">client.api.openAPI.specs.<a href="./src/resources/api/openapi/specs.ts">create</a>({ ...params }) -> SpecCreateResponse</code>
- <code title="get /api/v3/openapi/specs/list">client.api.openAPI.specs.<a href="./src/resources/api/openapi/specs.ts">list</a>() -> SpecListResponse</code>
- <code title="delete /api/v3/openapi/specs/{id}">client.api.openAPI.specs.<a href="./src/resources/api/openapi/specs.ts">delete</a>(id) -> SpecDeleteResponse</code>
- <code title="get /api/v3/openapi/specs/status/{id}">client.api.openAPI.specs.<a href="./src/resources/api/openapi/specs.ts">retrieveStatus</a>(id) -> SpecRetrieveStatusResponse</code>

## Org

### APIKey

Types:

- <code><a href="./src/resources/api/org/api-key.ts">APIKeyRetrieveResponse</a></code>
- <code><a href="./src/resources/api/org/api-key.ts">APIKeyRegenerateResponse</a></code>

Methods:

- <code title="get /api/v3/org/api_key">client.api.org.apiKey.<a href="./src/resources/api/org/api-key.ts">retrieve</a>() -> APIKeyRetrieveResponse</code>
- <code title="post /api/v3/org/api_key/regenerate">client.api.org.apiKey.<a href="./src/resources/api/org/api-key.ts">regenerate</a>() -> APIKeyRegenerateResponse</code>

### Project

Types:

- <code><a href="./src/resources/api/org/project/project.ts">ProjectCreateResponse</a></code>
- <code><a href="./src/resources/api/org/project/project.ts">ProjectRetrieveResponse</a></code>
- <code><a href="./src/resources/api/org/project/project.ts">ProjectListResponse</a></code>
- <code><a href="./src/resources/api/org/project/project.ts">ProjectDeleteResponse</a></code>

Methods:

- <code title="post /api/v3/org/project/new">client.api.org.project.<a href="./src/resources/api/org/project/project.ts">create</a>({ ...params }) -> ProjectCreateResponse</code>
- <code title="get /api/v3/org/project/{projectId}">client.api.org.project.<a href="./src/resources/api/org/project/project.ts">retrieve</a>(projectID) -> ProjectRetrieveResponse</code>
- <code title="get /api/v3/org/project/list">client.api.org.project.<a href="./src/resources/api/org/project/project.ts">list</a>() -> ProjectListResponse</code>
- <code title="delete /api/v3/org/project/delete/{projectId}">client.api.org.project.<a href="./src/resources/api/org/project/project.ts">delete</a>(projectID) -> ProjectDeleteResponse</code>

#### APIKeys

Types:

- <code><a href="./src/resources/api/org/project/api-keys.ts">APIKeyCreateResponse</a></code>
- <code><a href="./src/resources/api/org/project/api-keys.ts">APIKeyListResponse</a></code>
- <code><a href="./src/resources/api/org/project/api-keys.ts">APIKeyDeleteResponse</a></code>
- <code><a href="./src/resources/api/org/project/api-keys.ts">APIKeyCreateAPIKeyResponse</a></code>

Methods:

- <code title="post /api/v3/org/project/{projectId}/api_keys/create">client.api.org.project.apiKeys.<a href="./src/resources/api/org/project/api-keys.ts">create</a>(projectID, { ...params }) -> APIKeyCreateResponse</code>
- <code title="get /api/v3/org/project/{projectId}/api_keys/list">client.api.org.project.apiKeys.<a href="./src/resources/api/org/project/api-keys.ts">list</a>(projectID) -> APIKeyListResponse</code>
- <code title="delete /api/v3/org/project/{projectId}/api_keys/remove/{id}">client.api.org.project.apiKeys.<a href="./src/resources/api/org/project/api-keys.ts">delete</a>(id, { ...params }) -> APIKeyDeleteResponse</code>
- <code title="post /api/v3/org/project/{projectId}/api_keys/create-api-key">client.api.org.project.apiKeys.<a href="./src/resources/api/org/project/api-keys.ts">createAPIKey</a>(projectID) -> APIKeyCreateAPIKeyResponse</code>

#### Webhook

Types:

- <code><a href="./src/resources/api/org/project/webhook.ts">WebhookRetrieveResponse</a></code>
- <code><a href="./src/resources/api/org/project/webhook.ts">WebhookUpdateResponse</a></code>
- <code><a href="./src/resources/api/org/project/webhook.ts">WebhookDeleteResponse</a></code>
- <code><a href="./src/resources/api/org/project/webhook.ts">WebhookRefreshResponse</a></code>

Methods:

- <code title="get /api/v3/org/project/webhook">client.api.org.project.webhook.<a href="./src/resources/api/org/project/webhook.ts">retrieve</a>({ ...params }) -> WebhookRetrieveResponse</code>
- <code title="post /api/v3/org/project/webhook/update">client.api.org.project.webhook.<a href="./src/resources/api/org/project/webhook.ts">update</a>({ ...params }) -> WebhookUpdateResponse</code>
- <code title="delete /api/v3/org/project/webhook">client.api.org.project.webhook.<a href="./src/resources/api/org/project/webhook.ts">delete</a>({ ...params }) -> WebhookDeleteResponse</code>
- <code title="post /api/v3/org/project/webhook/refresh">client.api.org.project.webhook.<a href="./src/resources/api/org/project/webhook.ts">refresh</a>() -> WebhookRefreshResponse</code>

#### Trigger

Types:

- <code><a href="./src/resources/api/org/project/trigger.ts">TriggerUpdateResponse</a></code>
- <code><a href="./src/resources/api/org/project/trigger.ts">TriggerListResponse</a></code>

Methods:

- <code title="patch /api/v3/org/project/trigger">client.api.org.project.trigger.<a href="./src/resources/api/org/project/trigger.ts">update</a>({ ...params }) -> TriggerUpdateResponse</code>
- <code title="get /api/v3/org/project/trigger">client.api.org.project.trigger.<a href="./src/resources/api/org/project/trigger.ts">list</a>() -> TriggerListResponse</code>

## TeamMembers

Types:

- <code><a href="./src/resources/api/team-members.ts">TeamMemberUpdateResponse</a></code>
- <code><a href="./src/resources/api/team-members.ts">TeamMemberListResponse</a></code>
- <code><a href="./src/resources/api/team-members.ts">TeamMemberInviteResponse</a></code>
- <code><a href="./src/resources/api/team-members.ts">TeamMemberRemoveResponse</a></code>

Methods:

- <code title="put /api/v3/team-members/update/{id}">client.api.teamMembers.<a href="./src/resources/api/team-members.ts">update</a>(id, { ...params }) -> TeamMemberUpdateResponse</code>
- <code title="get /api/v3/team-members/list">client.api.teamMembers.<a href="./src/resources/api/team-members.ts">list</a>() -> TeamMemberListResponse</code>
- <code title="post /api/v3/team-members/invite">client.api.teamMembers.<a href="./src/resources/api/team-members.ts">invite</a>({ ...params }) -> TeamMemberInviteResponse</code>
- <code title="delete /api/v3/team-members/remove/{id}">client.api.teamMembers.<a href="./src/resources/api/team-members.ts">remove</a>(id) -> TeamMemberRemoveResponse</code>

## Toolkits

Types:

- <code><a href="./src/resources/api/toolkits.ts">ToolkitRetrieveResponse</a></code>
- <code><a href="./src/resources/api/toolkits.ts">ToolkitListResponse</a></code>
- <code><a href="./src/resources/api/toolkits.ts">ToolkitRetrieveCategoriesResponse</a></code>

Methods:

- <code title="get /api/v3/toolkits/{slug}">client.api.toolkits.<a href="./src/resources/api/toolkits.ts">retrieve</a>(slug) -> ToolkitRetrieveResponse</code>
- <code title="get /api/v3/toolkits">client.api.toolkits.<a href="./src/resources/api/toolkits.ts">list</a>({ ...params }) -> ToolkitListResponse</code>
- <code title="get /api/v3/toolkits/categories">client.api.toolkits.<a href="./src/resources/api/toolkits.ts">retrieveCategories</a>() -> ToolkitRetrieveCategoriesResponse</code>

## Tools

Types:

- <code><a href="./src/resources/api/tools/tools.ts">ToolRetrieveResponse</a></code>
- <code><a href="./src/resources/api/tools/tools.ts">ToolListResponse</a></code>
- <code><a href="./src/resources/api/tools/tools.ts">ToolRetrieveEnumResponse</a></code>

Methods:

- <code title="get /api/v3/tools/{tool_slug}">client.api.tools.<a href="./src/resources/api/tools/tools.ts">retrieve</a>(toolSlug) -> ToolRetrieveResponse</code>
- <code title="get /api/v3/tools">client.api.tools.<a href="./src/resources/api/tools/tools.ts">list</a>({ ...params }) -> ToolListResponse</code>
- <code title="get /api/v3/tools/enum">client.api.tools.<a href="./src/resources/api/tools/tools.ts">retrieveEnum</a>() -> string</code>

### Execute

Types:

- <code><a href="./src/resources/api/tools/execute.ts">ExecuteInputResponse</a></code>
- <code><a href="./src/resources/api/tools/execute.ts">ExecuteProxyResponse</a></code>
- <code><a href="./src/resources/api/tools/execute.ts">ExecuteRunResponse</a></code>

Methods:

- <code title="post /api/v3/tools/execute/{actionName}/input">client.api.tools.execute.<a href="./src/resources/api/tools/execute.ts">input</a>(actionName, { ...params }) -> ExecuteInputResponse</code>
- <code title="post /api/v3/tools/execute/proxy">client.api.tools.execute.<a href="./src/resources/api/tools/execute.ts">proxy</a>({ ...params }) -> ExecuteProxyResponse</code>
- <code title="post /api/v3/tools/execute/{action}">client.api.tools.execute.<a href="./src/resources/api/tools/execute.ts">run</a>(action, { ...params }) -> ExecuteRunResponse</code>

## TriggerInstances

Types:

- <code><a href="./src/resources/api/trigger-instances/trigger-instances.ts">TriggerInstanceListActiveResponse</a></code>
- <code><a href="./src/resources/api/trigger-instances/trigger-instances.ts">TriggerInstanceRemoveUpsertResponse</a></code>
- <code><a href="./src/resources/api/trigger-instances/trigger-instances.ts">TriggerInstanceUpdateStatusResponse</a></code>
- <code><a href="./src/resources/api/trigger-instances/trigger-instances.ts">TriggerInstanceUpsertResponse</a></code>

Methods:

- <code title="get /api/v3/trigger_instances/active">client.api.triggerInstances.<a href="./src/resources/api/trigger-instances/trigger-instances.ts">listActive</a>({ ...params }) -> TriggerInstanceListActiveResponse</code>
- <code title="delete /api/v3/trigger_instances/{slug}/upsert">client.api.triggerInstances.<a href="./src/resources/api/trigger-instances/trigger-instances.ts">removeUpsert</a>(slug) -> TriggerInstanceRemoveUpsertResponse</code>
- <code title="patch /api/v3/trigger_instances/{slug}/status/{status}">client.api.triggerInstances.<a href="./src/resources/api/trigger-instances/trigger-instances.ts">updateStatus</a>(status, { ...params }) -> TriggerInstanceUpdateStatusResponse</code>
- <code title="post /api/v3/trigger_instances/{slug}/upsert">client.api.triggerInstances.<a href="./src/resources/api/trigger-instances/trigger-instances.ts">upsert</a>(slug, { ...params }) -> TriggerInstanceUpsertResponse</code>

### Handle

Types:

- <code><a href="./src/resources/api/trigger-instances/handle.ts">HandleRetrieveResponse</a></code>
- <code><a href="./src/resources/api/trigger-instances/handle.ts">HandleExecuteResponse</a></code>

Methods:

- <code title="get /api/v3/trigger_instances/{slug}/{projectId}/handle">client.api.triggerInstances.handle.<a href="./src/resources/api/trigger-instances/handle.ts">retrieve</a>(projectID, { ...params }) -> string</code>
- <code title="post /api/v3/trigger_instances/{slug}/{projectId}/handle">client.api.triggerInstances.handle.<a href="./src/resources/api/trigger-instances/handle.ts">execute</a>(projectID, { ...params }) -> string</code>

## TriggersTypes

Types:

- <code><a href="./src/resources/api/triggers-types.ts">TriggersTypeRetrieveResponse</a></code>
- <code><a href="./src/resources/api/triggers-types.ts">TriggersTypeListResponse</a></code>
- <code><a href="./src/resources/api/triggers-types.ts">TriggersTypeRetrieveEnumResponse</a></code>

Methods:

- <code title="get /api/v3/triggers_types/{slug}">client.api.triggersTypes.<a href="./src/resources/api/triggers-types.ts">retrieve</a>(slug) -> TriggersTypeRetrieveResponse</code>
- <code title="get /api/v3/triggers_types">client.api.triggersTypes.<a href="./src/resources/api/triggers-types.ts">list</a>({ ...params }) -> TriggersTypeListResponse</code>
- <code title="get /api/v3/triggers_types/list/enum">client.api.triggersTypes.<a href="./src/resources/api/triggers-types.ts">retrieveEnum</a>() -> string</code>

## Payments

Types:

- <code><a href="./src/resources/api/payments.ts">PaymentCreateSessionResponse</a></code>
- <code><a href="./src/resources/api/payments.ts">PaymentManageSubscriptionResponse</a></code>

Methods:

- <code title="post /api/v3/payments/session">client.api.payments.<a href="./src/resources/api/payments.ts">createSession</a>({ ...params }) -> PaymentCreateSessionResponse</code>
- <code title="post /api/v3/payments/manage-subscription">client.api.payments.<a href="./src/resources/api/payments.ts">manageSubscription</a>() -> PaymentManageSubscriptionResponse</code>
