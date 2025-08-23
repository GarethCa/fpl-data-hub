import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api'; // Adjust the base URL as needed

export const fetchPlayers = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/players`);
        return response.data;
    } catch (error) {
        console.error('Error fetching players:', error);
        throw error;
    }
};

// Add more API functions as needed
