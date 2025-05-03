# AuthConfigs

Types:

```python
from composio_client.types import (
    AuthConfigCreateResponse,
    AuthConfigRetrieveResponse,
    AuthConfigUpdateResponse,
    AuthConfigListResponse,
    AuthConfigDeleteResponse,
    AuthConfigUpdateStatusResponse,
)
```

Methods:

- <code title="post /api/v3/auth_configs">client.auth_configs.<a href="./src/composio_client/resources/auth_configs.py">create</a>(\*\*<a href="src/composio_client/types/auth_config_create_params.py">params</a>) -> <a href="./src/composio_client/types/auth_config_create_response.py">AuthConfigCreateResponse</a></code>
- <code title="get /api/v3/auth_configs/{nanoid}">client.auth_configs.<a href="./src/composio_client/resources/auth_configs.py">retrieve</a>(nanoid) -> <a href="./src/composio_client/types/auth_config_retrieve_response.py">AuthConfigRetrieveResponse</a></code>
- <code title="patch /api/v3/auth_configs/{nanoid}">client.auth_configs.<a href="./src/composio_client/resources/auth_configs.py">update</a>(nanoid, \*\*<a href="src/composio_client/types/auth_config_update_params.py">params</a>) -> <a href="./src/composio_client/types/auth_config_update_response.py">object</a></code>
- <code title="get /api/v3/auth_configs">client.auth_configs.<a href="./src/composio_client/resources/auth_configs.py">list</a>(\*\*<a href="src/composio_client/types/auth_config_list_params.py">params</a>) -> <a href="./src/composio_client/types/auth_config_list_response.py">AuthConfigListResponse</a></code>
- <code title="delete /api/v3/auth_configs/{nanoid}">client.auth_configs.<a href="./src/composio_client/resources/auth_configs.py">delete</a>(nanoid) -> <a href="./src/composio_client/types/auth_config_delete_response.py">object</a></code>
- <code title="patch /api/v3/auth_configs/{nanoid}/{status}">client.auth_configs.<a href="./src/composio_client/resources/auth_configs.py">update_status</a>(status, \*, nanoid) -> <a href="./src/composio_client/types/auth_config_update_status_response.py">object</a></code>

# ConnectedAccounts

Types:

```python
from composio_client.types import (
    ConnectedAccountCreateResponse,
    ConnectedAccountRetrieveResponse,
    ConnectedAccountListResponse,
    ConnectedAccountDeleteResponse,
    ConnectedAccountRefreshResponse,
    ConnectedAccountUpdateStatusResponse,
)
```

Methods:

- <code title="post /api/v3/connected_accounts">client.connected_accounts.<a href="./src/composio_client/resources/connected_accounts.py">create</a>(\*\*<a href="src/composio_client/types/connected_account_create_params.py">params</a>) -> <a href="./src/composio_client/types/connected_account_create_response.py">ConnectedAccountCreateResponse</a></code>
- <code title="get /api/v3/connected_accounts/{nanoid}">client.connected_accounts.<a href="./src/composio_client/resources/connected_accounts.py">retrieve</a>(nanoid) -> <a href="./src/composio_client/types/connected_account_retrieve_response.py">ConnectedAccountRetrieveResponse</a></code>
- <code title="get /api/v3/connected_accounts">client.connected_accounts.<a href="./src/composio_client/resources/connected_accounts.py">list</a>(\*\*<a href="src/composio_client/types/connected_account_list_params.py">params</a>) -> <a href="./src/composio_client/types/connected_account_list_response.py">ConnectedAccountListResponse</a></code>
- <code title="delete /api/v3/connected_accounts/{nanoid}">client.connected_accounts.<a href="./src/composio_client/resources/connected_accounts.py">delete</a>(nanoid) -> <a href="./src/composio_client/types/connected_account_delete_response.py">ConnectedAccountDeleteResponse</a></code>
- <code title="post /api/v3/connected_accounts/{nanoid}/refresh">client.connected_accounts.<a href="./src/composio_client/resources/connected_accounts.py">refresh</a>(nanoid) -> <a href="./src/composio_client/types/connected_account_refresh_response.py">ConnectedAccountRefreshResponse</a></code>
- <code title="patch /api/v3/connected_accounts/{nanoId}/status">client.connected_accounts.<a href="./src/composio_client/resources/connected_accounts.py">update_status</a>(nano_id, \*\*<a href="src/composio_client/types/connected_account_update_status_params.py">params</a>) -> <a href="./src/composio_client/types/connected_account_update_status_response.py">ConnectedAccountUpdateStatusResponse</a></code>

