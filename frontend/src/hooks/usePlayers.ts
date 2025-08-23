import { useEffect, useState } from "react";

const API_BASE_URL = 'http://localhost:8000';

export interface Player {
  id: number;
  web_name: string;
  first_name?: string;
  second_name?: string;
  position?: string;
  team_id?: number;
  now_cost?: number;
  selected_by_percent?: number;
  total_points?: number;
}

export function usePlayers() {
  const [players, setPlayers] = useState<Player[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch(`${API_BASE_URL}/players`)
      .then((res) => {
        if (!res.ok) throw new Error("API error");
        return res.json();
      })
      .then(setPlayers)
      .catch(() => setError("Failed to fetch players"))
      .finally(() => setLoading(false));
  }, []);

  return { players, loading, error };
}