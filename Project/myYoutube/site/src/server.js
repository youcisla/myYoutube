// server.js
const express = require('express');
const cors = require('cors');

const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors());

// Define API routes
app.post('/user/1/video', (req, res) => {
    // Add your video upload handling logic here
    res.status(200).send('Video uploaded successfully!');
});

// Start server
const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