# Trigger

Types:

```python
from composio_client.types import TriggerLogResponse
```

Methods:

- <code title="post /api/v3/internal/trigger/logs">client.trigger.<a href="./src/composio_client/resources/trigger.py">log</a>(\*\*<a href="src/composio_client/types/trigger_log_params.py">params</a>) -> <a href="./src/composio_client/types/trigger_log_response.py">TriggerLogResponse</a></code>

# ActionExecution

Types:

```python
from composio_client.types import (
    ActionExecutionLogResponse,
    ActionExecutionRetrieveFieldsResponse,
    ActionExecutionRetrieveLogResponse,
)
```

Methods:

- <code title="post /api/v3/internal/action_execution/logs">client.action_execution.<a href="./src/composio_client/resources/action_execution.py">log</a>(\*\*<a href="src/composio_client/types/action_execution_log_params.py">params</a>) -> <a href="./src/composio_client/types/action_execution_log_response.py">ActionExecutionLogResponse</a></code>
- <code title="get /api/v3/internal/action_execution/fields">client.action_execution.<a href="./src/composio_client/resources/action_execution.py">retrieve_fields</a>() -> <a href="./src/composio_client/types/action_execution_retrieve_fields_response.py">ActionExecutionRetrieveFieldsResponse</a></code>
- <code title="get /api/v3/internal/action_execution/log/{id}">client.action_execution.<a href="./src/composio_client/resources/action_execution.py">retrieve_log</a>(id) -> <a href="./src/composio_client/types/action_execution_retrieve_log_response.py">ActionExecutionRetrieveLogResponse</a></code>

# Org

## APIKey

Types:

```python
from composio_client.types.org import APIKeyRetrieveResponse, APIKeyRegenerateResponse
```

Methods:

- <code title="get /api/v3/org/api_key">client.org.api_key.<a href="./src/composio_client/resources/org/api_key.py">retrieve</a>() -> <a href="./src/composio_client/types/org/api_key_retrieve_response.py">APIKeyRetrieveResponse</a></code>
- <code title="post /api/v3/org/api_key/regenerate">client.org.api_key.<a href="./src/composio_client/resources/org/api_key.py">regenerate</a>() -> <a href="./src/composio_client/types/org/api_key_regenerate_response.py">APIKeyRegenerateResponse</a></code>

## Project

Types:

```python
from composio_client.types.org import (
    ProjectCreateResponse,
    ProjectRetrieveResponse,
    ProjectListResponse,
    ProjectDeleteResponse,
)
```

Methods:

- <code title="post /api/v3/org/project/new">client.org.project.<a href="./src/composio_client/resources/org/project/project.py">create</a>(\*\*<a href="src/composio_client/types/org/project_create_params.py">params</a>) -> <a href="./src/composio_client/types/org/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="get /api/v3/org/project/{projectId}">client.org.project.<a href="./src/composio_client/resources/org/project/project.py">retrieve</a>(project_id) -> <a href="./src/composio_client/types/org/project_retrieve_response.py">ProjectRetrieveResponse</a></code>
- <code title="get /api/v3/org/project/list">client.org.project.<a href="./src/composio_client/resources/org/project/project.py">list</a>() -> <a href="./src/composio_client/types/org/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /api/v3/org/project/delete/{projectId}">client.org.project.<a href="./src/composio_client/resources/org/project/project.py">delete</a>(project_id) -> <a href="./src/composio_client/types/org/project_delete_response.py">ProjectDeleteResponse</a></code>

