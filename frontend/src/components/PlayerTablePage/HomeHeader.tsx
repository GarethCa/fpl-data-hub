import React from "react";

export default function HomeHeader() {
    return (
        <div className="bg-white/90 rounded-2xl shadow-2xl p-2 max-w-4xl w-full text-center mb-2">
            <h1 className="text-4xl font-extrabold text-gray-700 mb-4 drop-shadow">
                Fantasy Premier League Hub
            </h1>
            <p className="text-lg text-gray-700 mb-6">
                Welcome to your all-in-one FPL data explorer.<br />
                Sync, analyze, and visualize Fantasy Premier League stats with ease.
            </p>
        </div>
    );
}