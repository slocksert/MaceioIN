import axios from 'axios';

export async function deleteUser(userId) {
  try {
    const response = await axios.delete(`http://localhost:8000/delete/${userId}/`, {
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