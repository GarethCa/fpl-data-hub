from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.routes.load import router as load_router
from app.routes.player import router as player_router

app = FastAPI()

# CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API router
app.include_router(api_router)
app.include_router(load_router)
app.include_router(player_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Fantasy Premier League API!"}
