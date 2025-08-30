import React, { useState, useMemo } from "react";
import { usePlayers } from "../hooks/usePlayers";
import PlayersTable from "../components/PlayerTablePage/PlayerTable";
import FilterBar from "../components/PlayerTablePage/FilterBar";
import { useNavigate } from "react-router-dom";

// Dummy teams list for dropdown, replace with real data if available
const teams = [
    { id: 1, name: "Arsenal" },
    { id: 2, name: "Aston Villa" },
    { id: 3, name: "Bournemouth" },
    // ...add all teams...
];

export default function HomePage() {
    const { players, loading, error } = usePlayers();
    const navigate = useNavigate();

    const [filters, setFilters] = useState({
        position: "",
        team_id: "",
        total_points: "",
        pointsComp: ">=",
        now_cost: "",
        costComp: ">=",
        selected_by_percent: "",
        selectedComp: ">=",
        player_code: "",
    });

    const columns = [
        {
            name: "Name",
            selector: (row: any) => row.web_name,
            sortable: true,
            grow: 2,
        },
        {
            name: "Position",
            selector: (row: any) => row.position,
            sortable: true,
        },
        {
            name: "Team",
            selector: (row: any) => row.team_id,
            sortable: true,
        },
        {
            name: "Points",
            selector: (row: any) => row.total_points,
            sortable: true,
        },
        {
            name: "Cost",
            selector: (row: any) => row.now_cost ? row.now_cost/10 : "N/A",
            sortable: true,
        },
        {
            name: "Selected %",
            selector: (row: any) => row.selected_by_percent ?? 0,
            sortable: true,
        },
    ];

    // Filtering logic with comparisons
    const filteredPlayers = useMemo(() => {
        return players.filter((player: any) => {
            const points = Number(filters.total_points);
            const cost = Number(filters.now_cost);
            const selected = Number(filters.selected_by_percent);

            let pointsOk = true, costOk = true, selectedOk = true;

            if (filters.total_points !== "") {
                if (filters.pointsComp === ">=") pointsOk = player.total_points >= points;
                else if (filters.pointsComp === "<=") pointsOk = player.total_points <= points;
                else pointsOk = player.total_points === points;
            }
            if (filters.now_cost !== "") {
                if (filters.costComp === ">=") costOk = player.now_cost >= cost;
                else if (filters.costComp === "<=") costOk = player.now_cost <= cost;
                else costOk = player.now_cost === cost;
            }
            if (filters.selected_by_percent !== "") {
                if (filters.selectedComp === ">=") selectedOk = player.selected_by_percent >= selected;
                else if (filters.selectedComp === "<=") selectedOk = player.selected_by_percent <= selected;
                else selectedOk = player.selected_by_percent === selected;
            }

            return (
                (filters.position === "" || String(player.position) === filters.position) &&
                (filters.team_id === "" || String(player.team_id) === filters.team_id) &&
                pointsOk &&
                costOk &&
                selectedOk &&
                (filters.player_code === "" || String(player.player_code).includes(filters.player_code))
            );
        });
    }, [players, filters]);

    const handleRowClicked = (row: any) => {
        navigate(`/player/${row.id}`);
    };

    return (
        <div className="w-full">
            <FilterBar filters={filters} setFilters={setFilters} teams={teams} />
            <PlayersTable
                columns={columns}
                players={filteredPlayers}
                loading={loading}
                error={error}
                onRowClicked={handleRowClicked}
            />
        </div>
    );
}