import { Account } from 'src/models/accounts';
import { api } from 'src/boot/axios';
import { useApiHelper } from 'src/utils/api';

export default () => {
  const apihelper = useApiHelper({
    api: api,
    baseUrl: '/api/',
  });

  return {
    getCurrentUser: (id: number) =>
      apihelper.get(`user/profile/${id}/`) as Promise<Account>,
    getUsers: () =>
      apihelper.get('user/profile/') as Promise<Account[]>,
  };
};
