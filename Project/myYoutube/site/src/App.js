import React, { useState } from "react";
import Header from "./components/Header";
import Login from "./components/Login";
import MyVideos from "./components/MyVideos";
import Signup from "./components/Signup";
import UploadVideo from "./components/UploadVideo";

const App = () => {
    const [page, setPage] = useState("login");

    return (
        <div>
            <Header navigate={setPage} />
            {page === "login" && <Login navigate={setPage} />}
            {page === "signup" && <Signup navigate={setPage} />}
            {page === "my-videos" && <MyVideos />}
            {page === "upload-video" && <UploadVideo />}
        </div>
    );
};

export default App;
