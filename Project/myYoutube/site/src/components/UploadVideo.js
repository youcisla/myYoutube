import React, { useState } from 'react';
import axios from '../api/axiosInstance';

const UploadVideo = () => {
    const [videoFile, setVideoFile] = useState(null);
    const [videoName, setVideoName] = useState('');

    const handleFileChange = (e) => {
        setVideoFile(e.target.files[0]);
    };

    const handleNameChange = (e) => {
        setVideoName(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!videoFile || !videoName) {
            alert('Both name and file are required.');
            return;
        }

        const formData = new FormData();
        formData.append('name', videoName);
        formData.append('source', videoFile);

        try {
            const response = await axios.post('/user/1/video', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log('Video uploaded:', response.data);
        } catch (error) {
            if (error.response) {
                console.error('Server responded with:', error.response.status, error.response.data);
                alert(`Error uploading video: ${error.response.status}`);
            } else if (error.request) {
                console.error('No response received:', error.request);
                alert('Error uploading video: No response from server');
            } else {
                console.error('Error setting up request:', error.message);
                alert('Error uploading video: ' + error.message);
            }
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Video Name"
                    value={videoName}
                    onChange={handleNameChange}
                />
                <input type="file" accept="video/*" onChange={handleFileChange} />
                <button type="submit">Upload</button>
            </form>
        </div>
    );
};

export default UploadVideo;
