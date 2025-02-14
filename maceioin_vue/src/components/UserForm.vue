<template>
  <form @submit.prevent="handleSubmit" class="user-form">
    <div>
      <label for="name">Nome:</label>
      <input type="text" id="name" v-model="localUser.name" required />
    </div>
    <div>
      <label for="sector">Setor:</label>
      <select id="sector" v-model="localUser.sector" required>
        <option>Contabilidade</option>
        <option>Financeiro</option>
        <option>Atendimento</option>
        <option>Orçamento</option>
        <option>TI</option>
      </select>
    </div>
    <div>
      <label for="email">E-mail:</label>
      <input type="email" id="email" v-model="localUser.email" required />
    </div>
    <button type="submit">{{ buttonText }}</button>
  </form>
</template>

<script>
export default {
  props: {
    user: Object,
    buttonText: { type: String, default: "Adicionar" }
  },
  data() {
    return {
      localUser: { ...this.user }
    };
  },
  watch: {
    user: {
      handler(newVal) {
        this.localUser = { ...newVal };
      },
      deep: true
    }
  },
  methods: {
    handleSubmit() {
      this.$emit("submit", this.localUser);
      this.localUser = { name: '', username: '', sector: '', email: '' };
    }
  }
};
</script>

<style scoped>
.user-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.user-form label {
  font-weight: bold;
}
.user-form input, .user-form select {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  width: 100%;
}
.user-form button {
  padding: 10px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.user-form button:hover {
  background-color: #0056b3;
}
</style>