### APIKeys

Types:

```python
from composio_client.types.org.project import (
    APIKeyCreateResponse,
    APIKeyListResponse,
    APIKeyDeleteResponse,
    APIKeyCreateAPIKeyResponse,
)
```

Methods:

- <code title="post /api/v3/org/project/{projectId}/api_keys/create">client.org.project.api_keys.<a href="./src/composio_client/resources/org/project/api_keys.py">create</a>(project_id, \*\*<a href="src/composio_client/types/org/project/api_key_create_params.py">params</a>) -> <a href="./src/composio_client/types/org/project/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="get /api/v3/org/project/{projectId}/api_keys/list">client.org.project.api_keys.<a href="./src/composio_client/resources/org/project/api_keys.py">list</a>(project_id) -> <a href="./src/composio_client/types/org/project/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /api/v3/org/project/{projectId}/api_keys/remove/{id}">client.org.project.api_keys.<a href="./src/composio_client/resources/org/project/api_keys.py">delete</a>(id, \*, project_id) -> <a href="./src/composio_client/types/org/project/api_key_delete_response.py">APIKeyDeleteResponse</a></code>
- <code title="post /api/v3/org/project/{projectId}/api_keys/create-api-key">client.org.project.api_keys.<a href="./src/composio_client/resources/org/project/api_keys.py">create_api_key</a>(project_id) -> <a href="./src/composio_client/types/org/project/api_key_create_api_key_response.py">APIKeyCreateAPIKeyResponse</a></code>

### Webhook

Types:

```python
from composio_client.types.org.project import (
    WebhookRetrieveResponse,
    WebhookUpdateResponse,
    WebhookDeleteResponse,
    WebhookRefreshResponse,
)
```

Methods:

- <code title="get /api/v3/org/project/webhook">client.org.project.webhook.<a href="./src/composio_client/resources/org/project/webhook.py">retrieve</a>(\*\*<a href="src/composio_client/types/org/project/webhook_retrieve_params.py">params</a>) -> <a href="./src/composio_client/types/org/project/webhook_retrieve_response.py">WebhookRetrieveResponse</a></code>
- <code title="post /api/v3/org/project/webhook/update">client.org.project.webhook.<a href="./src/composio_client/resources/org/project/webhook.py">update</a>(\*\*<a href="src/composio_client/types/org/project/webhook_update_params.py">params</a>) -> <a href="./src/composio_client/types/org/project/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="delete /api/v3/org/project/webhook">client.org.project.webhook.<a href="./src/composio_client/resources/org/project/webhook.py">delete</a>(\*\*<a href="src/composio_client/types/org/project/webhook_delete_params.py">params</a>) -> <a href="./src/composio_client/types/org/project/webhook_delete_response.py">WebhookDeleteResponse</a></code>
- <code title="post /api/v3/org/project/webhook/refresh">client.org.project.webhook.<a href="./src/composio_client/resources/org/project/webhook.py">refresh</a>() -> <a href="./src/composio_client/types/org/project/webhook_refresh_response.py">WebhookRefreshResponse</a></code>

### Trigger

Types:

```python
from composio_client.types.org.project import TriggerUpdateResponse, TriggerListResponse
```

Methods:

- <code title="patch /api/v3/org/project/trigger">client.org.project.trigger.<a href="./src/composio_client/resources/org/project/trigger.py">update</a>(\*\*<a href="src/composio_client/types/org/project/trigger_update_params.py">params</a>) -> <a href="./src/composio_client/types/org/project/trigger_update_response.py">TriggerUpdateResponse</a></code>
- <code title="get /api/v3/org/project/trigger">client.org.project.trigger.<a href="./src/composio_client/resources/org/project/trigger.py">list</a>() -> <a href="./src/composio_client/types/org/project/trigger_list_response.py">TriggerListResponse</a></code>

# TeamMembers

Types:

