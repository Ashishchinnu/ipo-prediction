from langchain_groq import ChatGroq

# Initialize the language model with the specified parameters
llm = ChatGroq(
    temperature=0.1,
    model_name="llama-3.1-70b-versatile",
    groq_api_key="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"
)

def get_investment_analysis(company_name: str) -> str:
    prompt = f"""
    I am considering investing in {company_name} and would like your expert opinion on whether this is a good investment. 
    Please provide a detailed analysis based on the following factors:

    Financial Health:
    - Evaluate the company’s revenue growth, profitability, and key financial ratios (e.g., P/E ratio, debt-to-equity ratio, operating margin).
    - Assess its cash flow and liquidity position. Is the company financially stable, and does it have the resources to weather potential downturns?

    Growth Potential:
    - Analyze the company's market position and its ability to scale. Does it have a strong competitive advantage?
    - How does it perform in its sector, and what is its potential for future expansion?
    - Consider any new products, services, or geographic markets that could drive growth.

    Industry Trends:
    - What is the outlook for the industry in which the company operates? Are there any emerging trends or technological shifts that could affect its future performance?
    - How well is the company positioned to capitalize on these trends compared to its competitors?

    Management and Leadership:
    - Review the experience and track record of the company’s leadership team. Do they have a history of delivering results and making sound strategic decisions?
    - What is the company’s corporate governance structure like?

    Risks:
    - Identify any potential risks, such as market volatility, regulatory challenges, competition, or operational weaknesses.
    - Are there any red flags or concerns that investors should be aware of?

    Valuation:
    - Is the company’s current valuation reasonable? How does its stock price compare to its historical performance and industry benchmarks?

    Based on your analysis of these factors, please provide a recommendation on whether this is a good investment. Explain the reasons for your decision, highlighting the most critical elements influencing your conclusion.
    """
    
    try:
        # Get the response from the language model
        response = llm.invoke(prompt)
        content = response.content  # Directly access the 'content' attribute of the response
        return content
    except Exception as e:
        return f"An error occurred: {e}"
