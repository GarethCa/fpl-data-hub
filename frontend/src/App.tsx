import React from "react";
import { Routes, Route, useLocation } from "react-router-dom";
import SideBar from "./components/Sidebar";
import HomePage from "./pages/HomePage";
import PlayerDetailPage from "./pages/PlayerDetailPage";

export default function App() {
    const location = useLocation();

    return (
        <div className="min-h-screen min-w-full bg-white flex-0 flex-row">
            <SideBar />
            <div className="flex-1 items-center min-w-full min-h-screen pl-30 pt-5 pr-10">
                <Routes location={location}>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/player/:player_id" element={<PlayerDetailPage />} />
                </Routes>
            </div>
        </div>
    );
}