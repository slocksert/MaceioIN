<template>
  <header class="header">
    <router-link to="/">
      <img src="../assets/logo.png" alt="Maceió IN" />
    </router-link>
    <button @click="logout" class="logout-button">
      <v-icon name="co-account-logout" class="input-icon" />
      Sair
    </button>
  </header>
</template>

<script>
export default {
  name: 'PageHeader',
  methods: {
    logout() {
      localStorage.removeItem('access_token');
      this.$router.push('/login');
    },
  },
};
</script>

<style scoped>
.header {
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header img {
  max-width: 300px;
}

.logout-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background-color: #ff4136;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.logout-button:hover {
  background-color: #cc322a;
  transform: translateY(-2px);
}

.logout-icon {
  width: 20px;
  height: 20px;
  fill: white;
}
</style>