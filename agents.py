import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_openai import ChatOpenAI
from tools import FinancialDocumentTool

load_dotenv()

# Proper LLM initialization
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2  # Low temperature for deterministic financial outputs
)

# Financial Analyst Agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Provide accurate and evidence-based financial analysis strictly from the provided document.",
    verbose=True,
    memory=False,
    backstory=(
        "You are a professional financial analyst with expertise in financial statements, "
        "risk evaluation, and investment analysis. "
        "You base your conclusions strictly on document content. "
        "You never fabricate data. If information is missing, you clearly state it."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=3,
    allow_delegation=False
)

# Financial Document Verifier
verifier = Agent(
    role="Financial Document Verification Specialist",
    goal="Accurately determine whether the uploaded file is a financial document.",
    verbose=True,
    memory=False,
    backstory=(
        "You are a compliance professional trained to verify financial documents. "
        "You carefully examine content for structured financial data and accounting terminology. "
        "You do not guess or assume."
    ),
    llm=llm,
    max_iter=2,
    allow_delegation=False
)

# Investment Advisor
investment_advisor = Agent(
    role="Conservative Investment Advisor",
    goal="Provide responsible and data-driven investment insights based strictly on analyzed financial data.",
    verbose=True,
    memory=False,
    backstory=(
        "You are a certified financial advisor focused on risk-managed and compliant strategies. "
        "You avoid speculation and clearly explain risks."
    ),
    llm=llm,
    max_iter=3,
    allow_delegation=False
)

# Risk Assessor
risk_assessor = Agent(
    role="Financial Risk Analyst",
    goal="Identify realistic financial risks based on the document content.",
    verbose=True,
    memory=False,
    backstory=(
        "You specialize in assessing liquidity, market, credit, and operational risks objectively. "
        "You avoid exaggeration and focus on evidence."
    ),
    llm=llm,
    max_iter=3,
    allow_delegation=False
)