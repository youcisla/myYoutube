import axios from 'axios';

const getVideos = async () => {
    const token = localStorage.getItem('token');
    try {
        const response = await axios.get('http://127.0.0.1:8000/videos', {
            headers: {
                Authorization: `Bearer ${token}`, // Add token here
            },
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching videos:', error);
        throw error;
    }
};

export default getVideos;
