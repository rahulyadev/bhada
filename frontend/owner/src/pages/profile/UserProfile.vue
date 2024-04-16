<template>
  <q-page class="row items-center justify-evenly">
    <div class="row justify-center col-6">
      <div class="text-grey-9 text-h5 text-weight-bold">Your Profile data</div>
      <q-input
        dense
        outlined
        disable
        v-model="phoneNumber"
        label="Phone number"
        class="col-12 q-mt-md"
      ></q-input>
      <q-input
        dense
        outlined
        v-model="firstName"
        label="First name"
        class="col-12 q-mt-md"
      ></q-input>
      <q-input
        dense
        outlined
        v-model="lastName"
        label="Last name"
        class="col-12 q-mt-md"
      ></q-input>
      <q-input
        dense
        outlined
        type="email"
        v-model="email"
        label="Email"
        class="col-12 q-mt-md"
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
const user = profileStore.user;
const phoneNumber = ref(user?.phone_number);
const firstName = ref(user?.first_name);
const lastName = ref(user?.last_name);
const email = ref(user?.email);
// const upiId = ref(user?.upi_id);

const submit = async () => {
  // const data = {
  //   password: password.value,
  //   confirm_password: confirmPassword.value,
  // };
  // await profileStore.changePassword(data);
};
</script>
