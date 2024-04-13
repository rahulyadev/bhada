import { defineStore } from 'pinia';
import useAccountApi from 'src/api/account';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { RegisterData, User } from 'src/models/account';


export default defineStore('account', () => {
  const router = useRouter();
  const accountApi = useAccountApi();
  const user = ref<User>({
    id: 0,
    first_name: '',
    last_name: '',
    email: '',
    phone_number: '',
  });

  const loginUser = async (phone_number: string, password: string) => {
    const data = {
      phone_number: phone_number,
      password: password, 
    }
    const response = await accountApi.login(data);
    console.log(response);
    if (response && response.refresh && response.access) {
      localStorage.setItem('refreshToken', response.refresh);
      localStorage.setItem('accessToken', response.access);
      localStorage.setItem('id', response.id);
      console.log('Login successful and tokens stored.');
    } else {
      console.error('No tokens received from the API');
    }
  };

  const registerUser = async (registerData: RegisterData) => {
    const response = await accountApi.register(registerData);
    console.log(response);
    if (response && response.refresh && response.access) {
      localStorage.setItem('refreshToken', response.refresh);
      localStorage.setItem('accessToken', response.access);
      localStorage.setItem('id', response.id);
      console.log('Login successful and tokens stored.');
    } else {
      console.error('No tokens received from the API');
    }
  };

  const logout = async () => {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    localStorage.removeItem('id');
    router.push({ name: 'account/LoginUser' });
  };

  const getCurrentUser = async () => {
    const id = localStorage.getItem('id');
    console.log('id ==>>> ', id);
    if (!id) {
      console.log('router ==>>> ', router);
      const r = router.getRoutes();
      console.log('r ==>>> ', r);
      router.push({ name: 'account/LoginUser' });
      return;
    }
    const response = await accountApi.getCurrentUser(id);
    user.value = response;
  }

  return {
    user,
    loginUser,
    logout,
    registerUser,
    getCurrentUser,
  };
});
