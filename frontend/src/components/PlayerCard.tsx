import React from "react";
import type { Player } from "../hooks/usePlayers";

export default function PlayerCard({ player }: { player: Player }) {
  return (
    <div className="bg-white rounded-xl shadow-lg outline outline-2 outline-indigo-200 hover:outline-indigo-400 transition-all p-5 flex flex-col items-center min-h-[180px]">
      <div className="text-xl font-bold text-indigo-700 mb-1">{player.web_name}</div>
      <div className="text-gray-600 mb-1">{player.first_name} {player.second_name}</div>
      <div className="text-sm text-gray-500 mb-2">Position: {player.position || "N/A"}</div>
      <div className="flex gap-4 text-sm text-gray-700 mb-1">
        <span>Points: <span className="font-semibold">{player.total_points ?? 0}</span></span>
        <span>Cost: <span className="font-semibold">£{player.now_cost ? (player.now_cost / 10).toFixed(1) : "N/A"}m</span></span>
      </div>
      <div className="text-xs text-gray-400">Selected by: {player.selected_by_percent ?? 0}%</div>
    </div>
  );
}