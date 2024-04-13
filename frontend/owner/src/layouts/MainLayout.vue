<template>
  <q-layout v-show="!loading" view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title> Bhada </q-toolbar-title>

        <q-btn-dropdown
          dense
          flat
          :ripple="false"
          icon="person"
          no-caps
          :label="accountStore.user.first_name"
        >
          <q-list>
            <q-item clickable @click="logout">
              <q-item-section>
                <q-item-label>Logout</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
        </q-btn-dropdown>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header> Essential Links </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
  <div v-show="loading" class="fixed-center">
    <div>
      <q-spinner-gears color="primary" size="5rem" />
      <div class="text-h6 text-center">Loading...</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import EssentialLink, {
  EssentialLinkProps,
} from 'components/EssentialLink.vue';
import useAccountStore from 'src/stores/account';

const accountStore = useAccountStore();
const loading = ref(true);

onMounted(async () => {
  await accountStore.getCurrentUser();
  loading.value = false;
});

const essentialLinks: EssentialLinkProps[] = [
  {
    title: 'Account',
    caption: 'Account details',
    icon: 'school',
    link: 'https://quasar.dev',
  },
  {
    title: 'Property',
    caption: 'Property details',
    icon: 'code',
    link: 'https://github.com/quasarframework',
  },
];

const leftDrawerOpen = ref(false);

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}

const logout = () => {
  accountStore.logout();
};
</script>
