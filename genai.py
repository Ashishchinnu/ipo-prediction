# import os
# from langchain_google_genai import ChatGoogleGenerativeAI

# # Set the Google API key
# os.environ["GOOGLE_API_KEY"] = 


# # Initialize the model
# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# # Use try-except block for the print statement
# try:
#    print(llm.invoke("Sing a ballad of LangChain."))
    
# except Exception as e:
#     print(f"An error occurred: {e}")


# from langchain_groq import ChatGroq
# llm = ChatGroq(
#     temperature=0.1,
#     model_name="llama-3.1-70b-versatile",
#     groq_api_key="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"

# )
# response=llm.invoke("2+2")
# print(response.content)

# genai.py
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

# Define the prompt using the industry and description inputs
prompt = (
    f"Imagine you are a startup expert. Given the industry '{industry}' "
    f"and description '{description}', come up with 5 amazing startup ideas related to it. "
    "Give me an elevator pitch for each."
)

# Generate response from the model
try:
    response = llm.invoke(prompt)
    print(response.content)  # Output ideas as text
except Exception as e:
    print("An error occurred:", e)









# from langchain_core.prompts import PromptTemplate

# prompt_template = PromptTemplate.from_template(
#     "Tell me a {adjective} joke about {content}."
# )

# prompt_template.format(adjective="funny", content="chickens")


# import os
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import PromptTemplate


# # Set your Google API key
# os.environ["GOOGLE_API_KEY"] = 'AIzaSyAI8IJHQR2xNjD9b-nplFiPHSwTMTrRd1M'

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

# # Example usage
# industry = "healthcare"
# details = "telemedicine solutions"
# generate_startup_ideas(industry, details)
