from fastapi import FastAPI, HTTPException, Request,Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
import subprocess
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from rake import find_unique_similar_entries,df
from validateidea import analyze_business_idea
from news import get_startup_news
from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from searchstartups import get_startup_details
from hotfundingindustries import get_industry_suggestions
from improvemtstomyidea import process_idea
from hottrendingindustries import trending_industries
from fastapi.responses import JSONResponse
from recentlyfundedstartups import recently_funded_startups
from expertanalysis import get_investment_analysis 
from fastapi.templating import Jinja2Templates
from news import get_startup_news  # Importing the function from news.py
from fastapi.responses import HTMLResponse
from news import get_startup_news
from searchstartups import get_startup_details
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.responses import JSONResponse, PlainTextResponse
from startupresources import get_startup_resources




app = FastAPI()

# MongoDB connection setup
uri = "mongodb+srv://Tushar:password12345@capstone.sm6ii.mongodb.net/"
client = MongoClient(uri)
db = client["capstone_data"]
collection = db["user_data"]

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; specify your frontend URL here in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Define the request body model for idea generation
class IdeaRequest(BaseModel):
    industry: str
    description: str

# Endpoint to generate startup ideas
@app.post("/generate-ideas/")
async def generate_ideas(request: IdeaRequest):
    industry = request.industry
    description = request.description

    # Modify the command according to your Python environment if needed
    result = subprocess.run(
        ["python", "genai.py", industry, description],
        capture_output=True,
        text=True
    )

    # Return the result from the genai.py script
    if result.returncode == 0:
        return {"ideas": result.stdout.strip().splitlines()}  # Split lines for a cleaner response
    else:
        return {"error": "An error occurred while generating ideas"}

@app.post("/signup")
async def signup(request: Request):
    data = await request.json()
    username = data["username"]
    email = data["email"]
    password = data["password"]

    # Check if the user already exists
    if collection.find_one({"username": username}):
        raise HTTPException(status_code=400, detail="Username already exists")

    collection.insert_one(data)
    return {"message": "success"}

@app.post("/login")
async def login(request: Request):
    data = await request.json()
    username = data["username"]
    password = data["password"]

    user = collection.find_one({"username": username, "password": password})
    if user:
        return {"message": "User found", "user_type": user.get("describe", "Unknown")}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@app.post("/details")
async def details(request: Request):
    data = await request.json()
    email = data["email"]
    user_describe = data["describe"]
    profession = data["profession"]
    expertise = data["expertise"]
    industries = data["industries"]

    update_data = {
        "describe": user_describe,
        "profession": profession,
        "expertise": expertise,
        "industries": industries
    }

    result = collection.update_one(
        {"email": email},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "Updated details"}

# Define a simple root endpoint for health check
@app.get("/")
async def read_root():
    return {"message": "Welcome to the API"}

@app.post("/get_startup_details/")
async def get_startup_details(request: Request):
    data = await request.json()
    startup_name = data.get("startup_name")
    
    # Replace this with actual logic to retrieve startup details
    return {"details": f"Details for startup: {startup_name}"}




class StartupIdea(BaseModel):
    idea: str

# API endpoint to handle the search request
@app.post("/find_similar_startups/")
async def find_similar_startups(data: StartupIdea):
    description = data.idea
    similar_startups = find_unique_similar_entries(description, df)
    return {"results": similar_startups}
# Start the FastAPI app using `uvicorn` command:

    

class IdeaRequest(BaseModel):
    idea: str

