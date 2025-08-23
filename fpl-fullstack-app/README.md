pip# Project Title: FPL Fullstack App

## Description
This project is a fullstack application that loads Fantasy Premier League (FPL) data from the FPL API into a local database and serves this information through a React frontend. The application is structured with a Python backend using FastAPI and a React frontend built with Vite.

## Project Structure
```
fpl-fullstack-app
├── README.md
├── .env.example
├── frontend
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── index.html
│   └── src
│       ├── index.tsx
│       ├── App.tsx
│       ├── pages
│       │   └── HomePage.tsx
│       ├── components
│       │   └── Layout.tsx
│       ├── services
│       │   └── api.ts
│       ├── types
│       │   └── index.ts
│       └── styles
│           └── global.css
├── backend
│   ├── requirements.txt
│   └── app
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── api
│       │   ├── __init__.py
│       │   └── routes.py
│       ├── services
│       │   ├── __init__.py
│       │   └── fpl_client.py
│       ├── ingest
│       │   ├── __init__.py
│       │   └── load_fpl_data.py
│       ├── db
│       │   ├── __init__.py
│       │   └── session.py
│       ├── models
│       │   ├── __init__.py
│       │   └── player.py
│       └── schemas
│           ├── __init__.py
│           └── player.py
└── tests
    ├── backend
    │   ├── __init__.py
    │   └── test_players.py
    └── frontend
        └── App.test.tsx
```

## Getting Started

### Prerequisites
- Python 3.x
- Node.js and npm
- A local database (e.g., SQLite, PostgreSQL)

### Installation

1. **Backend Setup**
   - Navigate to the `backend` directory.
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

2. **Frontend Setup**
   - Navigate to the `frontend` directory.
   - Install the required npm packages:
     ```
     npm install
     ```

### Running the Application

1. **Start the Backend**
   - In the `backend` directory, run:
     ```
     uvicorn app.main:app --reload
     ```

2. **Start the Frontend**
   - In the `frontend` directory, run:
     ```
     npm run dev
     ```

### Usage
- Access the frontend application at `http://localhost:3000`.
- The backend API can be accessed at `http://localhost:8000`.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.