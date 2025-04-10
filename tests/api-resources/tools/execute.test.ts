// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ComposioSDK from 'composio-sdk';

const client = new ComposioSDK({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource execute', () => {
  test('getInput: only required params', async () => {
    const responsePromise = client.tools.execute.getInput('actionName', { text: 'text' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('getInput: required and optional params', async () => {
    const response = await client.tools.execute.getInput('actionName', {
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
