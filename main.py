from typing import Union
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("SUPABASE_URL or SUPABASE_KEY is not set in .env")

# Initialize Supabase client
supabase: Client = create_client(url, key)

# FastAPI app
app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, restrict to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# ----- Models -----
class LoginRequest(BaseModel):
    email: str
    password: str


class RegisterRequest(BaseModel):
    email: str
    password: str
    username: Union[str, None] = None


# ----- Routes -----
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# ----- Login -----
@app.post("/login")
def login(request: LoginRequest):
    try:
        user = supabase.auth.sign_in_with_password(
            {"email": request.email, "password": request.password}
        )
        if user and user.user:
            return {"message": "Login successful", "user": user.user}
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ----- Register -----
@app.post("/signup")
def register(request: RegisterRequest):
    try:
        user = supabase.auth.sign_up(
            {"email": request.email, "password": request.password}
        )
        return {"message": "User registered successfully", "user": user.user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
