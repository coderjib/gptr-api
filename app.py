import os
from dotenv import load_dotenv
from fastapi import FastAPI
from gpt_researcher import GPTResearcher

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

@app.get("/report/{report_type}")
async def get_report(query: str, report_type: str):
    researcher = GPTResearcher(query, report_type)
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    return {"report": report}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)