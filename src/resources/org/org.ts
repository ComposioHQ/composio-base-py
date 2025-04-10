// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import * as ProjectAPI from './project/project';
import {
  Project,
  ProjectCreateParams,
  ProjectCreateResponse,
  ProjectDeleteResponse,
  ProjectListResponse,
  ProjectRetrieveResponse,
} from './project/project';
import { APIPromise } from '../../core/api-promise';
import { RequestOptions } from '../../internal/request-options';

export class Org extends APIResource {
  project: ProjectAPI.Project = new ProjectAPI.Project(this._client);

  regenerateAPIKey(options?: RequestOptions): APIPromise<OrgRegenerateAPIKeyResponse> {
    return this._client.post('/api/v3/org/api_key/regenerate', options);
  }

  retrieveAPIKey(options?: RequestOptions): APIPromise<OrgRetrieveAPIKeyResponse> {
    return this._client.get('/api/v3/org/api_key', options);
  }
}

export interface OrgRegenerateAPIKeyResponse {
  org_api_key: string;
}

export interface OrgRetrieveAPIKeyResponse {
  org_api_key: string;
}

Org.Project = Project;

export declare namespace Org {
  export {
    type OrgRegenerateAPIKeyResponse as OrgRegenerateAPIKeyResponse,
    type OrgRetrieveAPIKeyResponse as OrgRetrieveAPIKeyResponse,
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
