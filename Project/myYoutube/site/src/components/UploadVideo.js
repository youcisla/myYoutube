import axios from "axios";
import React, { useState } from "react";

const UploadVideo = () => {
    const [videoFile, setVideoFile] = useState(null);
    const [uploadStatus, setUploadStatus] = useState("");

    const handleFileChange = (e) => {
        setVideoFile(e.target.files[0]);
    };

    const handleUpload = async (e) => {
        e.preventDefault();

        if (!videoFile) {
            setUploadStatus("Please select a video file.");
            return;
        }

        const token = localStorage.getItem("authToken");
        if (!token) {
            setUploadStatus("You need to be logged in to upload a video.");
            return;
        }

        const formData = new FormData();
        formData.append("video", videoFile);

        try {
            const response = await axios.post(
                "http://127.0.0.1:8000/upload-video/",
                formData,
                {
                    headers: {
                        Authorization: `Token ${token}`,
                        "Content-Type": "multipart/form-data",
                    },
                }
            );
            setUploadStatus("Video uploaded successfully!");
        } catch (error) {
            console.error("Error uploading video:", error.response?.data || error.message);
            setUploadStatus("Failed to upload video. Please try again.");
        }
    };

    return (
        <div>
            <h2>Upload Video</h2>
            <form onSubmit={handleUpload}>
                <input type="file" onChange={handleFileChange} accept="video/*" />
                <button type="submit">Upload Video</button>
            </form>
            <p>{uploadStatus}</p>
        </div>
    );
};

export default UploadVideo;
