import React from "react";

interface FilterBarProps {
    filters: any;
    setFilters: (f: any) => void;
    teams: { id: number; name: string }[];
}

export default function FilterBar({ filters, setFilters, teams }: FilterBarProps) {
    return (
        <div className="flex flex-wrap gap-4 mb-4 bg-gray-50 p-4 rounded shadow items-end">
            {/* Position */}
            <div>
                <label className="block text-xs mb-1">Position</label>
                <select
                    className="border rounded px-2 py-1"
                    value={filters.position}
                    onChange={e => setFilters((f: any) => ({ ...f, position: e.target.value }))}
                >
                    <option value="">All</option>
                    <option value="1">Goalkeeper</option>
                    <option value="2">Defender</option>
                    <option value="3">Midfielder</option>
                    <option value="4">Forward</option>
                </select>
            </div>
            {/* Team (multi-select) */}
            <div>
                <label className="block text-xs mb-1">Team</label>
                <select
                    className="border rounded px-2 py-1"
                    value={filters.team_id}
                    onChange={e => setFilters((f: any) => ({ ...f, team_id: e.target.value }))}
                >
                    <option value="">All</option>
                    {teams.map(team => (
                        <option key={team.id} value={team.id}>{team.name}</option>
                    ))}
                </select>
            </div>
            {/* Points */}
            <div>
                <label className="block text-xs mb-1">Points</label>
                <div className="flex gap-1">
                    <select
                        className="border rounded px-1 py-1"
                        value={filters.pointsComp || ">="}
                        onChange={e => setFilters((f: any) => ({ ...f, pointsComp: e.target.value }))}
                    >
                        <option value=">=">&ge;</option>
                        <option value="<=">&le;</option>
                        <option value="=">=</option>
                    </select>
                    <input
                        className="border rounded px-2 py-1 w-20"
                        type="number"
                        placeholder="Points"
                        value={filters.total_points}
                        onChange={e => setFilters((f: any) => ({ ...f, total_points: e.target.value }))}
                    />
                </div>
            </div>
            {/* Cost */}
            <div>
                <label className="block text-xs mb-1">Cost (£m)</label>
                <div className="flex gap-1">
                    <select
                        className="border rounded px-1 py-1"
                        value={filters.costComp || ">="}
                        onChange={e => setFilters((f: any) => ({ ...f, costComp: e.target.value }))}
                    >
                        <option value=">=">&ge;</option>
                        <option value="<=">&le;</option>
                        <option value="=">=</option>
                    </select>
                    <input
                        className="border rounded px-2 py-1 w-20"
                        type="number"
                        placeholder="Cost"
                        value={filters.now_cost}
                        onChange={e => setFilters((f: any) => ({ ...f, now_cost: e.target.value }))}
                    />
                </div>
            </div>
            {/* Selected % */}
            <div>
                <label className="block text-xs mb-1">Selected %</label>
                <div className="flex gap-1">
                    <select
                        className="border rounded px-1 py-1"
                        value={filters.selectedComp || ">="}
                        onChange={e => setFilters((f: any) => ({ ...f, selectedComp: e.target.value }))}
                    >
                        <option value=">=">&ge;</option>
                        <option value="<=">&le;</option>
                        <option value="=">=</option>
                    </select>
                    <input
                        className="border rounded px-2 py-1 w-20"
                        type="number"
                        placeholder="%"
                        value={filters.selected_by_percent}
                        onChange={e => setFilters((f: any) => ({ ...f, selected_by_percent: e.target.value }))}
                    />
                </div>
            </div>
        </div>
    );
}