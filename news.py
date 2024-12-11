# news.py
from langchain_groq import ChatGroq

# Initialize the language model
llm = ChatGroq(
    temperature=0.1,
    model_name="llama-3.1-70b-versatile",
    groq_api_key="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"
)

def get_startup_news():
    """
    Fetches the latest news about startup finance and topics relevant to startup founders.
    """
    prompt = "Provide the latest news on startup finance and any topics relevant to startup founders."
    response = llm.invoke(prompt)
    print(response.content)
    # Check if the response contains content
    # if hasattr(response, 'content') and response.content:
    return response.content
    # else:
    #     return "No news available at the moment."
