// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ComposioSDK from 'composio-sdk';

const client = new ComposioSDK({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource auth', () => {
  // Prism doesn't properly handle redirects
  test.skip('login', async () => {
    const responsePromise = client.api.auth.login('provider_name');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism doesn't properly handle redirects
  test.skip('login: request options and params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(
      client.api.auth.login(
        'provider_name',
        { redirectUri: 'redirectUri' },
        { path: '/_stainless_unknown_path' },
      ),
    ).rejects.toThrow(ComposioSDK.NotFoundError);
  });

  test('oneTap: only required params', async () => {
    const responsePromise = client.api.auth.oneTap('github', { data: { jwt: 'jwt' }, type: 'jwt' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('oneTap: required and optional params', async () => {
    const response = await client.api.auth.oneTap('github', { data: { jwt: 'jwt' }, type: 'jwt' });
  });

  test('retrieveCallback', async () => {
    const responsePromise = client.api.auth.retrieveCallback('github');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('retrieveCallback: request options and params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(
      client.api.auth.retrieveCallback(
        'github',
        {
          authCode: 'authCode',
          code: 'code',
          error: 'error',
          error_description: 'error_description',
          state: 'state',
        },
        { path: '/_stainless_unknown_path' },
      ),
    ).rejects.toThrow(ComposioSDK.NotFoundError);
  });
});
