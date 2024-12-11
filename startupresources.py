# startupresources.py
from langchain_groq import ChatGroq

# Initialize the language model
llm = ChatGroq(
    temperature=0.1,
    model_name="llama-3.1-70b-versatile",
    groq_api_key="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"
)

def get_startup_resources():
    """
    Fetches comprehensive advice, resources, and guidance on entrepreneurship for new founders.
    """
    prompt = """
    I am thinking of becoming an entrepreneur and starting my own business. Please provide comprehensive advice, resources, and guidance covering the following aspects:

    Initial Steps for Starting a Business:
    - What are the essential first steps to take when starting a business?
    - How can I evaluate whether my business idea is viable?
    - What are some common mistakes new entrepreneurs make, and how can I avoid them?

    Business Idea Development:
    - How do I refine my business idea to ensure it’s unique and has potential in the market?
    - What tools or frameworks can help me test my business concept?

    Market Research and Validation:
    - How can I conduct market research for my startup?
    - What are some ways to validate if there is demand for my product/service?

    Business Plan and Strategy:
    - How do I write a business plan? What key components should it include?
    - What are some strategic approaches I should consider when launching my business?

    Legal and Financial Setup:
    - What legal structure should I choose for my business (LLC, sole proprietorship, corporation)?
    - What are the key legal considerations and licenses I might need?
    - How do I handle business taxes and accounting?

    Funding Your Startup:
    - What are the different ways to fund a startup (bootstrapping, venture capital, crowdfunding)?
    - What should I know about seeking investors and preparing a pitch?
    - How do I determine how much capital I need to raise?

    Building a Team:
    - How do I recruit the right team for my startup?
    - What roles are essential to start with, and how do I manage a small team effectively?

    Marketing and Branding:
    - How do I create a brand identity and market my business effectively, especially with a limited budget?
    - What are some cost-effective digital marketing strategies for startups?
    - How do I build an online presence and engage with customers?

    Growth and Scaling:
    - How do I grow my startup beyond the initial phase?
    - What are some strategies for scaling operations and expanding to new markets?

    Tools and Resources:
    - What are some essential tools and resources for entrepreneurs (productivity, marketing, finances)?
    - Can you recommend any websites, books, or online courses that can help me learn more about entrepreneurship?

    Challenges and Risks:
    - What are the major challenges new entrepreneurs face and how can I prepare for them?
    - How do I assess and manage business risks?

    Long-term Vision and Exit Strategy:
    - What are some key factors to consider when planning for the long-term growth of my business?
    - What exit strategies should I think about in the future (selling the business, IPO, etc.)?
    """
    response = llm.invoke(prompt)
    return response.content
