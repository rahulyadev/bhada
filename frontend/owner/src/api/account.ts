import { api } from 'src/boot/axios';
import { useApiHelper } from 'src/utils/api';
import { LoginData, RegisterData, TokenResponse } from 'src/models/account';

export default () => {
  const apihelper = useApiHelper({
    api: api,
    baseUrl: '/api/',
  });

  return {
    login: (data: LoginData) =>
      apihelper.post('user/login/', data) as Promise<TokenResponse>,
    register: (data: RegisterData) =>
      apihelper.post('user/register/', data) as Promise<TokenResponse>,
  };
};
