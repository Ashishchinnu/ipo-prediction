# from langchain_groq import ChatGroq

# # Initialize the language model with the specified parameters
# llm = ChatGroq(
#     temperature=0.1,
#     model_name="llama-3.1-70b-versatile",
#     groq_api_key="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"
# )

# def suggest_industries_for_startup(founder_skills):
#     # Prompt with a placeholder for the skills of the founder
#     prompt = f"""
#     Based on current market trends, emerging technologies, and investor interests, suggest the most promising industries for a startup founder to focus on in 2024. 
#     The founder has expertise in {founder_skills}. 
#     Provide a detailed list of industries where these skills are in high demand, where there is significant investor funding, and where startups are likely to thrive. 
#     For each industry, include key trends, growth opportunities, and why it's attracting funding. 
#     Also, suggest actionable next steps for a founder with these skills to build a startup in the chosen industry.
#     """
    
#     # Get the response from the language model using the invoke method
#     try:
#         response = llm.invoke(prompt)
#         content = response.content  # Directly access the 'content' attribute of the response
#         return content
#     except Exception as e:
#         return f"An error occurred: {e}"

# # Example usage
# founder_skills = "software development, AI, and blockchain"
# industries = suggest_industries_for_startup(founder_skills)
# print(industries)


from langchain_groq import ChatGroq
import os

# Initialize the language model with the specified parameters
llm = ChatGroq(
    temperature=0.1,
    model_name="llama-3.1-70b-versatile",
    groq_api_key="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"
)

async def get_industry_suggestions(founder_skills: str) -> str:
    prompt = f"""
    Based on current market trends, emerging technologies, and investor interests, suggest the most promising industries for a startup founder to focus on in 2024. 
    The founder has expertise in {founder_skills}. 
    Provide a detailed list of industries where these skills are in high demand, where there is significant investor funding, and where startups are likely to thrive. 
    For each industry, include key trends, growth opportunities, and why it's attracting funding. 
    Also, suggest actionable next steps for a founder with these skills to build a startup in the chosen industry. keep it precise
    """
    
    # Get the response from the language model
    response = llm.invoke(prompt)
    content = response.content  # Directly access the 'content' attribute of the response
    return content
