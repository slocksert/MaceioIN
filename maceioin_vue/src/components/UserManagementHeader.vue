<template>
    <header class="header">
      <router-link to="/">
        <img src="../assets/logo.png" alt="Maceió IN" />
      </router-link>
      <button @click="logout"> Logout </button>
    </header>
  </template>
  
<script>
  export default {
    name: 'PageHeader',
    methods: {
      logout() {
        localStorage.removeItem('access_token');
        this.$router.push('/login');
      }
    }
  };
</script>
  
<style scoped>
  .header {
    padding: 1rem;
    display: flex;
    justify-content: space-between;
  }
  
  .header img {
    max-width: 300px;
  }
  
  .header h1 {
    margin: 0;
    color: #fff;
  }

  button {
    border: none; 
    border-radius: 4px; 
    cursor: pointer;
    color: white;
    padding: 1rem;
    background-color: #FF4136;
    text-transform: capitalize;
  }

  button:hover {
    background-color: #CC322A;
  }
</style>