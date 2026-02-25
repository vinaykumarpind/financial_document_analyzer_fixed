from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document as financial_task

app = FastAPI(title="Financial Document Analyzer")


def run_crew(query: str, file_path: str):
    crew = Crew(
        agents=[financial_analyst],
        tasks=[financial_task],
        process=Process.sequential,
    )

    result = crew.kickoff(
        inputs={
            "query": query,
            "file_path": file_path
        }
    )

    return result


@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}


@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document.")
):

    file_id = str(uuid.uuid4())
    os.makedirs("data", exist_ok=True)
    file_path = f"data/{file_id}_{file.filename}"

    try:
        with open(file_path, "wb") as f:
            f.write(await file.read())

        if not query:
            query = "Analyze this financial document."

        response = run_crew(query=query.strip(), file_path=file_path)

        return {
            "status": "success",
            "file_processed": file.filename,
            "analysis": response
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing document: {str(e)}"
        )

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
