<template>
    <section class="about-sefaz">
      <h2>Sobre a <span id="sefaz">SEFAZ</span></h2>
      <a href="https://www.sefaz.al.gov.br/" target="_blank">
        <img class="logo-sefaz" src="../assets/sefaz.jpg" alt="Logo da SEFAZ AL" />
      </a>
      <p>
        A Secretaria de Estado da Fazenda de Alagoas é responsável pelo planejamento,
        execução e avaliação das políticas financeiras, contábeis e tributárias do Estado.
      </p>
      <p>
        Sua atuação inclui a gestão da arrecadação de tributos, administração financeira,
        transparência fiscal e educação tributária.
      </p>
    </section>
  </template>
  
  <script>
  export default {
    name: 'AboutSefazSection',
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');

  #sefaz {
    font-weight: bold;
  }
  
  .about-sefaz {
    text-align: center;
    padding: 2rem;
    background: #f8f9fa;
    font-family: Roboto, sans-serif;
  }

  .about-sefaz p{
    text-align: justify;
  }
  
  .logo-sefaz {
    border-radius: 1rem;
    max-width: 100%;
    height: auto;
  }
  
  .about-sefaz h2 {
    color: #007BFF;
    margin-bottom: 15px;
    font-weight: 400;
  }
  
  .about-sefaz p {
    max-width: 600px;
    margin: 1rem auto 0;
    font-size: 1rem;
    line-height: 1.5;
  }
  </style>
  