import axios from 'axios';
import React, { useState } from 'react';
import axiosInstance from '../api/axiosInstance';

const UploadVideo = () => {
    const [videoFile, setVideoFile] = useState(null);

    const handleFileChange = (e) => {
        setVideoFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!videoFile) return;

        const formData = new FormData();
        formData.append('video', videoFile);

        try {
            const response = await axiosInstance.post('/user/1/video', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log('Video uploaded:', response.data);
        } catch (error) {
            console.error('Error uploading video:', error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="file" accept="video/*" onChange={handleFileChange} />
                <button type="submit">Upload</button>
            </form>
        </div>
    );
};

export default UploadVideo;

const handleUpload = async () => {
    try {
        const response = await axios.post('/user/1/video', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        console.log('Video uploaded:', response.data);
    } catch (error) {
        console.error('Error uploading video:', error.message);
    }
};