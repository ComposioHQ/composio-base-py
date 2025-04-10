# Auth

Types:

```python
from composio_sdk.types import AuthOneTapResponse, AuthRetrieveCallbackResponse
```

Methods:

- <code title="get /api/v3/auth/{provider_name}/login">client.auth.<a href="./src/composio_sdk/resources/auth/auth.py">login</a>(provider_name, \*\*<a href="src/composio_sdk/types/auth_login_params.py">params</a>) -> None</code>
- <code title="post /api/v3/auth/{provider_name}/one-tap">client.auth.<a href="./src/composio_sdk/resources/auth/auth.py">one_tap</a>(provider_name, \*\*<a href="src/composio_sdk/types/auth_one_tap_params.py">params</a>) -> <a href="./src/composio_sdk/types/auth_one_tap_response.py">AuthOneTapResponse</a></code>
- <code title="get /api/v3/auth/{provider_name}/callback">client.auth.<a href="./src/composio_sdk/resources/auth/auth.py">retrieve_callback</a>(provider_name, \*\*<a href="src/composio_sdk/types/auth_retrieve_callback_params.py">params</a>) -> <a href="./src/composio_sdk/types/auth_retrieve_callback_response.py">AuthRetrieveCallbackResponse</a></code>

## MagicLink

Types:

```python
from composio_sdk.types.auth import MagicLinkSendResponse, MagicLinkVerifyResponse
```

Methods:

- <code title="post /api/v3/auth/magic_link/send">client.auth.magic_link.<a href="./src/composio_sdk/resources/auth/magic_link.py">send</a>(\*\*<a href="src/composio_sdk/types/auth/magic_link_send_params.py">params</a>) -> <a href="./src/composio_sdk/types/auth/magic_link_send_response.py">MagicLinkSendResponse</a></code>
- <code title="post /api/v3/auth/magic_link/verify">client.auth.magic_link.<a href="./src/composio_sdk/resources/auth/magic_link.py">verify</a>(\*\*<a href="src/composio_sdk/types/auth/magic_link_verify_params.py">params</a>) -> <a href="./src/composio_sdk/types/auth/magic_link_verify_response.py">MagicLinkVerifyResponse</a></code>

## Session

Types:

```python
from composio_sdk.types.auth import SessionLogoutResponse, SessionRetrieveInfoResponse
```

Methods:

- <code title="post /api/v3/auth/session/logout">client.auth.session.<a href="./src/composio_sdk/resources/auth/session.py">logout</a>() -> <a href="./src/composio_sdk/types/auth/session_logout_response.py">SessionLogoutResponse</a></code>
- <code title="get /api/v3/auth/session/info">client.auth.session.<a href="./src/composio_sdk/resources/auth/session.py">retrieve_info</a>() -> <a href="./src/composio_sdk/types/auth/session_retrieve_info_response.py">SessionRetrieveInfoResponse</a></code>

# Admin

Types:

```python
from composio_sdk.types import AdminIdentifyResponse
```

Methods:

- <code title="post /api/v3/admin/identify">client.admin.<a href="./src/composio_sdk/resources/admin.py">identify</a>(\*\*<a href="src/composio_sdk/types/admin_identify_params.py">params</a>) -> <a href="./src/composio_sdk/types/admin_identify_response.py">AdminIdentifyResponse</a></code>

# AuthConfigs

Types:

```python
from composio_sdk.types import (
    AuthConfigCreateResponse,
    AuthConfigRetrieveResponse,
    AuthConfigUpdateResponse,
    AuthConfigListResponse,
    AuthConfigDeleteResponse,
    AuthConfigUpdateStatusResponse,
)
```

Methods:

