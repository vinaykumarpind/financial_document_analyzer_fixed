Financial Document Analyzer – Debugged & Refactored

Project Overview

This project is a refactored and debugged version of a CrewAI-based financial document analysis system.

The original repository contained:

Deterministic runtime bugs

Unsafe and misleading prompt instructions

Improper agent configuration

Broken PDF parsing logic

Weak output structuring

This submission fixes those issues and improves reliability, determinism, and responsible AI behavior.

Deterministic Bugs Identified & Fixed
1. Undefined LLM Initialization
Original code used:
llm = llm

This caused immediate runtime failure.
Fixed by properly initializing the LLM using ChatOpenAI with controlled temperature.

2. Incorrect Tool Parameter
Original agents used:
tool=[...]
CrewAI requires:
tools=[...]

This was corrected to ensure proper tool binding.

3. FastAPI Function Name Collision
The API endpoint function name conflicted with the imported task object, overwriting it at runtime.
Renamed the endpoint and properly aliased the task import.

4. File Path Not Passed to Crew
The uploaded PDF path was never passed into crew.kickoff().
Fixed by passing file_path explicitly through inputs.

5. Broken PDF Loader
The original implementation referenced an undefined Pdf class.
Replaced with PyPDFLoader from langchain-community for reliable document parsing.

6. Async / Structural Mismatches
Removed unnecessary async usage and unused imports to ensure cleaner execution flow.

Prompt Engineering Improvements
The original prompts intentionally instructed the model to:
Fabricate financial advice
Generate fake URLs
Hallucinate market risks
Contradict itself
Ignore user queries
Provide unsafe investment recommendations
These were replaced with:
Evidence-based financial analysis
Strict reliance on document content
Structured JSON output format
Deterministic behavior (low temperature)
Responsible investment guidance
Proper document verification logic
This significantly reduces hallucination risk and improves production reliability.

Architectural Improvements
Enforced structured JSON outputs for downstream parsing
Reduced agent memory for deterministic behavior
Disabled unnecessary delegation
Added proper file validation
Improved separation of concerns (API / Agent / Task / Tool)

Setup Instructions
1. Install Dependencies
pip install -r requirements.txt

2. Create Environment File
Create a .env file:
OPENAI_API_KEY=your_api_key_here

3. Run API
uvicorn main:app --reload
