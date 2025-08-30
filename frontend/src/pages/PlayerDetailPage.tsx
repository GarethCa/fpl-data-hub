import React from "react";
import { useParams, useNavigate } from "react-router-dom";
import { usePlayerDetail } from "../hooks/getPlayerDetail";

export default function PlayerDetailPage() {
    const { player_id } = useParams<{ player_id: string }>();
    const id = player_id ? parseInt(player_id, 10) : undefined;
    const { player, loading, error } = usePlayerDetail(id as number);
    const navigate = useNavigate();

    // Animation: slide in from right
    // Tailwind: transition-transform, duration-300, translate-x-full -> translate-x-0
    // Parent should have relative/overflow-hidden if needed

    if (loading) return <div className="p-8 text-xl text-indigo-700">Loading player details...</div>;
    if (error) return <div className="p-8 text-xl text-red-700">Error: {error}</div>;
    if (!player) return <div className="p-8 text-xl">No player found.</div>;

    return (
        <div
            className="
                inset-0 bg-white w-full shadow-2xl
                transform transition-transform duration-300
                translate-x-0
                md:rounded-l-2xl md:right-0 md:left-auto
                overflow-y-auto
            "
        >
            <button
                onClick={() => navigate(-1)}
                className="absolute top-4 left-4 px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700 transition"
            >
                ← Back
            </button>
            <div className="p-8 pt-16">
                <h1 className="text-3xl font-bold mb-4">
                    {player.web_name} ({player.first_name} {player.second_name})
                </h1>
                <div className="mb-2">Position: {player.position}</div>
                <div className="mb-2">Team ID: {player.team_id}</div>
                <div className="mb-2">Cost: £{(player.now_cost / 10).toFixed(1)}m</div>
                <div className="mb-2">Selected By: {player.selected_by_percent}%</div>
                <div className="mb-2">Total Points: {player.total_points}</div>
                <div className="mb-2">Player Code: {player.player_code}</div>
                <h2 className="text-2xl font-semibold mt-8 mb-2">Stats</h2>
                <pre className="bg-gray-100 rounded p-4 overflow-x-auto text-sm">
                    {JSON.stringify(player.stats, null, 2)}
                </pre>
            </div>
        </div>
    );
}