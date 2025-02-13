<template>
  <header class="header">
    <router-link to="/">
      <img src="../assets/logo.png" alt="Maceió IN" />
    </router-link>
  </header>
</template>

<script>
export default {
  name: 'PageHeader'
};
</script>

<style scoped>
.header {
  padding: 5px;
  text-align: center;
  background: linear-gradient(to right, #ff7f00, #007BFF);
}

.header img {
  max-width: 300px;
}

.header h1 {
  margin: 0;
  color: #fff;
}
</style>
