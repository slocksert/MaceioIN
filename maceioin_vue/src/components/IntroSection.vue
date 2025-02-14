<template>
  <section class="intro">
    <div class="intro-content">
      <p>
        Gerencie com eficiência os cadastros de pessoas da Secretaria da Fazenda.
        Nossa plataforma foi desenvolvida para facilitar a atualização, consulta e manutenção dos registros, garantindo transparência e segurança em cada operação.
      </p>
      <router-link to="/login" class="cta-button">Acessar</router-link>
    </div>
  </section>
</template>

<script>
export default {
  name: 'IntroSection',
};
</script>

<style scoped>
.intro {
  background: linear-gradient(to right, #ff7f00, #007BFF);
  color: white;
  text-align: center;
  padding: 60px 20px;
}

.intro-content {
  max-width: 600px;
  margin: 0 auto;
}

.intro-content p {
  font-size: 1.2rem;
  margin-bottom: 20px;
  text-align: center;
}

.cta-button {
  display: inline-block;
  background: white;
  color: #007BFF;
  padding: 10px 20px;
  border-radius: 5px;
  text-decoration: none;
  font-weight: bold;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.cta-button:hover {
  background-color: #ff7f00;
  color: white;
}
</style>
