// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ComposioSDK from 'composio-sdk';

const client = new ComposioSDK({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource trigger', () => {
  // skipped: tests are disabled for the time being
  test.skip('log: only required params', async () => {
    const responsePromise = client.api.v3.internal.trigger.log({ cursor: 'cursor' });
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
    const response = await client.api.v3.internal.trigger.log({
      cursor: 'cursor',
      entityId: 'entityId',
      integrationId: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
      limit: 0,
      search: 'search',
      status: 'success',
      time: '5m',
    });
  });
});
