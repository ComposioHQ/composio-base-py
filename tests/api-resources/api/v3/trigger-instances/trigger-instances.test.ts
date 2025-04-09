// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ComposioSDK from 'composio-sdk';

const client = new ComposioSDK({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource triggerInstances', () => {
  // skipped: tests are disabled for the time being
  test.skip('listActive', async () => {
    const responsePromise = client.api.v3.triggerInstances.listActive();
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // skipped: tests are disabled for the time being
  test.skip('listActive: request options and params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(
      client.api.v3.triggerInstances.listActive(
        {
          authConfigIds: 'authConfigIds',
          connectedAccountIds: 'connectedAccountIds',
          limit: 1,
          page: 1,
          showDisabled: true,
          triggerIds: 'triggerIds',
          triggerNames: 'triggerNames',
        },
        { path: '/_stainless_unknown_path' },
      ),
    ).rejects.toThrow(ComposioSDK.NotFoundError);
  });

  // skipped: tests are disabled for the time being
  test.skip('removeUpsert', async () => {
    const responsePromise = client.api.v3.triggerInstances.removeUpsert('slug');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // skipped: tests are disabled for the time being
  test.skip('updateStatus: only required params', async () => {
    const responsePromise = client.api.v3.triggerInstances.updateStatus('enable', { slug: 'slug' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // skipped: tests are disabled for the time being
  test.skip('updateStatus: required and optional params', async () => {
    const response = await client.api.v3.triggerInstances.updateStatus('enable', { slug: 'slug' });
  });

  // skipped: tests are disabled for the time being
  test.skip('upsert: only required params', async () => {
    const responsePromise = client.api.v3.triggerInstances.upsert('slug', {
      connectedAuthId: 'connectedAuthId',
      triggerConfig: { foo: 'bar' },
    });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // skipped: tests are disabled for the time being
  test.skip('upsert: required and optional params', async () => {
    const response = await client.api.v3.triggerInstances.upsert('slug', {
      connectedAuthId: 'connectedAuthId',
      triggerConfig: { foo: 'bar' },
    });
  });
});
