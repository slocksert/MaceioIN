<template>
    <div v-if="visible" class="modal">
      <div class="modal-content">
        <h3>{{ title }}</h3>
        <div class="button-container">
          <UserForm :user="user" :buttonText="buttonText" @submit="handleSubmit" />
          <button @click="$emit('close')" class="cancel-button">Cancelar</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import UserForm from "./UserForm.vue";
  
  export default {
    components: { UserForm },
    props: {
      visible: Boolean,
      user: Object,
      title: String,
      buttonText: String
    },
    methods: {
      handleSubmit(user) {
        this.$emit('submit', user);
      }
    }
  };
  </script>
  
  <style scoped>
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .modal-content {
    background: white;
    padding: 20px;
    border-radius: 8px;
    width: 400px;
  }
  
  .button-container {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    justify-content: space-between;
    margin-top: 20px;
  }
  
  button {
    padding: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    width: 100%;
  }
  
  .cancel-button {
    background-color: #FF4136;
    color: white;
  }
  
  .cancel-button:hover {
    background-color: #CC322A;
  }
  </style>