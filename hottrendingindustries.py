# hottrendingindustries.py

from langchain_groq import ChatGroq
import os

# Initialize the language model with the specified parameters
llm = ChatGroq(
    temperature=0.1,
    model_name="llama-3.1-70b-versatile",
    groq_api_key="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"
)

async def trending_industries() -> str:
    prompt = """
    I'm an investor looking to identify the hottest and most promising industries and market segments for investment right now. 
    Please provide an overview of key trends and high-growth areas across sectors, particularly those that show potential for scalability, disruptive technology, and strong future demand. 
    Prioritize industries that are gaining traction with venture capital, have emerging technological innovations, or are being shaped by new consumer behavior and regulatory trends. 
    If possible, include examples of recent successful startups or companies in these areas.
    """
    
    # Get the response from the language model
    response = llm.invoke(prompt)
    content = response.content  # Directly access the 'content' attribute of the response
    return content
