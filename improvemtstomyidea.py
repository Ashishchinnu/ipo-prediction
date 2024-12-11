
# improvementstomyidea.py

from langchain_groq import ChatGroq
import os

# Initialize the language model with specified parameters
llm = ChatGroq(
    temperature=0.1,
    model_name="llama-3.1-70b-versatile",
    groq_api_key="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"
)

def process_idea(idea):
    prompt = f"here is my <idea>{idea}</idea>\n" \
             "Concept Refinement: (Provide suggestions to refine and improve the core idea. This could be in the form of feature additions, targeting a different audience, or pivoting the business model.)\n" \
             "Market Fit: (How can the product be better aligned with market needs? Suggest ways to validate the market fit or gather feedback.)\n" \
             "Competitive Advantage: (Offer strategies to strengthen the startup's competitive edge, such as unique features, partnerships, or pricing models.)\n" \
             "Business Model & Monetization Strategy:\n" \
             "Pricing Strategy: (Suggest pricing models or methods to optimize revenue.)\n" \
             "Revenue Streams: (Offer ideas for additional revenue streams, such as upselling, cross-selling, or new monetization methods.)\n" \
             "Target Audience Suggestions:\n" \
             "Audience Expansion: (Offer ways to broaden or narrow the target audience, based on emerging trends, niche markets, or underserved groups.)\n" \
             "Acquisition Strategies: (Provide suggestions for user acquisition strategies that have worked in similar industries.)\n" \
             "Go-to-Market Strategy:\n" \
             "Brand Positioning: (Offer suggestions on how to position the brand in the market for maximum impact.)\n" \
             "Marketing Channels: (Suggest marketing channels that will work best for your audience, e.g., social media, SEO, partnerships, etc.)\n" \
             "Partnerships: (Provide suggestions for strategic partnerships to help accelerate growth.)\n" \
             "Steps Forward (Roadmap):\n" \
             "Immediate Steps: (What are the first 3 things you need to do within the next 30 days?)\n" \
             "Short-Term Goals (3-6 months): (List milestones to hit within the next 3 to 6 months, e.g., product development, marketing, sales goals.)\n" \
             "Long-Term Vision (6+ months): (Define the key goals for scaling your business and what it will take to achieve them, e.g., expanding to new markets, raising funding.)"

    # Call the `invoke` method to generate responses
    result = llm.invoke(input=prompt)
    
    # Access and return content from the result
    return result.content if hasattr(result, 'content') else 'No content found'
