import React, { useState } from "react";
import { uploadVideo } from "../api";

const UploadVideo = () => {
    const [videoFile, setVideoFile] = useState(null);
    const [videoName, setVideoName] = useState("");

    const handleUpload = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("name", videoName);
        formData.append("source", videoFile);

        try {
            const response = await uploadVideo(formData);
            alert(`Video uploaded: ${response.data.name}`);
        } catch (error) {
            console.error("Upload failed", error);
        }
    };

    return (
        <form onSubmit={handleUpload}>
            <h2>Upload a Video</h2>
            <input
                type="text"
                placeholder="Video Name"
                value={videoName}
                onChange={(e) => setVideoName(e.target.value)}
                required
            />
            <input
                type="file"
                onChange={(e) => setVideoFile(e.target.files[0])}
                accept="video/*"
                required
            />
            <button type="submit">Upload</button>
        </form>
    );
};

export default UploadVideo;