- <code title="post /api/v3/auth_configs">client.auth_configs.<a href="./src/composio_sdk/resources/auth_configs.py">create</a>(\*\*<a href="src/composio_sdk/types/auth_config_create_params.py">params</a>) -> <a href="./src/composio_sdk/types/auth_config_create_response.py">AuthConfigCreateResponse</a></code>
- <code title="get /api/v3/auth_configs/{nanoid}">client.auth_configs.<a href="./src/composio_sdk/resources/auth_configs.py">retrieve</a>(nanoid) -> <a href="./src/composio_sdk/types/auth_config_retrieve_response.py">AuthConfigRetrieveResponse</a></code>
- <code title="patch /api/v3/auth_configs/{nanoid}">client.auth_configs.<a href="./src/composio_sdk/resources/auth_configs.py">update</a>(nanoid, \*\*<a href="src/composio_sdk/types/auth_config_update_params.py">params</a>) -> <a href="./src/composio_sdk/types/auth_config_update_response.py">AuthConfigUpdateResponse</a></code>
- <code title="get /api/v3/auth_configs">client.auth_configs.<a href="./src/composio_sdk/resources/auth_configs.py">list</a>(\*\*<a href="src/composio_sdk/types/auth_config_list_params.py">params</a>) -> <a href="./src/composio_sdk/types/auth_config_list_response.py">AuthConfigListResponse</a></code>
- <code title="delete /api/v3/auth_configs/{nanoid}">client.auth_configs.<a href="./src/composio_sdk/resources/auth_configs.py">delete</a>(nanoid) -> <a href="./src/composio_sdk/types/auth_config_delete_response.py">AuthConfigDeleteResponse</a></code>
- <code title="patch /api/v3/auth_configs/{nanoid}/{status}">client.auth_configs.<a href="./src/composio_sdk/resources/auth_configs.py">update_status</a>(status, \*, nanoid) -> <a href="./src/composio_sdk/types/auth_config_update_status_response.py">AuthConfigUpdateStatusResponse</a></code>

# ConnectedAccounts

Types:

```python
from composio_sdk.types import (
    ConnectedAccountCreateResponse,
    ConnectedAccountRetrieveResponse,
    ConnectedAccountListResponse,
    ConnectedAccountDeleteResponse,
    ConnectedAccountRefreshResponse,
    ConnectedAccountUpdateStatusResponse,
)
```

Methods:

- <code title="post /api/v3/connected_accounts">client.connected_accounts.<a href="./src/composio_sdk/resources/connected_accounts.py">create</a>(\*\*<a href="src/composio_sdk/types/connected_account_create_params.py">params</a>) -> <a href="./src/composio_sdk/types/connected_account_create_response.py">ConnectedAccountCreateResponse</a></code>
- <code title="get /api/v3/connected_accounts/{nanoid}">client.connected_accounts.<a href="./src/composio_sdk/resources/connected_accounts.py">retrieve</a>(nanoid) -> <a href="./src/composio_sdk/types/connected_account_retrieve_response.py">ConnectedAccountRetrieveResponse</a></code>
- <code title="get /api/v3/connected_accounts">client.connected_accounts.<a href="./src/composio_sdk/resources/connected_accounts.py">list</a>(\*\*<a href="src/composio_sdk/types/connected_account_list_params.py">params</a>) -> <a href="./src/composio_sdk/types/connected_account_list_response.py">ConnectedAccountListResponse</a></code>
- <code title="delete /api/v3/connected_accounts/{nanoid}">client.connected_accounts.<a href="./src/composio_sdk/resources/connected_accounts.py">delete</a>(nanoid) -> <a href="./src/composio_sdk/types/connected_account_delete_response.py">ConnectedAccountDeleteResponse</a></code>
- <code title="post /api/v3/connected_accounts/{nanoid}/refresh">client.connected_accounts.<a href="./src/composio_sdk/resources/connected_accounts.py">refresh</a>(nanoid) -> <a href="./src/composio_sdk/types/connected_account_refresh_response.py">ConnectedAccountRefreshResponse</a></code>
- <code title="patch /api/v3/connected_accounts/{nanoId}/status">client.connected_accounts.<a href="./src/composio_sdk/resources/connected_accounts.py">update_status</a>(nano_id, \*\*<a href="src/composio_sdk/types/connected_account_update_status_params.py">params</a>) -> <a href="./src/composio_sdk/types/connected_account_update_status_response.py">ConnectedAccountUpdateStatusResponse</a></code>

# Trigger

Types:

```python
from composio_sdk.types import TriggerLogResponse
```

Methods:

