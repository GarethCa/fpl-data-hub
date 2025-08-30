import React from "react";
import { useParams, useNavigate } from "react-router-dom";
import { usePlayerDetail } from "../hooks/getPlayerDetail";

export default function PlayerDetailPage() {
    const { player_id } = useParams<{ player_id: string }>();
    const id = player_id ? parseInt(player_id, 10) : undefined;
    const { player, loading, error } = usePlayerDetail(id as number);
    const navigate = useNavigate();

    if (loading) return <div className="p-8 text-xl text-indigo-700">Loading player details...</div>;
    if (error) return <div className="p-8 text-xl text-red-700">Error: {error}</div>;
    if (!player) return <div className="p-8 text-xl">No player found.</div>;

    // Use the latest stats entry if available
    const stats = player.stats && player.stats.length > 0 ? player.stats[0] : null;

    return (
        <div
            className="
                inset-0 bg-white w-full shadow-2xl
                transform transition-transform duration-300
                translate-x-0
                md:rounded-l-2xl md:right-0 md:left-auto
                pb-10
                flex flex-col md:flex-row gap-8 px-8 pt-16
            "
        >
            <button
                onClick={() => navigate(-1)}
                className="absolute top-4 left-4 px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700 transition"
            >
                ← Back
            </button>
            {/* Player Info Card */}
            <div className="flex-1 bg-white rounded-xl shadow-lg p-6 mb-8 md:mb-0 h-80">
                <div className="bg-gray-50 rounded p-4 shadow">
                    <h1 className="text-3xl font-bold mb-4">
                        {player.first_name} {player.second_name}
                    </h1>
                    <div className="mb-2">Position: {player.position}</div>
                    <div className="mb-2">Team ID: {player.team_id}</div>
                    <div className="mb-2">Cost: £{(player.now_cost / 10).toFixed(1)}m</div>
                    <div className="mb-2">Selected By: {player.selected_by_percent}%</div>
                    <div className="mb-2">Total Points: {player.total_points}</div>
                    <div className="mb-2">Player Code: {player.player_code}</div>
                </div>
            </div>
            {/* Stats Card */}
            <div className="flex-1 bg-white rounded-xl shadow-lg p-6 overflow-x-auto">
                <h2 className="text-2xl font-semibold mb-4">Stats</h2>
                {stats ? (
                    <div className="flex flex-col gap-4">
                        {/* Availability & Status */}
                        <div className="bg-gray-50 rounded p-4 shadow">
                            <div className="font-semibold mb-2">Availability & Status</div>
                            <div>Status: {stats.status}</div>
                            <div>Minutes: {stats.minutes}</div>
                            <div>Chance of Playing Next Round: {stats.chance_of_playing_next_round ?? "N/A"}</div>
                            <div>Chance of Playing This Round: {stats.chance_of_playing_this_round ?? "N/A"}</div>
                            <div>News: {stats.news || "None"}</div>
                        </div>
                        {/* Performance */}
                        <div className="bg-gray-50 rounded p-4 shadow">
                            <div className="font-semibold mb-2">Performance</div>
                            <div>Goals Scored: {stats.goals_scored}</div>
                            <div>Assists: {stats.assists}</div>
                            <div>Clean Sheets: {stats.clean_sheets}</div>
                            <div>Goals Conceded: {stats.goals_conceded}</div>
                            <div>Own Goals: {stats.own_goals}</div>
                            <div>Yellow Cards: {stats.yellow_cards}</div>
                            <div>Red Cards: {stats.red_cards}</div>
                            <div>Penalties Missed: {stats.penalties_missed}</div>
                            <div>Penalties Saved: {stats.penalties_saved}</div>
                            <div>Saves: {stats.saves}</div>
                        </div>
                        {/* Value & Transfers */}
                        <div className="bg-gray-50 rounded p-4 shadow">
                            <div className="font-semibold mb-2">Value & Transfers</div>
                            <div>Cost Change (Event): {stats.cost_change_event}</div>
                            <div>Cost Change (Event Fall): {stats.cost_change_event_fall}</div>
                            <div>Cost Change (Start): {stats.cost_change_start}</div>
                            <div>Cost Change (Start Fall): {stats.cost_change_start_fall}</div>
                            <div>Transfers In: {stats.transfers_in}</div>
                            <div>Transfers In (Event): {stats.transfers_in_event}</div>
                            <div>Transfers Out: {stats.transfers_out}</div>
                            <div>Transfers Out (Event): {stats.transfers_out_event}</div>
                        </div>
                        {/* Advanced Stats */}
                        <div className="bg-gray-50 rounded p-4 shadow">
                            <div className="font-semibold mb-2">Advanced Stats</div>
                            <div>Influence: {stats.influence}</div>
                            <div>Creativity: {stats.creativity}</div>
                            <div>Threat: {stats.threat}</div>
                            <div>ICT Index: {stats.ict_index}</div>
                            <div>Bonus: {stats.bonus}</div>
                            <div>BPS: {stats.bps}</div>
                            <div>Form: {stats.form}</div>
                            <div>Points Per Game: {stats.points_per_game}</div>
                            <div>Event Points: {stats.event_points}</div>
                            <div>Dreamteam Count: {stats.dreamteam_count}</div>
                            <div>Special: {stats.special ? "Yes" : "No"}</div>
                        </div>
                    </div>
                ) : (
                    <div>No stats available.</div>
                )}
            </div>
        </div>
    );
}