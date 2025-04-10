// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import * as APIKeyAPI from './api-key';
import { APIKey, APIKeyRegenerateResponse, APIKeyRetrieveResponse } from './api-key';
import * as ProjectAPI from './project/project';
import {
  Project,
  ProjectCreateParams,
  ProjectCreateResponse,
  ProjectDeleteResponse,
  ProjectListResponse,
  ProjectRetrieveResponse,
} from './project/project';

export class Org extends APIResource {
  apiKey: APIKeyAPI.APIKey = new APIKeyAPI.APIKey(this._client);
  project: ProjectAPI.Project = new ProjectAPI.Project(this._client);
}

Org.APIKey = APIKey;
Org.Project = Project;

export declare namespace Org {
  export {
    APIKey as APIKey,
    type APIKeyRetrieveResponse as APIKeyRetrieveResponse,
    type APIKeyRegenerateResponse as APIKeyRegenerateResponse,
  };

  export {
    Project as Project,
    type ProjectCreateResponse as ProjectCreateResponse,
    type ProjectRetrieveResponse as ProjectRetrieveResponse,
    type ProjectListResponse as ProjectListResponse,
    type ProjectDeleteResponse as ProjectDeleteResponse,
    type ProjectCreateParams as ProjectCreateParams,
  };
}