- <code title="post /api/v3/internal/trigger/logs">client.trigger.<a href="./src/composio_sdk/resources/trigger.py">log</a>(\*\*<a href="src/composio_sdk/types/trigger_log_params.py">params</a>) -> <a href="./src/composio_sdk/types/trigger_log_response.py">TriggerLogResponse</a></code>

# ActionExecution

Types:

```python
from composio_sdk.types import (
    ActionExecutionLogResponse,
    ActionExecutionRetrieveFieldsResponse,
    ActionExecutionRetrieveLogResponse,
)
```

Methods:

- <code title="post /api/v3/internal/action_execution/logs">client.action_execution.<a href="./src/composio_sdk/resources/action_execution.py">log</a>(\*\*<a href="src/composio_sdk/types/action_execution_log_params.py">params</a>) -> <a href="./src/composio_sdk/types/action_execution_log_response.py">ActionExecutionLogResponse</a></code>
- <code title="get /api/v3/internal/action_execution/fields">client.action_execution.<a href="./src/composio_sdk/resources/action_execution.py">retrieve_fields</a>() -> <a href="./src/composio_sdk/types/action_execution_retrieve_fields_response.py">ActionExecutionRetrieveFieldsResponse</a></code>
- <code title="get /api/v3/internal/action_execution/log/{id}">client.action_execution.<a href="./src/composio_sdk/resources/action_execution.py">retrieve_log</a>(id) -> <a href="./src/composio_sdk/types/action_execution_retrieve_log_response.py">ActionExecutionRetrieveLogResponse</a></code>

# Org

## APIKey

Types:

```python
from composio_sdk.types.org import APIKeyRetrieveResponse, APIKeyRegenerateResponse
```

Methods:

- <code title="get /api/v3/org/api_key">client.org.api_key.<a href="./src/composio_sdk/resources/org/api_key.py">retrieve</a>() -> <a href="./src/composio_sdk/types/org/api_key_retrieve_response.py">APIKeyRetrieveResponse</a></code>
- <code title="post /api/v3/org/api_key/regenerate">client.org.api_key.<a href="./src/composio_sdk/resources/org/api_key.py">regenerate</a>() -> <a href="./src/composio_sdk/types/org/api_key_regenerate_response.py">APIKeyRegenerateResponse</a></code>

## Project

Types:

```python
from composio_sdk.types.org import (
    ProjectCreateResponse,
    ProjectRetrieveResponse,
    ProjectListResponse,
    ProjectDeleteResponse,
)
```

Methods:

- <code title="post /api/v3/org/project/new">client.org.project.<a href="./src/composio_sdk/resources/org/project/project.py">create</a>(\*\*<a href="src/composio_sdk/types/org/project_create_params.py">params</a>) -> <a href="./src/composio_sdk/types/org/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="get /api/v3/org/project/{projectId}">client.org.project.<a href="./src/composio_sdk/resources/org/project/project.py">retrieve</a>(project_id) -> <a href="./src/composio_sdk/types/org/project_retrieve_response.py">ProjectRetrieveResponse</a></code>
- <code title="get /api/v3/org/project/list">client.org.project.<a href="./src/composio_sdk/resources/org/project/project.py">list</a>() -> <a href="./src/composio_sdk/types/org/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /api/v3/org/project/delete/{projectId}">client.org.project.<a href="./src/composio_sdk/resources/org/project/project.py">delete</a>(project_id) -> <a href="./src/composio_sdk/types/org/project_delete_response.py">ProjectDeleteResponse</a></code>

### APIKeys

Types:

```python
from composio_sdk.types.org.project import (
    APIKeyCreateResponse,
    APIKeyListResponse,
    APIKeyDeleteResponse,
    APIKeyCreateAPIKeyResponse,
)
```

Methods:

