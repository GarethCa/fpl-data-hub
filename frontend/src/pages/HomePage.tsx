import React from "react";

export default function HomePage() {
    return (
        <div className="min-h-screen bg-gradient-to-br from-blue-900 via-indigo-800 to-purple-900 flex items-center justify-center">
            <div className="bg-white/90 rounded-2xl shadow-2xl p-10 max-w-lg w-full text-center">
                <h1 className="text-4xl font-extrabold text-indigo-700 mb-4 drop-shadow">
                    Fantasy Premier League Hub
                </h1>
                <p className="text-lg text-gray-700 mb-6">
                    Welcome to your all-in-one FPL data explorer.<br />
                    Sync, analyze, and visualize Fantasy Premier League stats with ease.
                </p>
                <a
                    href="https://fantasy.premierleague.com/"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-block px-6 py-3 bg-indigo-600 text-white font-semibold rounded-lg shadow hover:bg-indigo-700 transition"
                >
                    Visit Official FPL Site
                </a>
            </div>
        </div>
    );
}