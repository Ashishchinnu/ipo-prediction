from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from langchain_groq import ChatGroq
import os

# Initialize the ChatGroq model
llm = ChatGroq(
    temperature=0.1,
    model_name="llama-3.1-70b-versatile",
    groq_api_key="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"
)

# Define function to get startup news
def get_startup_news():
    prompt = "Provide the latest news on startup finance and any topics relevant to startup founders."
    response = llm.invoke(prompt)

    # Check and log the response to verify content
    if hasattr(response, 'content') and response.content:
        print("News content fetched successfully:", response.content)  # Debug line
        return response.content
    else:
        print("No news content fetched.")  # Debug line
        return "No news available at the moment."

# Initialize the FastAPI app
app = FastAPI()

# Define the route for the homepage
@app.get("/", response_class=HTMLResponse)
async def read_news():
    # Fetch the startup news
    news_content = get_startup_news()

    # Read the static NEWS.html file
    file_path = "news.html"
    with open(file_path, "r") as file:
        html_content = file.read()

    # Replace the placeholder {{ content }} with the dynamic news content
    html_content = html_content.replace("{{ content }}", news_content)

    # Return the updated HTML content with news
    return HTMLResponse(content=html_content)

# Run the app using Uvicorn
# Run the following command to start the app: uvicorn main:app --reload
