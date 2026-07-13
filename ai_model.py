import os
from dotenv import load_dotenv

from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

load_dotenv()

API_KEY = os.getenv("L4DS7Qc9yUqPQ61C0j4YTPdgYJkkVi74AbowGmoBxUns")
PROJECT_ID = os.getenv("546073c5-30e0-4511-b820-72778ab57cd3")
URL = os.getenv("URL")
MODEL_ID = os.getenv("MODEL_ID")

credentials = Credentials(
    url=URL,
    api_key=API_KEY
)

parameters = {
    GenParams.MAX_NEW_TOKENS: 300,
    GenParams.TEMPERATURE: 0.7,
    GenParams.TOP_P: 0.9
}

model = ModelInference(
    model_id=MODEL_ID,
    credentials=credentials,
    project_id=PROJECT_ID,
    params=parameters
)

def get_ai_plan(name, age, gender, bmi, goal):

    prompt = f"""
You are an expert AI Fitness Coach.

Create a personalized fitness plan.

Name: {name}
Age: {age}
Gender: {gender}
BMI: {bmi}
Goal: {goal}

Provide:

1. Weekly Workout Plan (Monday to Sunday)
2. Healthy Diet Plan
3. Daily Water Intake
4. Daily Calories Recommendation
5. Motivational Quote
6. One Health Tip

Keep the response neat and easy to read.
"""

    return model.generate_text(prompt=prompt)