import { useEffect, useState } from "react";

const API_BASE_URL = 'http://localhost:8000';

export interface PlayerStats {
  [key: string]: any; // Accept any structure for stats
}

export interface PlayerDetails {
  id: number;
  web_name: string;
  first_name: string;
  second_name: string;
  position: string;
  team_id: number;
  now_cost: number;
  selected_by_percent: number;
  total_points: number;
  player_code: string;
  stats: PlayerStats[];
}

export function usePlayerDetail(playerId: number) {
  const [player, setPlayer] = useState<PlayerDetails | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!playerId) return;
    setLoading(true);
    setError(null);

    fetch(`${API_BASE_URL}/players/${playerId}`)
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch player details");
        return res.json();
      })
      .then((data) => {
        setPlayer(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message || "Unknown error");
        setLoading(false);
      });
  }, [playerId]);

  return { player, loading, error };
}