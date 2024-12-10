import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${localStorage.getItem('token')}`, // Ensure token is stored in localStorage
    },
});

const fetchVideos = async () => {
    try {
        const response = await axiosInstance.get('/my-videos/');
        setVideos(response.data);
    } catch (error) {
        console.error('Error fetching videos:', error);
        alert('Failed to fetch videos');
    }
};


export default axiosInstance;
