# Composio SDK TypeScript MCP Server

It is generated with [Stainless](https://www.stainless.com/).

## Installation

### Building

Because it's not published yet, clone the repo and build it:

```sh
git clone git@github.com:composiohq/composio-base-ts.git
cd composio-base-ts
yarn && ./scripts/build-all
```

### Running

```sh
# set env vars as needed
export COMPOSIO_API_KEY="My API Key"
npx ./packages/mcp-server
```

> [!NOTE]
> Once this package is [published to npm](https://app.stainless.com/docs/guides/publish), this will become: `npx -y composio-sdk-mcp`

### Via MCP Client

[Build the project](#building) as mentioned above.

There is a partial list of existing clients at [modelcontextprotocol.io](https://modelcontextprotocol.io/clients). If you already
have a client, consult their documentation to install the MCP server.

For clients with a configuration JSON, it might look something like this:

```json
{
  "mcpServers": {
    "composio_sdk_api": {
      "command": "npx",
      "args": ["-y", "/path/to/local/composio-base-ts/packages/mcp-server"],
      "env": {
        "COMPOSIO_API_KEY": "My API Key"
      }
    }
  }
}
```

## Filtering tools

You can run the package on the command line to discover and filter the set of tools that are exposed by the
MCP Server. This can be helpful for large APIs where including all endpoints at once is too much for your AI's
context window.

You can filter by multiple aspects:

- `--tool` includes a specific tool by name
- `--resource` includes all tools under a specific resource, and can have wildcards, e.g. `my.resource*`
- `--operation` includes just read (get/list) or just write operations

See more information with `--help`.

All of these command-line options can be repeated, combined together, and have corresponding exclusion versions (e.g. `--no-tool`).

Use `--list` to see the list of available tools, or see below.

## Importing the tools and server individually

```js
// Import the server, generated endpoints, or the init function
import { server, endpoints, init } from "composio-sdk-mcp/server";

// import a specific tool
import createAuthConfigs from "composio-sdk-mcp/tools/auth-configs/create-auth-configs";

// initialize the server and all endpoints
init({ server, endpoints });

// manually start server
const transport = new StdioServerTransport();
await server.connect(transport);

// or initialize your own server with specific tools
const myServer = new McpServer(...);

// define your own endpoint
const myCustomEndpoint = {
  tool: {
    name: 'my_custom_tool',
    description: 'My custom tool',
    inputSchema: zodToJsonSchema(z.object({ a_property: z.string() })),
  },
  handler: async (client: client, args: any) => {
    return { myResponse: 'Hello world!' };
  })
};

// initialize the server with your custom endpoints
init({ server: myServer, endpoints: [createAuthConfigs, myCustomEndpoint] });
```

## Available Tools

The following tools are available in this MCP server.

### Resource `auth_configs`:

- `create_auth_configs` (`write`):
- `retrieve_auth_configs` (`read`):
- `update_auth_configs` (`write`):
- `list_auth_configs` (`read`):
- `delete_auth_configs` (`write`):
- `update_status_auth_configs` (`write`):

### Resource `connected_accounts`:

- `create_connected_accounts` (`write`):
- `retrieve_connected_accounts` (`read`):
- `list_connected_accounts` (`read`):
- `delete_connected_accounts` (`write`):
- `refresh_connected_accounts` (`write`):
- `update_status_connected_accounts` (`write`):

### Resource `trigger`:

- `log_trigger` (`write`):

### Resource `action_execution`:

- `log_action_execution` (`write`):
- `retrieve_fields_action_execution` (`read`):
- `retrieve_log_action_execution` (`read`):

### Resource `org`:

- `regenerate_api_key_org` (`write`):
- `retrieve_api_key_org` (`read`):

### Resource `org.project`:

- `create_org_project` (`write`):
- `retrieve_org_project` (`read`):
- `list_org_project` (`read`):
- `delete_org_project` (`write`):

### Resource `org.project.api_keys`:

- `create_project_org_api_keys` (`write`):
- `list_project_org_api_keys` (`read`):
- `delete_project_org_api_keys` (`write`):
- `create_api_key_project_org_api_keys` (`write`):

### Resource `org.project.webhook`:

- `retrieve_project_org_webhook` (`read`): Get the webhook URL for a project
- `update_project_org_webhook` (`write`):
- `delete_project_org_webhook` (`write`):
- `refresh_project_org_webhook` (`write`):

### Resource `org.project.trigger`:

- `update_project_org_trigger` (`write`):
- `list_project_org_trigger` (`read`):

### Resource `team_members`:

- `update_team_members` (`write`):
- `list_team_members` (`read`):
- `invite_team_members` (`write`):
- `remove_team_members` (`write`):

### Resource `toolkits`:

- `retrieve_toolkits` (`read`):
- `list_toolkits` (`read`):
- `retrieve_categories_toolkits` (`read`):

### Resource `tools`:

- `retrieve_tools` (`read`):
- `list_tools` (`read`):
- `retrieve_enum_tools` (`read`):
- `run_tools` (`write`):

### Resource `tools.execute`:

- `get_input_tools_execute` (`write`):
- `proxy_tools_execute` (`write`):

### Resource `trigger_instances`:

- `list_active_trigger_instances` (`read`):
- `remove_upsert_trigger_instances` (`write`):
- `update_status_trigger_instances` (`write`):
- `upsert_trigger_instances` (`write`):

### Resource `trigger_instances.handle`:

- `retrieve_trigger_instances_handle` (`read`):
- `execute_trigger_instances_handle` (`write`):

### Resource `triggers_types`:

- `retrieve_triggers_types` (`read`):
- `list_triggers_types` (`read`):
- `retrieve_enum_triggers_types` (`read`):

### Resource `payments`:

- `create_session_payments` (`write`):
- `manage_subscription_payments` (`write`):
