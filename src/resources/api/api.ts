// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import * as AdminAPI from './admin';
import { Admin, AdminIdentifyParams, AdminIdentifyResponse } from './admin';
import * as AuthConfigsAPI from './auth-configs';
import {
  AuthConfigCreateParams,
  AuthConfigCreateResponse,
  AuthConfigDeleteResponse,
  AuthConfigListParams,
  AuthConfigListResponse,
  AuthConfigRetrieveResponse,
  AuthConfigUpdateParams,
  AuthConfigUpdateResponse,
  AuthConfigUpdateStatusParams,
  AuthConfigUpdateStatusResponse,
  AuthConfigs,
} from './auth-configs';
import * as CliAPI from './cli';
import {
  Cli,
  CliCreateSessionResponse,
  CliLinkSessionParams,
  CliLinkSessionResponse,
  CliRetrieveSessionParams,
  CliRetrieveSessionResponse,
} from './cli';
import * as ConnectedAccountsAPI from './connected-accounts';
import {
  ConnectedAccountCreateParams,
  ConnectedAccountCreateResponse,
  ConnectedAccountDeleteResponse,
  ConnectedAccountListParams,
  ConnectedAccountListResponse,
  ConnectedAccountRefreshResponse,
  ConnectedAccountRetrieveResponse,
  ConnectedAccountUpdateStatusParams,
  ConnectedAccountUpdateStatusResponse,
  ConnectedAccounts,
} from './connected-accounts';
import * as PaymentsAPI from './payments';
import {
  PaymentCreateSessionParams,
  PaymentCreateSessionResponse,
  PaymentManageSubscriptionParams,
  PaymentManageSubscriptionResponse,
  Payments,
} from './payments';
import * as TeamMembersAPI from './team-members';
import {
  TeamMemberInviteParams,
  TeamMemberInviteResponse,
  TeamMemberListResponse,
  TeamMemberRemoveResponse,
  TeamMemberUpdateParams,
  TeamMemberUpdateResponse,
  TeamMembers,
} from './team-members';
import * as ToolkitsAPI from './toolkits';
import {
  ToolkitListParams,
  ToolkitListResponse,
  ToolkitRetrieveCategoriesResponse,
  ToolkitRetrieveResponse,
  Toolkits,
} from './toolkits';
import * as TriggersTypesAPI from './triggers-types';
import {
  TriggersTypeListParams,
  TriggersTypeListResponse,
  TriggersTypeRetrieveEnumResponse,
  TriggersTypeRetrieveResponse,
  TriggersTypes,
} from './triggers-types';
import * as AuthAPI from './auth/auth';
import {
  Auth,
  AuthLoginParams,
  AuthOneTapParams,
  AuthOneTapResponse,
  AuthRetrieveCallbackParams,
  AuthRetrieveCallbackResponse,
} from './auth/auth';
import * as InternalAPI from './internal/internal';
import { Internal } from './internal/internal';
import * as OpenAPIAPI from './openapi/openapi';
import { OpenAPI } from './openapi/openapi';
import * as OrgAPI from './org/org';
import { Org } from './org/org';
import * as ToolsAPI from './tools/tools';
import {
  ToolListParams,
  ToolListResponse,
  ToolRetrieveEnumResponse,
  ToolRetrieveResponse,
  Tools,
} from './tools/tools';
import * as TriggerInstancesAPI from './trigger-instances/trigger-instances';
import {
  TriggerInstanceListActiveParams,
  TriggerInstanceListActiveResponse,
  TriggerInstanceRemoveUpsertResponse,
  TriggerInstanceUpdateStatusParams,
  TriggerInstanceUpdateStatusResponse,
  TriggerInstanceUpsertParams,
  TriggerInstanceUpsertResponse,
  TriggerInstances,
} from './trigger-instances/trigger-instances';

export class API extends APIResource {
  auth: AuthAPI.Auth = new AuthAPI.Auth(this._client);
  admin: AdminAPI.Admin = new AdminAPI.Admin(this._client);
  authConfigs: AuthConfigsAPI.AuthConfigs = new AuthConfigsAPI.AuthConfigs(this._client);
  cli: CliAPI.Cli = new CliAPI.Cli(this._client);
  connectedAccounts: ConnectedAccountsAPI.ConnectedAccounts = new ConnectedAccountsAPI.ConnectedAccounts(
    this._client,
  );
  internal: InternalAPI.Internal = new InternalAPI.Internal(this._client);
  openAPI: OpenAPIAPI.OpenAPI = new OpenAPIAPI.OpenAPI(this._client);
  org: OrgAPI.Org = new OrgAPI.Org(this._client);
  teamMembers: TeamMembersAPI.TeamMembers = new TeamMembersAPI.TeamMembers(this._client);
  toolkits: ToolkitsAPI.Toolkits = new ToolkitsAPI.Toolkits(this._client);
  tools: ToolsAPI.Tools = new ToolsAPI.Tools(this._client);
  triggerInstances: TriggerInstancesAPI.TriggerInstances = new TriggerInstancesAPI.TriggerInstances(
    this._client,
  );
  triggersTypes: TriggersTypesAPI.TriggersTypes = new TriggersTypesAPI.TriggersTypes(this._client);
  payments: PaymentsAPI.Payments = new PaymentsAPI.Payments(this._client);
}

API.Auth = Auth;
API.Admin = Admin;
API.AuthConfigs = AuthConfigs;
API.Cli = Cli;
API.ConnectedAccounts = ConnectedAccounts;
API.Internal = Internal;
API.OpenAPI = OpenAPI;
API.Org = Org;
API.TeamMembers = TeamMembers;
API.Toolkits = Toolkits;
API.Tools = Tools;
API.TriggerInstances = TriggerInstances;
API.TriggersTypes = TriggersTypes;
API.Payments = Payments;

