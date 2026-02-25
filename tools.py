import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()




class FinancialDocumentTool:

    @staticmethod
    def read_data_tool(file_path: str):
        """
        Reads and extracts text from a PDF financial document.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        loader = PyPDFLoader(file_path)
        documents = loader.load()

        full_report = ""

        for doc in documents:
            content = doc.page_content.strip()
            full_report += content + "\n"

        return full_report




class InvestmentTool:

    @staticmethod
    def analyze_investment_tool(financial_document_data: str):
        """
        Placeholder for structured investment analysis.
        """
        return "Investment analysis logic to be implemented."




class RiskTool:

    @staticmethod
    def create_risk_assessment_tool(financial_document_data: str):
        """
        Placeholder for structured risk assessment.
        """
        return "Risk assessment logic to be implemented."