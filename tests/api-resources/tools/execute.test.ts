// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ComposioSDK from 'composio-sdk';

const client = new ComposioSDK({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource execute', () => {
  test('execute', async () => {
    const responsePromise = client.tools.execute.execute('action');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('execute: request options and params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(
      client.tools.execute.execute(
        'action',
        {
          allow_tracing: true,
          arguments: { foo: 'bar' },
          connected_account_id: 'connected_account_id',
          entity_id: 'entity_id',
          text: 'text',
          version: 'version',
        },
        { path: '/_stainless_unknown_path' },
      ),
    ).rejects.toThrow(ComposioSDK.NotFoundError);
  });

  test('input: only required params', async () => {
    const responsePromise = client.tools.execute.input('actionName', { text: 'text' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('input: required and optional params', async () => {
    const response = await client.tools.execute.input('actionName', {
      text: 'text',
      customDescription: 'customDescription',
      systemPrompt: 'systemPrompt',
      version: 'version',
    });
  });

  test('proxy: only required params', async () => {
    const responsePromise = client.tools.execute.proxy({ endpoint: 'endpoint', method: 'GET' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('proxy: required and optional params', async () => {
    const response = await client.tools.execute.proxy({
      endpoint: 'endpoint',
      method: 'GET',
      body: {},
      connected_account_id: 'connected_account_id',
      parameters: [{ name: 'name', type: 'header', value: 'value' }],
    });
  });
});
