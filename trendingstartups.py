# from langchain_core.prompts import PromptTemplate

# prompt_template = PromptTemplate.from_template(
#     "Tell me a {adjective} joke about {content}."
# )

# prompt_template.format(adjective="funny", content="chickens")


# import os
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import PromptTemplate




# import os
# from langchain_google_genai import ChatGoogleGenerativeAI

# # Set the Google API key
# os.environ["GOOGLE_API_KEY"] = 'your key'

# # Initialize the model
# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# # Use try-except block for the print statement
# try:
#     prompt = (
#         "Give me all the latest news I need as someone who closely watches and follows "
#         "startup finance and companies. I might be thinking of starting my own company. "
#         "Please provide links to these news articles."
#     )
    
#     response = llm.invoke(prompt)
#     content = response.content  # Capture the content
#     print(content)  # Print only the content part

# except Exception as e:
#     print(f"An error occurred: {e}")\








import sys
from langchain_groq import ChatGroq

# Initialize the language model with the specified parameters
llm = ChatGroq(
    temperature=0.1,
    model_name="llama-3.1-70b-versatile",
    groq_api_key="your key"
)

# Get industry and description as arguments
industry = sys.argv[1]
description = sys.argv[2]

# Define the prompt to get the latest news articles
prompt = (
    f"As a close observer of startup finance and companies, I want to stay updated. "
    "Please provide me with the latest news articles that would be valuable for someone "
    "considering starting their own company in the industry '{industry}'. "
    "Include links to these articles and a brief summary of each."
)

# Generate response from the model
try:
    response = llm.invoke(prompt)
    print(response.content)  # Output ideas as text
except Exception as e:
    print("An error occurred:", e)









# # Set your Google API 
# os.environ["GOOGLE_API_KEY"] = 'AIzaSyD4h2BnDgnPGsMNp8K_U-iVY0dUCs91cxk'

# # Initialize the Google Generative AI model
# llm = ChatGoogleGenerativeAI(model="gemini-pro")

# # Define the prompt template for generating startup ideas
# prompt_template = PromptTemplate.from_template(
#     "You are an expert on startups. Give me startup ideas based on {industry} and related to {details}. "
#     "Give me the top 5 ideas you can come up with as well as break each idea down."
# )

# # Function to generate startup ideas
# def generate_startup_ideas(industry, details):
#     # Format the prompt with the provided industry and details
#     prompt = prompt_template.format(industry=industry, details=details)
    
#     # Debug: print the generated prompt
#     print("Generated Prompt:")
#     print(prompt)  # See if the prompt is generated correctly
    
#     # Invoke the language model with the generated prompt
#     try:
#         response = llm.invoke(prompt)
#         # Debug: print the response type
#         print("Response type:", type(response))
        
#         # Check if the response has a text attribute or similar to print
#         if hasattr(response, 'text'):
#             print("Response Text:")
#             print(response.text)  # Attempt to print the response text
#         else:
#             print("Response content:")
#             print(response)  # Print the whole response if text is not available
    
#     except Exception as e:
#         print("Error during invocation:", e)  # Catch and print any errors
