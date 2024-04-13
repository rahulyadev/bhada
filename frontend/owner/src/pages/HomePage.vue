<template>
  <q-page class="row items-center justify-evenly">
    Homeee
    User details: {{ accountStore.user }}
  </q-page>
</template>

<script setup lang="ts">
import useAccountStore from 'src/stores/account';

const accountStore = useAccountStore();

</script>
