import { api } from 'src/boot/axios';
import { useApiHelper } from 'src/utils/api';
import { ChangePasswordData, User } from 'src/models/profile';
import { GenericResponse } from 'src/models/common';

export default () => {
  const apihelper = useApiHelper({
    api: api,
    baseUrl: '/api/',
  });

  return {
    changePassword: (data: ChangePasswordData) =>
      apihelper.patch(
        'user/change-password/',
        data,
      ) as Promise<GenericResponse>,
    getCurrentUser: (id: string) =>
      apihelper.get(`user/profile/${id}/`) as Promise<User>,
    getUsers: () => apihelper.get('user/profile/') as Promise<User[]>,
  };
};
