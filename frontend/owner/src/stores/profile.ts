import { defineStore } from 'pinia';
import useProfileApi from 'src/api/profile';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { ChangePasswordData, User } from 'src/models/profile';

export default defineStore('profile', () => {
  const router = useRouter();
  const profileApi = useProfileApi();
  const user = ref<User>({
    id: 0,
    first_name: '',
    last_name: '',
    email: '',
    phone_number: '',
  });

  const getCurrentUser = async () => {
    const id = localStorage.getItem('id');
    if (!id) {
      router.push({ name: 'account/LoginUser' });
      return;
    }
    const response = await profileApi.getCurrentUser(id);
    user.value = response;
  };

  const changePassword = async (data: ChangePasswordData) => {
    await profileApi.changePassword(data);
  };

  return {
    user,
    getCurrentUser,
    changePassword,
  };
});
