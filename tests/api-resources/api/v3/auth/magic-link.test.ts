// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ComposioSDK from 'composio-sdk';

const client = new ComposioSDK({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource magicLink', () => {
  // skipped: tests are disabled for the time being
  test.skip('send: only required params', async () => {
    const responsePromise = client.api.v3.auth.magicLink.send({ email: 'dev@stainless.com' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // skipped: tests are disabled for the time being
  test.skip('send: required and optional params', async () => {
    const response = await client.api.v3.auth.magicLink.send({
      email: 'dev@stainless.com',
      verifyHost: 'verifyHost',
    });
  });

  // skipped: tests are disabled for the time being
  test.skip('verify: only required params', async () => {
    const responsePromise = client.api.v3.auth.magicLink.verify({ token: 'token' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // skipped: tests are disabled for the time being
  test.skip('verify: required and optional params', async () => {
    const response = await client.api.v3.auth.magicLink.verify({ token: 'token' });
  });
});