- <code title="post /api/v3/org/project/{projectId}/api_keys/create">client.org.project.api_keys.<a href="./src/composio_sdk/resources/org/project/api_keys.py">create</a>(project_id, \*\*<a href="src/composio_sdk/types/org/project/api_key_create_params.py">params</a>) -> <a href="./src/composio_sdk/types/org/project/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="get /api/v3/org/project/{projectId}/api_keys/list">client.org.project.api_keys.<a href="./src/composio_sdk/resources/org/project/api_keys.py">list</a>(project_id) -> <a href="./src/composio_sdk/types/org/project/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /api/v3/org/project/{projectId}/api_keys/remove/{id}">client.org.project.api_keys.<a href="./src/composio_sdk/resources/org/project/api_keys.py">delete</a>(id, \*, project_id) -> <a href="./src/composio_sdk/types/org/project/api_key_delete_response.py">APIKeyDeleteResponse</a></code>
- <code title="post /api/v3/org/project/{projectId}/api_keys/create-api-key">client.org.project.api_keys.<a href="./src/composio_sdk/resources/org/project/api_keys.py">create_api_key</a>(project_id) -> <a href="./src/composio_sdk/types/org/project/api_key_create_api_key_response.py">APIKeyCreateAPIKeyResponse</a></code>

### Webhook

Types:

```python
from composio_sdk.types.org.project import (
    WebhookRetrieveResponse,
    WebhookUpdateResponse,
    WebhookDeleteResponse,
    WebhookRefreshResponse,
)
```

Methods:

- <code title="get /api/v3/org/project/webhook">client.org.project.webhook.<a href="./src/composio_sdk/resources/org/project/webhook.py">retrieve</a>(\*\*<a href="src/composio_sdk/types/org/project/webhook_retrieve_params.py">params</a>) -> <a href="./src/composio_sdk/types/org/project/webhook_retrieve_response.py">WebhookRetrieveResponse</a></code>
- <code title="post /api/v3/org/project/webhook/update">client.org.project.webhook.<a href="./src/composio_sdk/resources/org/project/webhook.py">update</a>(\*\*<a href="src/composio_sdk/types/org/project/webhook_update_params.py">params</a>) -> <a href="./src/composio_sdk/types/org/project/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="delete /api/v3/org/project/webhook">client.org.project.webhook.<a href="./src/composio_sdk/resources/org/project/webhook.py">delete</a>(\*\*<a href="src/composio_sdk/types/org/project/webhook_delete_params.py">params</a>) -> <a href="./src/composio_sdk/types/org/project/webhook_delete_response.py">WebhookDeleteResponse</a></code>
- <code title="post /api/v3/org/project/webhook/refresh">client.org.project.webhook.<a href="./src/composio_sdk/resources/org/project/webhook.py">refresh</a>() -> <a href="./src/composio_sdk/types/org/project/webhook_refresh_response.py">WebhookRefreshResponse</a></code>

### Trigger

Types:

```python
from composio_sdk.types.org.project import TriggerUpdateResponse, TriggerListResponse
```

Methods:

- <code title="patch /api/v3/org/project/trigger">client.org.project.trigger.<a href="./src/composio_sdk/resources/org/project/trigger.py">update</a>(\*\*<a href="src/composio_sdk/types/org/project/trigger_update_params.py">params</a>) -> <a href="./src/composio_sdk/types/org/project/trigger_update_response.py">TriggerUpdateResponse</a></code>
- <code title="get /api/v3/org/project/trigger">client.org.project.trigger.<a href="./src/composio_sdk/resources/org/project/trigger.py">list</a>() -> <a href="./src/composio_sdk/types/org/project/trigger_list_response.py">TriggerListResponse</a></code>

# TeamMembers

Types:

```python
from composio_sdk.types import (
    TeamMemberUpdateResponse,
    TeamMemberListResponse,
    TeamMemberInviteResponse,
    TeamMemberRemoveResponse,
)
```

Methods:

- <code title="put /api/v3/team-members/update/{id}">client.team_members.<a href="./src/composio_sdk/resources/team_members.py">update</a>(id, \*\*<a href="src/composio_sdk/types/team_member_update_params.py">params</a>) -> <a href="./src/composio_sdk/types/team_member_update_response.py">TeamMemberUpdateResponse</a></code>
- <code title="get /api/v3/team-members/list">client.team_members.<a href="./src/composio_sdk/resources/team_members.py">list</a>() -> <a href="./src/composio_sdk/types/team_member_list_response.py">TeamMemberListResponse</a></code>
- <code title="post /api/v3/team-members/invite">client.team_members.<a href="./src/composio_sdk/resources/team_members.py">invite</a>(\*\*<a href="src/composio_sdk/types/team_member_invite_params.py">params</a>) -> <a href="./src/composio_sdk/types/team_member_invite_response.py">TeamMemberInviteResponse</a></code>
- <code title="delete /api/v3/team-members/remove/{id}">client.team_members.<a href="./src/composio_sdk/resources/team_members.py">remove</a>(id) -> <a href="./src/composio_sdk/types/team_member_remove_response.py">TeamMemberRemoveResponse</a></code>

