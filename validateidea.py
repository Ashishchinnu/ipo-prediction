import re
from langchain_groq import ChatGroq

# Initialize the language model
llm = ChatGroq(
    temperature=0.1,
    model_name="llama-3.1-70b-versatile",
    groq_api_key="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"
)

# Define the prompt template
prompt = """
I am starting a new business idea and would like feedback on its feasibility, market potential, and overall strengths and weaknesses. Here is the idea:

<idea>

Please analyze the idea from a business perspective, including:

Market demand: Is there a clear need for this product or service? Who would be the target customers?
Competition: Who are the competitors, and how does this idea compare to what's already available in the market?
Revenue potential: What revenue streams could this idea generate, and how scalable is the business model?
Challenges: What are the potential obstacles or risks in executing this idea?
Growth potential: How could the business expand or diversify over time?
Provide a thorough assessment of the strengths and weaknesses of the concept and any recommendations for improvement.
"""

# Function to analyze the business idea
def analyze_business_idea(idea):
    # Replace the <idea> placeholder with the actual business idea
    formatted_prompt = prompt.replace("<idea>", idea)
    
    # Generate response using the `invoke` method
    response = llm.invoke([formatted_prompt])
    
    # Extract only the content part of the response using regex
    response_str = str(response)  # Convert response to a string
    match = re.search(r'content="(.+?)" additional_kwargs', response_str, re.DOTALL)
    if match:
        analysis = match.group(1)  # Extract the content part
        
        # Replace **text** with <strong>text</strong> for bold formatting
        analysis = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', analysis)
        
        # Replace \n with <br> for line breaks
        analysis = analysis.replace('\n', '<br>')
        
        
        return analysis
    return "Error: No valid response returned."
