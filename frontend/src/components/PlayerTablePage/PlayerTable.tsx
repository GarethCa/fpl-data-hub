import React, { useRef, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import DataTable from "react-data-table-component";

export default function PlayersTable({ columns, players, loading, error }: any) {
    const rowHeight = 56;
    const headerHeight = 56;
    const padding = 16;
    const [pageSize, setPageSize] = useState(10);
    const [tableKey, setTableKey] = useState(0);
    const containerRef = useRef<HTMLDivElement>(null);
    const navigate = useNavigate();

    // Dynamically set page size based on available height
    useEffect(() => {
        const handleResize = () => {
            const availableHeight = window.innerHeight - headerHeight - padding;
            const rows = Math.floor(availableHeight / rowHeight);
            setPageSize(rows > 0 ? rows : 5);
            setTableKey(prev => prev + 1); // Force DataTable remount
        };
        handleResize();
        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, []);

    const handleRowClicked = (row: any) => {
        navigate(`/player/${row.id}`);
    };

    //TODO: Stop it losing state on resize
    return (
        <div
            ref={containerRef}
            className="w-full bg-white rounded-xl shadow-lg p-6 flex-1 pb-0"
        >
            {loading ? (
                <div className="text-center text-xl text-indigo-700">Loading players...</div>
            ) : error ? (
                <div className="text-center text-red-200 text-xl bg-red-700/80 rounded-lg p-4">
                    Could not load player data. Please try again later.
                </div>
            ) : (
                <div className="w-full">
                    <DataTable
                        key={tableKey}
                        columns={columns}
                        data={players}
                        pagination
                        paginationPerPage={pageSize}
                        paginationRowsPerPageOptions={[pageSize]}
                        highlightOnHover
                        striped
                        responsive
                        onRowClicked={handleRowClicked}
                        progressPending={loading}
                        noDataComponent="No players found"
                        customStyles={{
                            headCells: {
                                style: {
                                    backgroundColor: "#364152",
                                    color: "#e0e7ff",
                                    fontWeight: 700,
                                },
                            },
                            rows: {
                                style: {
                                    fontFamily: "inherit",
                                },
                                highlightOnHoverStyle: {
                                    backgroundColor: "#f1f5fd",
                                    outline: "none",
                                },
                            },
                        }}
                    />
                </div>
            )}
        </div>
    );
}