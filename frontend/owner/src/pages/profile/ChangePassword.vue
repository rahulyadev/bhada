<template>
  <q-page class="row items-center justify-evenly">
    <div class="row justify-center col-6">
      <div class="text-grey-9 text-h5 text-weight-bold">Change Password</div>
      <q-input
        class="col-12 q-mt-md"
        dense
        outlined
        v-model="password"
        label="Password"
      ></q-input>
      <q-input
        dense
        outlined
        class="q-mt-md col-12"
        v-model="confirmPassword"
        type="password"
        label="Consfirm Password"
      ></q-input>
      <q-btn
        style="border-radius: 8px"
        color="dark"
        rounded
        size="md"
        label="Sumbit"
        no-caps
        class="q-mt-lg col-12"
        @click="submit"
      ></q-btn>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import useProfileStore from 'src/stores/profile';

const profileStore = useProfileStore();
const password = ref('');
const confirmPassword = ref('');

const submit = async () => {
  if (password.value !== confirmPassword.value) {
    return;
  }
  const data = {
    password: password.value,
    confirm_password: confirmPassword.value,
  };
  await profileStore.changePassword(data);
};
</script>
