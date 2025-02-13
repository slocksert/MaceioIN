<template>
  <UserManagementHeader />
  <div class="user-management">
    <div class="title-button">
      <h2>Cadastro de Pessoas</h2>
      <button @click="openAddUserModal" class="add-user-btn">
        <Icon icon="akar-icons:plus" class="add-icon" /> Adicionar Usuário
      </button>
    </div>
    
    <UserTable :users="users" @edit="openEditModal" @delete="handleDeleteUser" />

    <UserFormModal :visible="showAddUserModal" :user="newUser" title="Adicionar Usuário" buttonText="Adicionar" @submit="handleAddUser" @close="closeAddUserModal" />
    <UserFormModal :visible="showEditUserModal" :user="editingUser" title="Editar Usuário" buttonText="Salvar" @submit="handleUpdateUser" @close="closeEditModal" />
  </div>
  <PageFooter />
</template>

<script>
import { Icon } from '@iconify/vue';
import UserFormModal from "../components/UserFormModal.vue";
import UserTable from "../components/UserTable.vue";
import UserManagementHeader from "../components/UserManagementHeader.vue";
import PageFooter from "../components/PageFooter.vue";
import { addUser } from "../composables/addUser";
import { editUser } from "../composables/editUser";
import { deleteUser } from "../composables/deleteUser";
import { fetchUsers } from "../composables/getUser";
import { useToast } from 'vue-toastification';

export default {
  components: { Icon, UserFormModal, UserTable, UserManagementHeader, PageFooter },
  data() {
    return {
      newUser: { name: "", username: "", sector: "", email: "" },
      users: [],
      showAddUserModal: false,
      showEditUserModal: false,
      editingUserIndex: null,
      editingUser: { name: "", username: "", sector: "", email: "" },
      lastToastMessage: ''
    };
  },
  methods: {
    openAddUserModal() {
      this.showAddUserModal = true;
    },
    closeAddUserModal() {
      this.showAddUserModal = false;
    },
    async handleAddUser(user) {
      try {
        await addUser(user);
        this.handleFetchUsers();
        this.closeAddUserModal();
        this.showToast('Usuário adicionado com sucesso!');
      } catch (error) {
        this.showToast('Erro ao adicionar usuário.');
      }
    },
    openEditModal(index) {
      this.editingUserIndex = index;
      this.editingUser = { ...this.users[index] };
      this.showEditUserModal = true;
    },
    async handleUpdateUser(updatedUser) {
      try {
        await editUser(this.users[this.editingUserIndex].id, updatedUser);
        this.users.splice(this.editingUserIndex, 1, updatedUser);
        this.closeEditModal();
        this.handleFetchUsers();
        this.showToast('Usuário atualizado com sucesso!');
      } catch (error) {
        this.showToast('Erro ao atualizar usuário.');
      }
    },
    async handleDeleteUser(index) {
      try {
        await deleteUser(this.users[index].id);
        this.handleFetchUsers();
        this.showToast('Usuário deletado com sucesso!');
      } catch (error) {
        this.showToast('Erro ao deletar usuário.');
      }
    },
    closeEditModal() {
      this.showEditUserModal = false;
      this.editingUser = { name: "", username: "", sector: "", email: "" };
    },
    async handleFetchUsers() {
      this.users = await fetchUsers();
    },
    showToast(message) {
      if (this.lastToastMessage !== message) {
        this.toast.success(message);
        this.lastToastMessage = message;
      }
    }
  },
  mounted() {
    this.handleFetchUsers();
  },
  setup() {
    const toast = useToast();
    return { toast };
  }
};
</script>

<style scoped>
.title-button {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.user-management {
  max-width: 700px; 
  margin: 50px auto; 
  padding: 20px;
  background-color: #fff; 
  border-radius: 8px; 
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 { 
  color: #333; 
  text-align: center; 
}

.add-user-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 12px 20px;
  background-color: #4e72e6;
  color: white;
  font-size: 16px;
  font-weight: bold;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.add-user-btn:hover {
  background-color: #354d9b;
}

.add-icon {
  font-size: 1rem;
  margin-right: 8px;
}

@media (max-width: 768px) {
  .user-management{
    margin: 1rem;
    margin-top: 8rem;
}
}
</style>