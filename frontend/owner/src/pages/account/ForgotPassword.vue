<template>
  <q-page class="flex flex-center bg-grey-2">
    <q-card class="q-pa-md shadow-2 my_card" bordered>
      <q-card-section class="text-center">
        <div class="text-grey-9 text-h5 text-weight-bold">Sign in</div>
        <div class="text-grey-8">Sign in below to access your account</div>
      </q-card-section>
      <q-card-section>
        <q-input
          dense
          outlined
          v-model="phoneNumber"
          label="Phone number"
        ></q-input>
      </q-card-section>
      <q-card-section>
        <q-btn
          style="border-radius: 8px"
          color="dark"
          rounded
          size="md"
          label="Sign in"
          no-caps
          class="full-width"
          @click="signIn"
        ></q-btn>
      </q-card-section>
      <q-card-section class="text-center q-pt-none">
        <div class="text-grey-8">
          Don't have an account yet?
          <a
            href="#"
            class="text-dark text-weight-bold"
            style="text-decoration: none"
            @click.prevent="goToLogin"
            >Login.</a
          >
        </div>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import useAccountStore from 'src/stores/account';
import { useRouter } from 'vue-router';

const router = useRouter();

const accountStore = useAccountStore();
const phoneNumber = ref('');
const firstName = ref('');
const lastName = ref('');
const email = ref('');
const password = ref('');
const confirmPassword = ref('');

const signIn = async () => {
  if (password.value !== confirmPassword.value) {
    alert('Passwords do not match');
    return;
  }
  const data = {
    phone_number: phoneNumber.value,
    first_name: firstName.value,
    last_name: lastName.value,
    email: email.value,
    password: password.value,
  };
  try {
    await accountStore.registerUser(data);
    router.push({ name: 'Home' });
  } catch (error) {
    console.error(error);
  }
};

const goToLogin = () => {
  router.push({ name: 'account/LoginUser' });
};
</script>

<style>
.my_card {
  width: 25rem;
  border-radius: 8px;
  box-shadow:
    0 20px 25px -5px rgb(0 0 0 / 0.1),
    0 8px 10px -6px rgb(0 0 0 / 0.1);
}
</style>
