from crewai import Task
from agents import financial_analyst
from tools import FinancialDocumentTool

# Main Financial Analysis Task
analyze_financial_document = Task(
    description="""
    Analyze the financial document located at {file_path}.

    Carefully extract and summarize:
    - Revenue
    - Expenses
    - Net Profit or Loss
    - Key financial ratios (if available)
    - Growth trends
    - Key financial observations

    Base your response strictly on the document content.
    Do not fabricate information.
    If data is missing, clearly state it.
    """,

    expected_output="""
    Return structured JSON:

    {
        "revenue": "",
        "expenses": "",
        "net_profit": "",
        "financial_ratios": {},
        "growth_trends": [],
        "key_observations": []
    }
    """,

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

)
