import React from "react";
import { usePlayers } from "../hooks/usePlayers";
import SideBar from "../components/Sidebar";
import PlayersTable from "../components/PlayerTablePage/PlayerTable";
import HomeHeader from "../components/PlayerTablePage/HomeHeader";

export default function HomePage() {
    const { players, loading, error } = usePlayers();

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
            selector: (row: any) => row.now_cost ? `£${(row.now_cost / 10).toFixed(1)}m` : "N/A",
            sortable: true,

        },
        {
            name: "Selected %",
            selector: (row: any) => row.selected_by_percent ?? 0,
            sortable: true,

        },
    ];

    return (
      
            <div >
                <PlayersTable columns={columns} players={players} loading={loading} error={error} />
            </div>
    );
}