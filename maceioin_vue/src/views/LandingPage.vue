<template>
    <div class="landing-page">
      <header class="header">
        <img src="../assets/logo.png" alt="Maceió IN" />
        <h1>Maceió IN</h1>
      </header>
      <main class="main-content">
        <section class="intro">
          <h2>Secretaria de Fazenda de Maceió</h2>
          <p>Bem-vindo ao site da Secretaria de Fazenda de Maceió. Aqui você encontrará informações sobre nossas atividades e serviços.</p>
        </section>
      </main>
      <footer class="footer">
        <p>&copy; {{ currentYear }} Maceió IN. Todos os direitos reservados.</p>
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
    color: #333;
    background-color: #fff;
  }
  
  .header {
    background-color: #007BFF; /* Blue */
    padding: 20px;
    text-align: center;
  }
  
  .header img {
    max-width: 100px;
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
  
  .footer {
    background-color: #007BFF; /* Blue */
    padding: 10px;
    text-align: center;
    color: #fff;
  }
  </style>