export declare namespace API {
  export {
    Auth as Auth,
    type AuthOneTapResponse as AuthOneTapResponse,
    type AuthRetrieveCallbackResponse as AuthRetrieveCallbackResponse,
    type AuthLoginParams as AuthLoginParams,
    type AuthOneTapParams as AuthOneTapParams,
    type AuthRetrieveCallbackParams as AuthRetrieveCallbackParams,
  };

  export {
    Admin as Admin,
    type AdminIdentifyResponse as AdminIdentifyResponse,
    type AdminIdentifyParams as AdminIdentifyParams,
  };

  export {
    AuthConfigs as AuthConfigs,
    type AuthConfigCreateResponse as AuthConfigCreateResponse,
    type AuthConfigRetrieveResponse as AuthConfigRetrieveResponse,
    type AuthConfigUpdateResponse as AuthConfigUpdateResponse,
    type AuthConfigListResponse as AuthConfigListResponse,
    type AuthConfigDeleteResponse as AuthConfigDeleteResponse,
    type AuthConfigUpdateStatusResponse as AuthConfigUpdateStatusResponse,
    type AuthConfigCreateParams as AuthConfigCreateParams,
    type AuthConfigUpdateParams as AuthConfigUpdateParams,
    type AuthConfigListParams as AuthConfigListParams,
    type AuthConfigUpdateStatusParams as AuthConfigUpdateStatusParams,
  };

  export {
    Cli as Cli,
    type CliCreateSessionResponse as CliCreateSessionResponse,
    type CliLinkSessionResponse as CliLinkSessionResponse,
    type CliRetrieveSessionResponse as CliRetrieveSessionResponse,
    type CliLinkSessionParams as CliLinkSessionParams,
    type CliRetrieveSessionParams as CliRetrieveSessionParams,
  };

  export {
    ConnectedAccounts as ConnectedAccounts,
    type ConnectedAccountCreateResponse as ConnectedAccountCreateResponse,
    type ConnectedAccountRetrieveResponse as ConnectedAccountRetrieveResponse,
    type ConnectedAccountListResponse as ConnectedAccountListResponse,
    type ConnectedAccountDeleteResponse as ConnectedAccountDeleteResponse,
    type ConnectedAccountRefreshResponse as ConnectedAccountRefreshResponse,
    type ConnectedAccountUpdateStatusResponse as ConnectedAccountUpdateStatusResponse,
    type ConnectedAccountCreateParams as ConnectedAccountCreateParams,
    type ConnectedAccountListParams as ConnectedAccountListParams,
    type ConnectedAccountUpdateStatusParams as ConnectedAccountUpdateStatusParams,
  };

  export { Internal as Internal };

  export { OpenAPI as OpenAPI };

  export { Org as Org };

  export {
    TeamMembers as TeamMembers,
    type TeamMemberUpdateResponse as TeamMemberUpdateResponse,
    type TeamMemberListResponse as TeamMemberListResponse,
    type TeamMemberInviteResponse as TeamMemberInviteResponse,
    type TeamMemberRemoveResponse as TeamMemberRemoveResponse,
    type TeamMemberUpdateParams as TeamMemberUpdateParams,
    type TeamMemberInviteParams as TeamMemberInviteParams,
  };

  export {
    Toolkits as Toolkits,
    type ToolkitRetrieveResponse as ToolkitRetrieveResponse,
    type ToolkitListResponse as ToolkitListResponse,
    type ToolkitRetrieveCategoriesResponse as ToolkitRetrieveCategoriesResponse,
    type ToolkitListParams as ToolkitListParams,
  };

  export {
    Tools as Tools,
    type ToolRetrieveResponse as ToolRetrieveResponse,
    type ToolListResponse as ToolListResponse,
    type ToolRetrieveEnumResponse as ToolRetrieveEnumResponse,
    type ToolListParams as ToolListParams,
  };

  export {
    TriggerInstances as TriggerInstances,
    type TriggerInstanceListActiveResponse as TriggerInstanceListActiveResponse,
    type TriggerInstanceRemoveUpsertResponse as TriggerInstanceRemoveUpsertResponse,
    type TriggerInstanceUpdateStatusResponse as TriggerInstanceUpdateStatusResponse,
    type TriggerInstanceUpsertResponse as TriggerInstanceUpsertResponse,
    type TriggerInstanceListActiveParams as TriggerInstanceListActiveParams,
    type TriggerInstanceUpdateStatusParams as TriggerInstanceUpdateStatusParams,
    type TriggerInstanceUpsertParams as TriggerInstanceUpsertParams,
  };

  export {
    TriggersTypes as TriggersTypes,
    type TriggersTypeRetrieveResponse as TriggersTypeRetrieveResponse,
    type TriggersTypeListResponse as TriggersTypeListResponse,
    type TriggersTypeRetrieveEnumResponse as TriggersTypeRetrieveEnumResponse,
    type TriggersTypeListParams as TriggersTypeListParams,
  };

  export {
    Payments as Payments,
    type PaymentCreateSessionResponse as PaymentCreateSessionResponse,
    type PaymentManageSubscriptionResponse as PaymentManageSubscriptionResponse,
    type PaymentCreateSessionParams as PaymentCreateSessionParams,
    type PaymentManageSubscriptionParams as PaymentManageSubscriptionParams,
  };
}
