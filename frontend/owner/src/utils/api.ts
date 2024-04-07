import { AxiosInstance, AxiosResponse, ParamsSerializerOptions } from 'axios';

interface APiHelperConfig {
  api: AxiosInstance;
  baseUrl: string;
}

const paramsSerializer: ParamsSerializerOptions = {
  indexes: null, // by default: false
};

const getAxiosResponseData = async (
  axiosReponsePromise: Promise<AxiosResponse>,
) => (await axiosReponsePromise).data as Promise<unknown>;

export const useApiHelper = (config: APiHelperConfig) => {
  return {
    get: async (url: string, options = {}) =>
      getAxiosResponseData(
        config.api.get(`${config.baseUrl}${url}`, {
          paramsSerializer: paramsSerializer,
          ...options,
        }),
      ),
    post: async (url: string, data: unknown, options = {}) =>
      getAxiosResponseData(
        config.api.post(`${config.baseUrl}${url}`, data, {
          paramsSerializer: paramsSerializer,
          ...options,
        }),
      ),
    put: async (url: string, data: unknown, options = {}) =>
      getAxiosResponseData(
        config.api.put(`${config.baseUrl}${url}`, data, {
          paramsSerializer: paramsSerializer,
          ...options,
        }),
      ),
    patch: async (url: string, data: unknown, options = {}) =>
      getAxiosResponseData(
        config.api.patch(`${config.baseUrl}${url}`, data, {
          paramsSerializer: paramsSerializer,
          ...options,
        }),
      ),
    delete: async (url: string, options = {}) =>
      getAxiosResponseData(
        config.api.delete(`${config.baseUrl}${url}`, {
          paramsSerializer: paramsSerializer,
          ...options,
        }),
      ),
  };
};
