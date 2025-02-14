<template>
  <div class="container">
    <header class="header">
      <router-link to="/">
        <img src="../assets/logo.png" alt="Maceió IN" class="logo" />
      </router-link>
    </header>
    <div class="login-card">
      <h2>Bem-vindo</h2>
      <form @submit.prevent="login">
        <div class="input-group">
          <v-icon name="co-user" class="input-icon" />
          <input
            type="text"
            id="username"
            v-model="username"
            placeholder="Usuário"
            required
          />
        </div>
        <div class="input-group">
          <v-icon name="co-lock-locked" class="input-icon" />
          <input
            type="password"
            id="password"
            v-model="password"
            placeholder="Senha"
            required
          />
        </div>
        <div class="btn-container">
          <button type="submit" class="btn-login">Entrar</button>
        </div>
      </form>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import { useToast } from "vue-toastification";

export default {
  name: "LoginForm",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  created() {
    const token = localStorage.getItem("access_token");
    if (token) {
      this.$router.push("/admin");
    }
  },
  methods: {
    async login() {
      const toast = useToast();
      try {
        const response = await axios.post("https://djangoapi.slocksert.dev/login/", {
          username: this.username,
          password: this.password,
        });

        if (response.status === 200) {
          localStorage.setItem("access_token", response.data.access);
          localStorage.setItem("refresh_token", response.data.refresh);
          toast.success("Login realizado com sucesso! 🚀");
          this.$router.push("/admin");
        }
      } catch (error) {
        if (error.response && error.response.status === 401) {
          toast.error("Usuário ou senha inválidos.");
        } else {
          toast.error(
            "Falha no login: Erro de conexão com o servidor. Tente novamente mais tarde."
          );
        }
      }
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  margin: 0;
  padding: 2rem;
  box-sizing: border-box;
}

.header {
  position: absolute;
  top: 1rem;
  left: 1rem;
}

.logo {
  max-width: 100%;
  height: auto;
}

.login-card {
  background: #fff;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 25rem;
  width: 90%;
  animation: fadeIn 0.5s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

h2 {
  margin-bottom: 1.5rem;
  color: #333;
  font-family: 'Poppins', sans-serif;
}

.input-group {
  position: relative;
  width: 75%;
  margin: 0 auto 1.5rem;
}

.input-icon {
  position: absolute;
  top: 50%;
  left: 1rem;
  transform: translateY(-50%);
  color: #aaa;
}

.input-group input {
  width: 50%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.input-group input:focus {
  border-color: #5563de;
  outline: none;
}

.btn-container {
  display: flex;
  justify-content: center;
  width: 100%;
}

.btn-login {
  width: 75%;
  padding: 0.75rem;
  background-color: #5563de;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 18px;
  cursor: pointer;
  transition: background 0.3s, transform 0.3s;
}

.btn-login:hover {
  background-color: #3d46b1;
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .input-icon {
    left: 2px;
  }
}
</style>