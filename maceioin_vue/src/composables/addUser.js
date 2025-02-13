import axios from 'axios';

export async function addUser(newUser) {
  try {
    const response = await axios.post('http://localhost:8000/add/', newUser, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    console.log('User added:', response.data);
  } catch (error) {
    console.error('Error adding user:', error);
  }
}