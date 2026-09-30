from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI(title="FitBuddy AI")

# Configure Gemini - Add your API Key here
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

class UserInput(BaseModel):
    age: int
    weight: float
    height: float
    goal: str
    level: str

@app.get("/")
def home():
    return {"message": "FitBuddy AI is Running!"}

@app.post("/generate-plan")
def generate_plan(user: UserInput):
    prompt = f"""
    Create a personalized fitness plan:
    Age: {user.age}, Weight: {user.weight}kg, Height: {user.height}cm
    Goal: {user.goal}, Fitness Level: {user.level}
    Give workout plan for 7 days and diet plan.
    """
    response = model.generate_content(prompt)
    return {"plan": response.text}