```python
from composio_client.types import (
    TeamMemberUpdateResponse,
    TeamMemberListResponse,
    TeamMemberInviteResponse,
    TeamMemberRemoveResponse,
)
```

Methods:

- <code title="put /api/v3/team-members/update/{id}">client.team_members.<a href="./src/composio_client/resources/team_members.py">update</a>(id, \*\*<a href="src/composio_client/types/team_member_update_params.py">params</a>) -> <a href="./src/composio_client/types/team_member_update_response.py">TeamMemberUpdateResponse</a></code>
- <code title="get /api/v3/team-members/list">client.team_members.<a href="./src/composio_client/resources/team_members.py">list</a>() -> <a href="./src/composio_client/types/team_member_list_response.py">TeamMemberListResponse</a></code>
- <code title="post /api/v3/team-members/invite">client.team_members.<a href="./src/composio_client/resources/team_members.py">invite</a>(\*\*<a href="src/composio_client/types/team_member_invite_params.py">params</a>) -> <a href="./src/composio_client/types/team_member_invite_response.py">TeamMemberInviteResponse</a></code>
- <code title="delete /api/v3/team-members/remove/{id}">client.team_members.<a href="./src/composio_client/resources/team_members.py">remove</a>(id) -> <a href="./src/composio_client/types/team_member_remove_response.py">TeamMemberRemoveResponse</a></code>

# Toolkits

Types:

```python
from composio_client.types import (
    ToolkitRetrieveResponse,
    ToolkitListResponse,
    ToolkitRetrieveCategoriesResponse,
)
```

Methods:

- <code title="get /api/v3/toolkits/{slug}">client.toolkits.<a href="./src/composio_client/resources/toolkits.py">retrieve</a>(slug) -> <a href="./src/composio_client/types/toolkit_retrieve_response.py">ToolkitRetrieveResponse</a></code>
- <code title="get /api/v3/toolkits">client.toolkits.<a href="./src/composio_client/resources/toolkits.py">list</a>(\*\*<a href="src/composio_client/types/toolkit_list_params.py">params</a>) -> <a href="./src/composio_client/types/toolkit_list_response.py">ToolkitListResponse</a></code>
- <code title="get /api/v3/toolkits/categories">client.toolkits.<a href="./src/composio_client/resources/toolkits.py">retrieve_categories</a>() -> <a href="./src/composio_client/types/toolkit_retrieve_categories_response.py">ToolkitRetrieveCategoriesResponse</a></code>

# Tools

Types:

```python
from composio_client.types import (
    ToolRetrieveResponse,
    ToolListResponse,
    ToolExecuteResponse,
    ToolGetInputResponse,
    ToolProxyResponse,
    ToolRetrieveEnumResponse,
)
```

Methods:

- <code title="get /api/v3/tools/{tool_slug}">client.tools.<a href="./src/composio_client/resources/tools.py">retrieve</a>(tool_slug) -> <a href="./src/composio_client/types/tool_retrieve_response.py">ToolRetrieveResponse</a></code>
- <code title="get /api/v3/tools">client.tools.<a href="./src/composio_client/resources/tools.py">list</a>(\*\*<a href="src/composio_client/types/tool_list_params.py">params</a>) -> <a href="./src/composio_client/types/tool_list_response.py">ToolListResponse</a></code>
- <code title="post /api/v3/tools/execute/{action}">client.tools.<a href="./src/composio_client/resources/tools.py">execute</a>(action, \*\*<a href="src/composio_client/types/tool_execute_params.py">params</a>) -> <a href="./src/composio_client/types/tool_execute_response.py">ToolExecuteResponse</a></code>
- <code title="post /api/v3/tools/execute/{actionName}/input">client.tools.<a href="./src/composio_client/resources/tools.py">get_input</a>(action_name, \*\*<a href="src/composio_client/types/tool_get_input_params.py">params</a>) -> <a href="./src/composio_client/types/tool_get_input_response.py">ToolGetInputResponse</a></code>
- <code title="post /api/v3/tools/execute/proxy">client.tools.<a href="./src/composio_client/resources/tools.py">proxy</a>(\*\*<a href="src/composio_client/types/tool_proxy_params.py">params</a>) -> <a href="./src/composio_client/types/tool_proxy_response.py">ToolProxyResponse</a></code>
- <code title="get /api/v3/tools/enum">client.tools.<a href="./src/composio_client/resources/tools.py">retrieve_enum</a>() -> str</code>

