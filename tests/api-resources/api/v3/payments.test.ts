// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ComposioSDK from 'composio-sdk';

const client = new ComposioSDK({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource payments', () => {
  // skipped: tests are disabled for the time being
  test.skip('createSession: only required params', async () => {
    const responsePromise = client.api.v3.payments.createSession({ applyDiscount: true, plan: 'HOBBY' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // skipped: tests are disabled for the time being
  test.skip('createSession: required and optional params', async () => {
    const response = await client.api.v3.payments.createSession({ applyDiscount: true, plan: 'HOBBY' });
  });

  // skipped: tests are disabled for the time being
  test.skip('manageSubscription', async () => {
    const responsePromise = client.api.v3.payments.manageSubscription();
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // skipped: tests are disabled for the time being
  test.skip('manageSubscription: request options and params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(
      client.api.v3.payments.manageSubscription({}, { path: '/_stainless_unknown_path' }),
    ).rejects.toThrow(ComposioSDK.NotFoundError);
  });
});
