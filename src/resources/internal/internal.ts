// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import * as ActionExecutionAPI from './action-execution';
import {
  ActionExecution,
  ActionExecutionLogParams,
  ActionExecutionLogResponse,
  ActionExecutionRetrieveFieldsResponse,
  ActionExecutionRetrieveLogResponse,
} from './action-execution';
import * as TriggerAPI from './trigger';
import { Trigger, TriggerLogParams, TriggerLogResponse } from './trigger';

export class Internal extends APIResource {
  trigger: TriggerAPI.Trigger = new TriggerAPI.Trigger(this._client);
  actionExecution: ActionExecutionAPI.ActionExecution = new ActionExecutionAPI.ActionExecution(this._client);
}

Internal.Trigger = Trigger;
Internal.ActionExecution = ActionExecution;

export declare namespace Internal {
  export {
    Trigger as Trigger,
    type TriggerLogResponse as TriggerLogResponse,
    type TriggerLogParams as TriggerLogParams,
  };

  export {
    ActionExecution as ActionExecution,
    type ActionExecutionLogResponse as ActionExecutionLogResponse,
    type ActionExecutionRetrieveFieldsResponse as ActionExecutionRetrieveFieldsResponse,
    type ActionExecutionRetrieveLogResponse as ActionExecutionRetrieveLogResponse,
    type ActionExecutionLogParams as ActionExecutionLogParams,
  };
}
