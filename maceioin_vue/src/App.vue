<template>
  <div class="landing-page">
    <header class="header">
      <h1>MaceióIN</h1>
    </header>
    <main class="main-content">
      <section class="intro">
        <h2>Welcome to MaceióIN</h2>
        <p>Discover the beauty and culture of Maceió.</p>
      </section>
      <section class="features">
        <h2>Features</h2>
        <ul>
          <li>Beautiful Beaches</li>
          <li>Rich Culture</li>
          <li>Delicious Cuisine</li>
        </ul>
      </section>
    </main>
    <footer class="footer">
      <p>&copy; {{ currentYear }} MaceióIN. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentYear: new Date().getFullYear()
    };
  }
};
</script>

<style scoped>
.landing-page {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  font-family: Arial, sans-serif;
  color: #fff;
  background-color: #fff;
}

.header {
  background-color: #007BFF; /* Blue */
  padding: 20px;
  text-align: center;
}

.header h1 {
  margin: 0;
  color: #fff;
}

.main-content {
  flex: 1;
  padding: 20px;
}

.intro {
  background-color: #FFA500; /* Orange */
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 20px;
}

.features {
  background-color: #007BFF; /* Blue */
  padding: 20px;
  border-radius: 8px;
}

.features ul {
  list-style-type: none;
  padding: 0;
}

.features li {
  margin: 10px 0;
}

.footer {
  background-color: #007BFF; /* Blue */
  padding: 10px;
  text-align: center;
}
</style>