# Define FastAPI endpoint to analyze business idea
@app.post("/validate_business_idea/")
async def analyze_idea(request: IdeaRequest):
    try:
        # Call the function from validateidea.py to analyze the idea
        analysis = analyze_business_idea(request.idea)
        return {"analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


class SkillsInput(BaseModel):
    founder_skills: str

# Define the endpoint to get industry suggestions
@app.post("/suggest_industries/")
async def suggest_industries(skills_input: SkillsInput):
    try:
        # Get the industry suggestions from hotfundingindustries.py
        analysis = await get_industry_suggestions(skills_input.founder_skills)
        return {"analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    

# Define a Pydantic model for input validation
class IdeaRequest(BaseModel):
    idea: str

@app.post("/improve_business_idea/")
async def validate_business_idea(request: IdeaRequest):
    # Extract the idea from the request
    startup_idea = request.idea

    # Call the imported function
    try:
        analysis = process_idea(startup_idea)
        return {"analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error processing the idea") from e
    

@app.get("/trending_industries/")
async def get_trending_industries():
    try:
        content = await trending_industries()
        return JSONResponse(content={"content": content})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)





@app.get("/recently_funded_startups/")
async def get_recently_funded_startups():
    content = await recently_funded_startups()  # Call the LangChain function to get the content
    return JSONResponse(content={"content": content})


# Create a request body model
class CompanyRequest(BaseModel):
    company_name: str

@app.post("/investment_analysis/")
async def investment_analysis(request: CompanyRequest):
    try:
        # Get the company name from the request
        company_name = request.company_name
        # Call the expert analysis function
        analysis = get_investment_analysis(company_name)
        return {"analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


@app.get("/news", response_class=HTMLResponse)
async def news(request: Request):
    # Fetch the latest startup news
    content = get_startup_news()
    return content








@app.get("/")
async def read_root():
    return FileResponse("searchstartups.html")

@app.post("/search")
async def search(startup_name: str = Form(...)):
    try:
        # Get startup details using the provided startup name
        result = await get_startup_details(startup_name)

        # If no result is found, return an error in JSON format
        if result is None or isinstance(result, str) and result == "No content found":
            return PlainTextResponse("No results found", status_code=404)
        
        return PlainTextResponse(result, status_code=200)
    except Exception as e:
        # In case of an exception, return a structured error message
        print(f"Error in API: {str(e)}")
        return PlainTextResponse(f"Error: {str(e)}", status_code=500)
    


@app.get("/", response_class=HTMLResponse)
async def get_html_page():
    with open("resources.html", "r") as f:
        return f.read()

@app.get("/resources", response_class=HTMLResponse)
async def fetch_resources():
    resources = get_startup_resources()
    return resources




file_mapping = {
    'healthcare': 'healthcare.csv',
    'tech': 'tech.csv',
    'finance': 'finance.csv',
    'consumer': 'consumer.csv'
}

@app.post("/search_company")
async def search_company(
    industry: str = Form(...),
    company_name: str = Form(...)
):
    # Validate industry
    if industry.lower() not in file_mapping:
        raise HTTPException(status_code=400, detail=f"Invalid industry: {industry}")
    
    try:
        # Load the corresponding CSV file
        df = pd.read_csv(file_mapping[industry.lower()])
        
        # Search for the company in the CSV file
        company_data = df[df['Organization Name'].str.lower() == company_name.lower()]
        
        # Check if the company is found
        if company_data.empty:
            return {
                "result": f"Company '{company_name}' not found in {industry} industry."
            }
        else:
            # Select only 'Organization Name' and 'success' columns
            filtered_data = company_data[['Organization Name', 'success']]
            
            # Convert the filtered data to a readable format
            result_str = "Company Data:\n" + filtered_data.to_string(index=False)
            return {"result": result_str}
            
    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail=f"File {file_mapping[industry.lower()]} not found!"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred: {str(e)}"
        )






# from fastapi import FastAPI, Form, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# import pandas as pd

# from fastapi import FastAPI, HTTPException, Request, Form
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from pymongo import MongoClient
# import subprocess
# from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
# from fastapi.templating import Jinja2Templates
# from startupresources import get_startup_resources  # Assuming this is a function in startupresources.py
# from searchstartups import get_startup_details
# from rake import find_unique_similar_entries, df
# from validateidea import analyze_business_idea
# from hotfundingindustries import get_industry_suggestions
# from improvemtstomyidea import process_idea
# from hottrendingindustries import trending_industries
# from recentlyfundedstartups import recently_funded_startups
# from expertanalysis import get_investment_analysis
# from news import get_startup_news

# app = FastAPI()

# # MongoDB connection setup
# uri = "mongodb+srv://Tushar:password12345@capstone.sm6ii.mongodb.net/"
# client = MongoClient(uri)
# db = client["capstone_data"]
# collection = db["user_data"]

# # Add CORS Middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins; specify your frontend URL here in production
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all HTTP methods
#     allow_headers=["*"],  # Allows all headers
# )

# # Define the request body model for idea generation
# class IdeaRequest(BaseModel):
#     industry: str
#     description: str

# # Endpoint to generate startup ideas
# @app.post("/generate-ideas/")
# async def generate_ideas(request: IdeaRequest):
#     industry = request.industry
#     description = request.description

#     result = subprocess.run(
#         ["python", "genai.py", industry, description],
#         capture_output=True,
#         text=True
#     )

#     if result.returncode == 0:
#         return {"ideas": result.stdout.strip().splitlines()}
#     else:
#         return {"error": "An error occurred while generating ideas"}

# # User signup and login routes (same as your existing ones)
# @app.post("/signup")
# async def signup(request: Request):
#     data = await request.json()
#     username = data["username"]
#     email = data["email"]
#     password = data["password"]

#     # Check if the user already exists
#     if collection.find_one({"username": username}):
#         raise HTTPException(status_code=400, detail="Username already exists")

#     collection.insert_one(data)
#     return {"message": "success"}

# @app.post("/login")
# async def login(request: Request):
#     data = await request.json()
#     username = data["username"]
#     password = data["password"]

#     user = collection.find_one({"username": username, "password": password})
#     if user:
#         return {"message": "User found", "user_type": user.get("describe", "Unknown")}
#     else:
#         raise HTTPException(status_code=401, detail="Invalid username or password")

# # Fetch startup resources from startupresources.py
# @app.get("/resources", response_class=HTMLResponse)
# async def fetch_resources():
#     try:
#         resources = get_startup_resources()  # This function should return resources
#         return {"resources": resources}
#     except Exception as e:
#         print(f"Error: {e}")  # Log the error on the backend for debugging
#         raise HTTPException(status_code=500, detail=f"Error fetching resources: {str(e)}")
    


# # Fetching latest startup news (assuming news.py is set up)
# @app.get("/news", response_class=HTMLResponse)
# async def news(request: Request):
#     content = get_startup_news()
#     return content

# # Fetch recently funded startups
# @app.get("/recently_funded_startups/")
# async def get_recently_funded_startups():
#     content = await recently_funded_startups()
#     return JSONResponse(content={"content": content})

# # API endpoint to analyze business idea
# @app.post("/validate_business_idea/")
# async def analyze_idea(request: IdeaRequest):
#     try:
#         analysis = analyze_business_idea(request.idea)
#         return {"analysis": analysis}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # Handle trending industries
# @app.get("/trending_industries/")
# async def get_trending_industries():
#     try:
#         content = await trending_industries()
#         return JSONResponse(content={"content": content})
#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)

# # API endpoint to handle the search request
# @app.post("/find_similar_startups/")
# async def find_similar_startups(data: IdeaRequest):
#     description = data.idea
#     similar_startups = find_unique_similar_entries(description, df)
#     return {"results": similar_startups}

# # API endpoint to validate business idea and process it
# @app.post("/improve_business_idea/")
# async def validate_business_idea(request: IdeaRequest):
#     try:
#         analysis = process_idea(request.idea)
#         return {"analysis": analysis}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Error processing the idea") from e

# # API endpoint to analyze investment analysis for startups
# @app.post("/investment_analysis/")
# async def investment_analysis(request: IdeaRequest):
#     try:
#         company_name = request.idea
#         analysis = get_investment_analysis(company_name)
#         return {"analysis": analysis}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # Root endpoint for health check
# @app.get("/")
# async def read_root():
#     return HTMLResponse(content="<h1>Welcome to the API</h1>")








# file_mapping = {
#     'healthcare': 'healthcare.csv',
#     'tech': 'tech.csv',
#     'finance': 'finance.csv',
#     'consumer': 'consumer.csv'
# }

# @app.post("/search_company")
# async def search_company(
#     industry: str = Form(...),
#     company_name: str = Form(...)
# ):
#     # Validate industry
#     if industry.lower() not in file_mapping:
#         raise HTTPException(status_code=400, detail=f"Invalid industry: {industry}")
    
#     try:
#         # Load the corresponding CSV file
#         df = pd.read_csv(file_mapping[industry.lower()])
        
#         # Search for the company in the CSV file
#         company_data = df[df['Organization Name'].str.lower() == company_name.lower()]
        
#         # Check if the company is found
#         if company_data.empty:
#             return {
#                 "result": f"Company '{company_name}' not found in {industry} industry."
#             }
#         else:
#             # Convert the company data to a readable format
            
#             result_str = "Company Data:\n" + company_data.to_string(index=False)
#             return {"result": result_str}
            
#     except FileNotFoundError:
#         raise HTTPException(
#             status_code=404,
#             detail=f"File {file_mapping[industry.lower()]} not found!"
#         )
#     except Exception as e:
#         raise HTTPException(
#             status_code=500,
#             detail=f"An error occurred: {str(e)}"
#         )
