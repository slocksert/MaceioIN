<template>
  <div class="table-container">
    <table class="user-table">
      <thead>
        <tr>
          <th>Nome</th>
          <th>Usuário</th>
          <th>Setor</th>
          <th>E-mail</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(user, index) in users" :key="index">
          <td>{{ user.name }}</td>
          <td>{{ user.username }}</td>
          <td>{{ user.sector }}</td>
          <td>{{ user.email }}</td>
          <td class="actions">
            <button class="edit-btn" @click="$emit('edit', index)">
              ✏️
            </button>
            <button class="delete-btn" @click="$emit('delete', index)">
              🗑️
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    users: Array
  }
};
</script>

<style scoped>
.table-container {
  width: 100%;
  overflow-x: auto;
}

.user-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.user-table th, .user-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.user-table th {
  background-color: #f8f9fa;
  font-weight: bold;
  text-transform: uppercase;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.actions {
  display: flex;
  gap: 10px;
}

button {
  border: none;
  background: none;
  cursor: pointer;
  font-size: 18px;
}

.edit-btn {
  color: #007bff;
}

.delete-btn {
  color: #dc3545;
}

button:hover {
  opacity: 0.7;
}
</style>
