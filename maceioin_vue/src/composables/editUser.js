import axios from 'axios';

export async function editUser(userId, userData) {
  try {
    const response = await axios.patch(`http://localhost:8000/edit/${userId}/`, userData, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error editing user:', error);
    throw error;
  }
}