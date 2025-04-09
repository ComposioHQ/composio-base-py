// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import * as SpecsAPI from './specs';
import {
  SpecCreateParams,
  SpecCreateResponse,
  SpecDeleteResponse,
  SpecListResponse,
  SpecRetrieveStatusResponse,
  Specs,
} from './specs';

export class OpenAPI extends APIResource {
  specs: SpecsAPI.Specs = new SpecsAPI.Specs(this._client);
}

OpenAPI.Specs = Specs;

export declare namespace OpenAPI {
  export {
    Specs as Specs,
    type SpecCreateResponse as SpecCreateResponse,
    type SpecListResponse as SpecListResponse,
    type SpecDeleteResponse as SpecDeleteResponse,
    type SpecRetrieveStatusResponse as SpecRetrieveStatusResponse,
    type SpecCreateParams as SpecCreateParams,
  };
}
