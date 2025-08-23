import React from "react";
import { usePlayers } from "../hooks/usePlayers";
import PlayerCard from "../components/PlayerCard";

export default function HomePage() {
    const { players, loading, error } = usePlayers();

    return (
        <div className="min-h-screen bg-gradient-to-br from-blue-900 via-indigo-800 to-purple-900 flex flex-col items-center justify-center py-8">
            <div className="bg-white/90 rounded-2xl shadow-2xl p-10 max-w-lg w-full text-center mb-8">
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
            <div className="w-full max-w-4xl grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                {loading ? (
                    <div className="col-span-full text-white text-xl">Loading players...</div>
                ) : error ? (
                    <div className="col-span-full text-red-200 text-xl bg-red-700/80 rounded-lg p-4">
                        Could not load player data. Please try again later.
                    </div>
                ) : (
                    players.map((player) => (
                        <PlayerCard key={player.id} player={player} />
                    ))
                )}
            </div>
        </div>
    );
}