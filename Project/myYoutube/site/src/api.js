import axios from 'axios';
const baseURL = "http://127.0.0.1:8000"; // Replace with the actual base URL

axios.defaults.baseURL = 'http://127.0.0.1:8000';

// Fetch all videos
export const fetchVideos = async () => {
    try {
        const response = await fetch(`${baseURL}/videos`);
        const data = await response.json();
        return data.data;
    } catch (error) {
        console.error('Failed to fetch videos', error);
        return [];
    }
};

// Upload a video
export const uploadVideo = async (userId, formData) => {
    try {
        const response = await fetch(`${baseURL}/user/${userId}/video`, {
            method: 'POST',
            body: formData
        });
        return await response.json();
    } catch (error) {
        console.error('Failed to upload video', error);
        throw error;
    }
};

// Delete a video
export const deleteVideo = async (videoId) => {
    try {
        await fetch(`${baseURL}/video/${videoId}`, {
            method: 'DELETE'
        });
    } catch (error) {
        console.error('Failed to delete video', error);
    }
};
