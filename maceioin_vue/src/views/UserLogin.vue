<template>
  <div id="app">
    <LoginForm />
    <PageFooter />
  </div>
</template>

<script>
import LoginForm from '../components/LoginForm.vue';
import PageFooter from '../components/PageFooter.vue';


export default {
  components: {
    LoginForm,
    PageFooter
  }
};
</script>

<style>
html, body, #app {
  height: 100%;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

#app {
  display: flex;
  flex-direction: column;
  justify-content: space-between; 
}

main {
  flex: 1;
}

.footer {
  background: rgba(0, 0, 0, 0.781);
  backdrop-filter: blur(10px);
  padding: 10px;
  text-align: center;
  color: #fff;
}
</style>