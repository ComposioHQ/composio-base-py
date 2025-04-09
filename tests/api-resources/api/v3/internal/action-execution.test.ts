// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ComposioSDK from 'composio-sdk';

const client = new ComposioSDK({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource actionExecution', () => {
  // skipped: tests are disabled for the time being
  test.skip('log: only required params', async () => {
    const responsePromise = client.api.v3.internal.actionExecution.log({ cursor: 0 });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // skipped: tests are disabled for the time being
  test.skip('log: required and optional params', async () => {
    const response = await client.api.v3.internal.actionExecution.log({
      cursor: 0,
      case_sensitive: true,
      from: 0,
      limit: 0,
      search_params: [{ field: 'field', operation: 'operation', value: 'value' }],
      to: 0,
    });
  });

  // skipped: tests are disabled for the time being
  test.skip('retrieveFields', async () => {
    const responsePromise = client.api.v3.internal.actionExecution.retrieveFields();
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // skipped: tests are disabled for the time being
  test.skip('retrieveLog', async () => {
    const responsePromise = client.api.v3.internal.actionExecution.retrieveLog('id');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });
});
