from langchain_groq import ChatGroq
import os
import asyncio
# Initialize the language model with the specified parameters
llm = ChatGroq(
    temperature=0.1,
    model_name="llama-3.1-70b-versatile",
    groq_api_key="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"
)

async def recently_funded_startups() -> str:
    prompt = """
    Provide a detailed list of hot new startups that have recently acquired significant funding. 
    Include the following details for each startup:
    - Company name
    - Industry or sector
    -funding rounds
    -main investors
   
    - Brief description of the startup and its product or service
    - Geographic location (if available)
    

    Focus on startups that have been funded within the last 6 months. Include only startups in high-growth sectors like technology, AI, healthcare, green energy, fintech, and other emerging industries. Prioritize companies with innovative ideas, strong market potential, and high growth rates.If You have no insights available tell what is the latest that u can access
    """

    # Get the response from the language model
    response = llm.invoke(prompt)
    content = response.content  # Directly access the 'content' attribute of the response
    print(content)
    return content
if __name__ == "__main__":
    asyncio.run(recently_funded_startups())