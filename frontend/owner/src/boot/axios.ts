import { boot } from 'quasar/wrappers';
import axios, {
  AxiosInstance,
  AxiosResponse,
  AxiosRequestHeaders,
} from 'axios';
import { Router } from 'vue-router';

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance;
    $api: AxiosInstance;
  }
}

// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)
const api = axios.create({ baseURL: 'http://127.0.0.1:8000' });

// Modified refreshToken function with actual backend call
async function refreshToken(): Promise<string | null> {
  try {
    // Assume refreshToken is stored in the tokenService
    const refreshToken = tokenService.getRefreshToken();
    if (!refreshToken) {
      // If no refresh token is available, fail here
      console.log('No refresh token available.');
      return null;
    }

    // Making an axios call to refresh token endpoint
    const response = await axios.post(
      'http://127.0.0.1:8000/api/token/refresh/',
      {
        refresh: refreshToken,
      },
    );

    // Assuming your backend responds with new access token
    const { access: newAccessToken } = response.data;
    // Update stored tokens with new access token (and potentially new refresh token if provided by your backend)
    tokenService.setTokens({ accessToken: newAccessToken, refreshToken });

    return newAccessToken;
  } catch (error) {
    console.error('Failed to refresh token:', error);
    // Handle failure (e.g., by clearing stored tokens, redirecting to login, etc.)
    tokenService.clearTokens();
    return null;
  }
}

// Token Service to manage JWT tokens
class TokenService {
  private accessToken: string | null = null;
  private refreshToken: string | null = null;

  setTokens({
    accessToken,
    refreshToken,
  }: {
    accessToken: string;
    refreshToken: string;
  }) {
    this.accessToken = accessToken;
    this.refreshToken = refreshToken;
  }

  getAccessToken() {
    return this.accessToken;
  }

  getRefreshToken() {
    return this.refreshToken;
  }

  clearTokens() {
    this.accessToken = null;
    this.refreshToken = null;
  }
}

const tokenService = new TokenService();

function setupInterceptors(api: AxiosInstance, router: Router) {
  // Define your interceptors here, using `router` to redirect
  // Request interceptor for API calls
  api.interceptors.request.use(
    async (config) => {
      const token = tokenService.getAccessToken();
      if (token) {
        config.headers = {
          Authorization: `Bearer ${token}`,
          ...config.headers,
        } as AxiosRequestHeaders;
      }
      return config;
    },
    (error) => {
      Promise.reject(error);
    },
  );

  // Response interceptor for API calls
  api.interceptors.response.use(
    (response: AxiosResponse) => response,
    async (error) => {
      const originalRequest = error.config;
      if ((error.response.status === 401 || error.response.status === 403) && !originalRequest._retry) {
        originalRequest._retry = true;
        const accessToken = await refreshToken();
        if (accessToken) {
          axios.defaults.headers.common['Authorization'] =
            'Bearer ' + accessToken;
          return api(originalRequest);
        } else {
          // Token refresh has failed, handle accordingly (e.g., redirect to login)
          // You might want to emit an event or call a method to logout the user
          console.error('Token refresh failed, redirecting to login...');
          router.push('/login');
          // Redirect to login or perform logout
        }
      }
      return Promise.reject(error);
    },
  );
}

export default boot(({ app, router }) => {
  // for use inside Vue files (Options API) through this.$axios and this.$api

  app.config.globalProperties.$axios = axios;
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  app.config.globalProperties.$api = api;
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API
  setupInterceptors(api, router);
});

export { api };
