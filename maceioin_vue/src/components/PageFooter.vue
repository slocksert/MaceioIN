<template>
  <footer class="footer">
    <p>&copy; {{ currentYear }} Maceió IN. Todos os direitos reservados.</p>
  </footer>
</template>

<script>
export default {
  name: 'PageFooter',
  data() {
    return {
      currentYear: new Date().getFullYear()
    };
  }
};
</script>

<style scoped>
.footer {
  background-color: #f4f4f4;
  backdrop-filter: blur(10px);
  padding: 10px;
  text-align: center;
  color: black;
  margin-top: auto;
  position: sticky;
  bottom: 0;
  width: 100%;
}
</style>