# Toolkits

Types:

```python
from composio_sdk.types import (
    ToolkitRetrieveResponse,
    ToolkitListResponse,
    ToolkitRetrieveCategoriesResponse,
)
```

Methods:

- <code title="get /api/v3/toolkits/{slug}">client.toolkits.<a href="./src/composio_sdk/resources/toolkits.py">retrieve</a>(slug) -> <a href="./src/composio_sdk/types/toolkit_retrieve_response.py">ToolkitRetrieveResponse</a></code>
- <code title="get /api/v3/toolkits">client.toolkits.<a href="./src/composio_sdk/resources/toolkits.py">list</a>(\*\*<a href="src/composio_sdk/types/toolkit_list_params.py">params</a>) -> <a href="./src/composio_sdk/types/toolkit_list_response.py">ToolkitListResponse</a></code>
- <code title="get /api/v3/toolkits/categories">client.toolkits.<a href="./src/composio_sdk/resources/toolkits.py">retrieve_categories</a>() -> <a href="./src/composio_sdk/types/toolkit_retrieve_categories_response.py">ToolkitRetrieveCategoriesResponse</a></code>

# Tools

Types:

```python
from composio_sdk.types import ToolRetrieveResponse, ToolListResponse, ToolRetrieveEnumResponse
```

Methods:

- <code title="get /api/v3/tools/{tool_slug}">client.tools.<a href="./src/composio_sdk/resources/tools/tools.py">retrieve</a>(tool_slug) -> <a href="./src/composio_sdk/types/tool_retrieve_response.py">ToolRetrieveResponse</a></code>
- <code title="get /api/v3/tools">client.tools.<a href="./src/composio_sdk/resources/tools/tools.py">list</a>(\*\*<a href="src/composio_sdk/types/tool_list_params.py">params</a>) -> <a href="./src/composio_sdk/types/tool_list_response.py">ToolListResponse</a></code>
- <code title="get /api/v3/tools/enum">client.tools.<a href="./src/composio_sdk/resources/tools/tools.py">retrieve_enum</a>() -> str</code>

## Execute

Types:

```python
from composio_sdk.types.tools import (
    ExecuteExecuteResponse,
    ExecuteInputResponse,
    ExecuteProxyResponse,
)
```

Methods:

- <code title="post /api/v3/tools/execute/{action}">client.tools.execute.<a href="./src/composio_sdk/resources/tools/execute.py">execute</a>(action, \*\*<a href="src/composio_sdk/types/tools/execute_execute_params.py">params</a>) -> <a href="./src/composio_sdk/types/tools/execute_execute_response.py">ExecuteExecuteResponse</a></code>
- <code title="post /api/v3/tools/execute/{actionName}/input">client.tools.execute.<a href="./src/composio_sdk/resources/tools/execute.py">input</a>(action_name, \*\*<a href="src/composio_sdk/types/tools/execute_input_params.py">params</a>) -> <a href="./src/composio_sdk/types/tools/execute_input_response.py">ExecuteInputResponse</a></code>
- <code title="post /api/v3/tools/execute/proxy">client.tools.execute.<a href="./src/composio_sdk/resources/tools/execute.py">proxy</a>(\*\*<a href="src/composio_sdk/types/tools/execute_proxy_params.py">params</a>) -> <a href="./src/composio_sdk/types/tools/execute_proxy_response.py">ExecuteProxyResponse</a></code>

# TriggerInstances

Types:

```python
from composio_sdk.types import (
    TriggerInstanceListActiveResponse,
    TriggerInstanceRemoveUpsertResponse,
    TriggerInstanceUpdateStatusResponse,
    TriggerInstanceUpsertResponse,
)
```

