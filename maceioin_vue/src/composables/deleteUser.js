import axios from 'axios';

export async function deleteUser(userId) {
  try {
    const response = await axios.delete(`https://djangoapi.slocksert.dev/delete/${userId}/`, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error deleting user:', error);
    throw error;
  }
}