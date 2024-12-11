from langchain_groq import ChatGroq

# Initialize the language model with the specified parameters
llm = ChatGroq(
    temperature=0.1,
    model_name="llama-3.1-70b-versatile",
    groq_api_key="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"
)

# Function to get detailed startup information
async def get_startup_details(startup_name: str):
    prompt = (
        f"I am interested in learning about '{startup_name}'. Please provide detailed information covering the following aspects:\n\n"
        "Overview: Describe the company's mission, founding date, and key industry.\n"
        "Founders and Key Team Members: Share information on the founders, their backgrounds, and any prominent team members.\n"
        "Product/Service: Explain what products or services the startup offers, their target audience, and how they address market needs.\n"
        "Market and Competition: Analyze the startup's position in the market, its competitors, and any unique competitive advantages it might have.\n"
        "Funding: List the funding rounds it has gone through, key investors, total amount raised, and valuation, if available.\n"
        "Business Model and Revenue: Describe the business model (e.g., subscription, freemium, B2B, B2C) and any known details on revenue streams or pricing.\n"
        "Milestones and Growth: Outline major achievements, growth metrics (such as user numbers, market reach), and notable partnerships.\n"
        "Challenges and Risks: Highlight any challenges the startup faces, such as regulatory, technical, or market-related issues.\n"
        "Future Plans: Summarize the company's vision, upcoming projects, or expansions that they have publicly shared.\n\n"
        "Please make sure to include the latest data available, and let me know if some information is not accessible."
    )

    response = await llm.ainvoke(prompt)  # Use ainvoke instead of invoke
    
    # Ensure the response is a string or a JSON-like object
    if hasattr(response, 'content'):
        return response.content
    else:
        return "No content found"
