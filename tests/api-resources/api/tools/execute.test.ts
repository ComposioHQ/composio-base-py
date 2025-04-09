// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ComposioSDK from 'composio-sdk';

const client = new ComposioSDK({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource execute', () => {
  // skipped: tests are disabled for the time being
  test.skip('input: only required params', async () => {
    const responsePromise = client.api.tools.execute.input('actionName', { text: 'text' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // skipped: tests are disabled for the time being
  test.skip('input: required and optional params', async () => {
    const response = await client.api.tools.execute.input('actionName', {
      text: 'text',
      customDescription: 'customDescription',
      systemPrompt: 'systemPrompt',
      version: 'version',
    });
  });

  // skipped: tests are disabled for the time being
  test.skip('proxy: only required params', async () => {
    const responsePromise = client.api.tools.execute.proxy({ endpoint: 'endpoint', method: 'GET' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // skipped: tests are disabled for the time being
  test.skip('proxy: required and optional params', async () => {
    const response = await client.api.tools.execute.proxy({
      endpoint: 'endpoint',
      method: 'GET',
      body: {},
      connected_account_id: 'connected_account_id',
      parameters: [{ name: 'name', type: 'header', value: 'value' }],
    });
  });

  // skipped: tests are disabled for the time being
  test.skip('run', async () => {
    const responsePromise = client.api.tools.execute.run('action');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // skipped: tests are disabled for the time being
  test.skip('run: request options and params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(
      client.api.tools.execute.run(
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
});
