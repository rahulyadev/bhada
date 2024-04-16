<template>
  <q-page class="row items-center justify-evenly">
    Homeee User details: {{ profileStore.user }}
  </q-page>
</template>

<script setup lang="ts">
import useProfileStore from 'src/stores/profile';

const profileStore = useProfileStore();
</script>
