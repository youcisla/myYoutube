import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);

document.addEventListener('DOMContentLoaded', () => {
    const videoGrid = document.querySelector('.video-grid');
    const addVideoBtn = document.getElementById('add-video-btn');
    const deleteVideoBtn = document.getElementById('delete-video-btn');

    addVideoBtn.addEventListener('click', () => {
        const newVideoCard = document.createElement('article');
        newVideoCard.classList.add('video-card');
        newVideoCard.innerHTML = `
        <h3>New Video</h3>
        <video controls>
          <source src="new-video.mp4" type="video/mp4">
          Your browser does not support the video tag.
        </video>
      `;
        videoGrid.appendChild(newVideoCard);
    });

    deleteVideoBtn.addEventListener('click', () => {
        const lastVideoCard = videoGrid.querySelector('.video-card:last-child');
        if (lastVideoCard) {
            videoGrid.removeChild(lastVideoCard);
        } else {
            alert('No videos left to delete!');
        }
    });
});
