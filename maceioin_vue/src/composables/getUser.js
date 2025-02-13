import axios from 'axios';

export async function fetchUsers() {
  try {
    const response = await axios.get('http://localhost:8000');
    return response.data;
  } catch (error) {
    console.error('Error fetching users:', error);
    return [];
  }
}