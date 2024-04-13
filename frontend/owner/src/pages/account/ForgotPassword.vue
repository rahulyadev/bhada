<template>
  <div>Forget Password</div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import useAccountStore from 'src/stores/account';

const accountStore = useAccountStore();
const phoneNumber = ref('3443');
const password = ref('sddsd');

const signIn = () => {
  accountStore.loginUser(phoneNumber.value, password.value);
};

signIn();
</script>
