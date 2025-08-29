import React from "react";
import { useNavigate } from "react-router-dom";
import DataTable from "react-data-table-component";

export default function PlayersTable({ columns, players, loading, error }: any) {
    // Calculate page size based on viewport height (approximate row height: 56px, header: 56px, padding: 32px)
    const rowHeight = 56;
    const headerHeight = 56;
    const padding = 16;
    const [pageSize, setPageSize] = React.useState(10);
    const [tableKey, setTableKey] = React.useState(0);
    const navigate = useNavigate();

    React.useEffect(() => {
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
    return (
        <div className="max-w-8xl bg-white rounded-xl shadow-lg p-6 flex-1 pb-0">
            {loading ? (
                <div className="text-center text-xl text-indigo-700">Loading players...</div>
            ) : error ? (
                <div className="text-center text-red-200 text-xl bg-red-700/80 rounded-lg p-4">
                    Could not load player data. Please try again later.
                </div>
            ) : (
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
            )}
        </div>
    );
}