Methods:

- <code title="get /api/v3/trigger_instances/active">client.trigger_instances.<a href="./src/composio_sdk/resources/trigger_instances/trigger_instances.py">list_active</a>(\*\*<a href="src/composio_sdk/types/trigger_instance_list_active_params.py">params</a>) -> <a href="./src/composio_sdk/types/trigger_instance_list_active_response.py">TriggerInstanceListActiveResponse</a></code>
- <code title="delete /api/v3/trigger_instances/{slug}/upsert">client.trigger_instances.<a href="./src/composio_sdk/resources/trigger_instances/trigger_instances.py">remove_upsert</a>(slug) -> <a href="./src/composio_sdk/types/trigger_instance_remove_upsert_response.py">TriggerInstanceRemoveUpsertResponse</a></code>
- <code title="patch /api/v3/trigger_instances/{slug}/status/{status}">client.trigger_instances.<a href="./src/composio_sdk/resources/trigger_instances/trigger_instances.py">update_status</a>(status, \*, slug) -> <a href="./src/composio_sdk/types/trigger_instance_update_status_response.py">TriggerInstanceUpdateStatusResponse</a></code>
- <code title="post /api/v3/trigger_instances/{slug}/upsert">client.trigger_instances.<a href="./src/composio_sdk/resources/trigger_instances/trigger_instances.py">upsert</a>(slug, \*\*<a href="src/composio_sdk/types/trigger_instance_upsert_params.py">params</a>) -> <a href="./src/composio_sdk/types/trigger_instance_upsert_response.py">TriggerInstanceUpsertResponse</a></code>

## Handle

Types:

```python
from composio_sdk.types.trigger_instances import HandleRetrieveResponse, HandleExecuteResponse
```

Methods:

- <code title="get /api/v3/trigger_instances/{slug}/{projectId}/handle">client.trigger_instances.handle.<a href="./src/composio_sdk/resources/trigger_instances/handle.py">retrieve</a>(project_id, \*, slug) -> str</code>
- <code title="post /api/v3/trigger_instances/{slug}/{projectId}/handle">client.trigger_instances.handle.<a href="./src/composio_sdk/resources/trigger_instances/handle.py">execute</a>(project_id, \*, slug) -> str</code>

# TriggersTypes

Types:

```python
from composio_sdk.types import (
    TriggersTypeRetrieveResponse,
    TriggersTypeListResponse,
    TriggersTypeRetrieveEnumResponse,
)
```

Methods:

- <code title="get /api/v3/triggers_types/{slug}">client.triggers_types.<a href="./src/composio_sdk/resources/triggers_types.py">retrieve</a>(slug) -> <a href="./src/composio_sdk/types/triggers_type_retrieve_response.py">TriggersTypeRetrieveResponse</a></code>
- <code title="get /api/v3/triggers_types">client.triggers_types.<a href="./src/composio_sdk/resources/triggers_types.py">list</a>(\*\*<a href="src/composio_sdk/types/triggers_type_list_params.py">params</a>) -> <a href="./src/composio_sdk/types/triggers_type_list_response.py">TriggersTypeListResponse</a></code>
- <code title="get /api/v3/triggers_types/list/enum">client.triggers_types.<a href="./src/composio_sdk/resources/triggers_types.py">retrieve_enum</a>() -> str</code>

# Payments

Types:

```python
from composio_sdk.types import PaymentCreateSessionResponse, PaymentManageSubscriptionResponse
```

Methods:

- <code title="post /api/v3/payments/session">client.payments.<a href="./src/composio_sdk/resources/payments.py">create_session</a>(\*\*<a href="src/composio_sdk/types/payment_create_session_params.py">params</a>) -> <a href="./src/composio_sdk/types/payment_create_session_response.py">PaymentCreateSessionResponse</a></code>
- <code title="post /api/v3/payments/manage-subscription">client.payments.<a href="./src/composio_sdk/resources/payments.py">manage_subscription</a>() -> <a href="./src/composio_sdk/types/payment_manage_subscription_response.py">PaymentManageSubscriptionResponse</a></code>