# TriggerInstances

Types:

```python
from composio_client.types import (
    TriggerInstanceListActiveResponse,
    TriggerInstanceRemoveUpsertResponse,
    TriggerInstanceUpdateStatusResponse,
    TriggerInstanceUpsertResponse,
)
```

Methods:

- <code title="get /api/v3/trigger_instances/active">client.trigger_instances.<a href="./src/composio_client/resources/trigger_instances/trigger_instances.py">list_active</a>(\*\*<a href="src/composio_client/types/trigger_instance_list_active_params.py">params</a>) -> <a href="./src/composio_client/types/trigger_instance_list_active_response.py">TriggerInstanceListActiveResponse</a></code>
- <code title="delete /api/v3/trigger_instances/{slug}/upsert">client.trigger_instances.<a href="./src/composio_client/resources/trigger_instances/trigger_instances.py">remove_upsert</a>(slug) -> <a href="./src/composio_client/types/trigger_instance_remove_upsert_response.py">TriggerInstanceRemoveUpsertResponse</a></code>
- <code title="patch /api/v3/trigger_instances/{slug}/status/{status}">client.trigger_instances.<a href="./src/composio_client/resources/trigger_instances/trigger_instances.py">update_status</a>(status, \*, slug) -> <a href="./src/composio_client/types/trigger_instance_update_status_response.py">TriggerInstanceUpdateStatusResponse</a></code>
- <code title="post /api/v3/trigger_instances/{slug}/upsert">client.trigger_instances.<a href="./src/composio_client/resources/trigger_instances/trigger_instances.py">upsert</a>(slug, \*\*<a href="src/composio_client/types/trigger_instance_upsert_params.py">params</a>) -> <a href="./src/composio_client/types/trigger_instance_upsert_response.py">TriggerInstanceUpsertResponse</a></code>

## Handle

Types:

```python
from composio_client.types.trigger_instances import HandleRetrieveResponse, HandleExecuteResponse
```

Methods:

- <code title="get /api/v3/trigger_instances/{slug}/{projectId}/handle">client.trigger_instances.handle.<a href="./src/composio_client/resources/trigger_instances/handle.py">retrieve</a>(project_id, \*, slug) -> str</code>
- <code title="post /api/v3/trigger_instances/{slug}/{projectId}/handle">client.trigger_instances.handle.<a href="./src/composio_client/resources/trigger_instances/handle.py">execute</a>(project_id, \*, slug) -> str</code>

# TriggersTypes

Types:

```python
from composio_client.types import (
    TriggersTypeRetrieveResponse,
    TriggersTypeListResponse,
    TriggersTypeRetrieveEnumResponse,
)
```

Methods:

- <code title="get /api/v3/triggers_types/{slug}">client.triggers_types.<a href="./src/composio_client/resources/triggers_types.py">retrieve</a>(slug) -> <a href="./src/composio_client/types/triggers_type_retrieve_response.py">TriggersTypeRetrieveResponse</a></code>
- <code title="get /api/v3/triggers_types">client.triggers_types.<a href="./src/composio_client/resources/triggers_types.py">list</a>(\*\*<a href="src/composio_client/types/triggers_type_list_params.py">params</a>) -> <a href="./src/composio_client/types/triggers_type_list_response.py">TriggersTypeListResponse</a></code>
- <code title="get /api/v3/triggers_types/list/enum">client.triggers_types.<a href="./src/composio_client/resources/triggers_types.py">retrieve_enum</a>() -> str</code>

# Mcp

Types:

