<template>
    <div class="register">
      <h2>Register</h2>
      <form @submit.prevent="register">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <button type="submit">Register</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'UserRegister',
    data() {
      return {
        username: '',
        password: '',
        email: ''
      };
    },
    methods: {
      register() {
        // Implement registration logic here
        this.$router.push('/login');
      }
    }
  };
  </script>
  
  <style scoped>
  .register {
    max-width: 300px;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  .register h2 {
    margin-bottom: 20px;
  }
  
  .register form div {
    margin-bottom: 10px;
  }
  
  .register label {
    display: block;
    margin-bottom: 5px;
  }
  
  .register input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  
  .register button {
    width: 100%;
    padding: 10px;
    background-color: #007BFF;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .register button:hover {
    background-color: #0056b3;
  }
  </style>