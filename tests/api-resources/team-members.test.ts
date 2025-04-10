// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ComposioSDK from 'composio-sdk';

const client = new ComposioSDK({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource teamMembers', () => {
  test('update: only required params', async () => {
    const responsePromise = client.teamMembers.update('tm_123456', {
      email: 'dev@stainless.com',
      name: 'name',
      role: 'role',
    });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('update: required and optional params', async () => {
    const response = await client.teamMembers.update('tm_123456', {
      email: 'dev@stainless.com',
      name: 'name',
      role: 'role',
    });
  });

  test('list', async () => {
    const responsePromise = client.teamMembers.list();
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('invite: only required params', async () => {
    const responsePromise = client.teamMembers.invite({
      email: 'dev@stainless.com',
      name: 'name',
      role: 'role',
    });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('invite: required and optional params', async () => {
    const response = await client.teamMembers.invite({
      email: 'dev@stainless.com',
      name: 'name',
      role: 'role',
      verifyHost: 'verifyHost',
    });
  });

  test('remove', async () => {
    const responsePromise = client.teamMembers.remove('tm_123456');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });
});
