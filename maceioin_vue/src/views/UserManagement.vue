<template>
    <div class="user-management">
      <h2>Cadastro de Pessoas</h2>
      <form @submit.prevent="addUser">
        <div>
          <label for="name">Nome:</label>
          <input type="text" id="name" v-model="newUser.name" required />
        </div>
        <div>
          <label for="sector">Setor:</label>
          <select id="sector" v-model="newUser.sector" required>
            <option>Contabilidade</option>
            <option>Financeiro</option>
            <option>Atendimento</option>
            <option>Orçamento</option>
            <option>TI</option>
          </select>
        </div>
        <div>
          <label for="email">E-mail:</label>
          <input type="email" id="email" v-model="newUser.email" required />
        </div>
        <button type="submit">Adicionar</button>
      </form>
      <table>
        <thead>
          <tr>
            <th>Nome</th>
            <th>Setor</th>
            <th>E-mail</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(user, index) in users" :key="index">
            <td>{{ user.name }}</td>
            <td>{{ user.sector }}</td>
            <td>{{ user.email }}</td>
            <td>
              <button @click="editUser(index)">Editar</button>
              <button @click="deleteUser(index)">Excluir</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        newUser: {
          name: '',
          sector: '',
          email: ''
        },
        users: []
      };
    },
    methods: {
      addUser() {
        this.users.push({ ...this.newUser });
        this.newUser.name = '';
        this.newUser.sector = '';
        this.newUser.email = '';
      },
      editUser(index) {
        const user = this.users[index];
        this.newUser = { ...user };
        this.users.splice(index, 1);
      },
      deleteUser(index) {
        this.users.splice(index, 1);
      }
    }
  };
  </script>
  
  <style scoped>
  .user-management {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  .user-management h2 {
    margin-bottom: 20px;
  }
  
  .user-management form div {
    margin-bottom: 10px;
  }
  
  .user-management label {
    display: block;
    margin-bottom: 5px;
  }
  
  .user-management input,
  .user-management select {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  
  .user-management button {
    padding: 10px;
    background-color: #007BFF;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .user-management button:hover {
    background-color: #0056b3;
  }
  
  .user-management table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  
  .user-management table th,
  .user-management table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  
  .user-management table th {
    background-color: #007BFF;
    color: #fff;
  }
  </style>