```python
from composio_client.types import (
    McpCreateResponse,
    McpRetrieveResponse,
    McpUpdateResponse,
    McpListResponse,
    McpDeleteResponse,
    McpRetrieveAppResponse,
    McpValidateResponse,
)
```

Methods:

- <code title="post /api/v3/mcp/create">client.mcp.<a href="./src/composio_client/resources/mcp/mcp.py">create</a>(\*\*<a href="src/composio_client/types/mcp_create_params.py">params</a>) -> <a href="./src/composio_client/types/mcp_create_response.py">McpCreateResponse</a></code>
- <code title="get /api/v3/mcp/{id}">client.mcp.<a href="./src/composio_client/resources/mcp/mcp.py">retrieve</a>(id) -> <a href="./src/composio_client/types/mcp_retrieve_response.py">McpRetrieveResponse</a></code>
- <code title="patch /api/v3/mcp/{id}">client.mcp.<a href="./src/composio_client/resources/mcp/mcp.py">update</a>(id, \*\*<a href="src/composio_client/types/mcp_update_params.py">params</a>) -> <a href="./src/composio_client/types/mcp_update_response.py">McpUpdateResponse</a></code>
- <code title="get /api/v3/mcp/list">client.mcp.<a href="./src/composio_client/resources/mcp/mcp.py">list</a>(\*\*<a href="src/composio_client/types/mcp_list_params.py">params</a>) -> <a href="./src/composio_client/types/mcp_list_response.py">McpListResponse</a></code>
- <code title="delete /api/v3/mcp/{id}">client.mcp.<a href="./src/composio_client/resources/mcp/mcp.py">delete</a>(id) -> <a href="./src/composio_client/types/mcp_delete_response.py">McpDeleteResponse</a></code>
- <code title="get /api/v3/mcp/app/{appKey}">client.mcp.<a href="./src/composio_client/resources/mcp/mcp.py">retrieve_app</a>(app_key) -> <a href="./src/composio_client/types/mcp_retrieve_app_response.py">McpRetrieveAppResponse</a></code>
- <code title="get /api/v3/mcp/validate/{uuid}">client.mcp.<a href="./src/composio_client/resources/mcp/mcp.py">validate</a>(uuid) -> <a href="./src/composio_client/types/mcp_validate_response.py">McpValidateResponse</a></code>

## Command

Types:

```python
from composio_client.types.mcp import CommandGenerateResponse
```

Methods:

- <code title="post /api/v3/mcp/command/generate">client.mcp.command.<a href="./src/composio_client/resources/mcp/command.py">generate</a>(\*\*<a href="src/composio_client/types/mcp/command_generate_params.py">params</a>) -> <a href="./src/composio_client/types/mcp/command_generate_response.py">CommandGenerateResponse</a></code>

# Files

Types:

```python
from composio_client.types import FileListResponse, FileCreatePresignedURLResponse
```

Methods:

- <code title="get /api/v3/files/list">client.files.<a href="./src/composio_client/resources/files.py">list</a>(\*\*<a href="src/composio_client/types/file_list_params.py">params</a>) -> <a href="./src/composio_client/types/file_list_response.py">FileListResponse</a></code>
- <code title="post /api/v3/files/upload/{fileType}">client.files.<a href="./src/composio_client/resources/files.py">create_presigned_url</a>(file_type, \*\*<a href="src/composio_client/types/file_create_presigned_url_params.py">params</a>) -> <a href="./src/composio_client/types/file_create_presigned_url_response.py">FileCreatePresignedURLResponse</a></code>

# Migration

Types:

```python
from composio_client.types import MigrationRetrieveNanoidResponse
```

Methods:

- <code title="get /api/v3/migration/get-nanoid">client.migration.<a href="./src/composio_client/resources/migration.py">retrieve_nanoid</a>(\*\*<a href="src/composio_client/types/migration_retrieve_nanoid_params.py">params</a>) -> <a href="./src/composio_client/types/migration_retrieve_nanoid_response.py">MigrationRetrieveNanoidResponse</a></code>
