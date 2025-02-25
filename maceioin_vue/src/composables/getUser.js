import axios from 'axios';

export async function fetchUsers() {
  try {
    const response = await axios.get('https://djangoapi.slocksert.dev/');
    return response.data;
  } catch (error) {
    console.error('Error fetching users:', error);
    return [];
  }
}