import pandas as pd

# Function to read the CSV file and search for the company
def search_company(industry, company_name):
    # Map industry to the corresponding CSV file
    file_mapping = {
        'healthcare': 'healthcare.csv',
        'tech': 'tech.csv',  # Add more industries as needed
        'finance': 'finance.csv',
        'consumer':'consumer.csv'
    }

    # Check if the industry is valid
    if industry not in file_mapping:
        print(f"Invalid industry: {industry}")
        return

    # Load the corresponding CSV file
    try:
        df = pd.read_csv(file_mapping[industry])
    except FileNotFoundError:
        print(f"File {file_mapping[industry]} not found!")
        return

    # Search for the company in the CSV file
    company_data = df[df['Organization Name'].str.lower() == company_name.lower()]

    # Check if the company is found
    if company_data.empty:
        print(f"Company '{company_name}' not found in {industry} industry.")
    else:
        # Display the company data with column names
        print(f"Company Data for '{company_name}':")
        print(company_data.to_string(index=False))

# Input: industry and company name
industry = input("Enter the industry (e.g., healthcare, tech, finance): ").lower()
company_name = input("Enter the company name: ")

# Call the function to search for the company
search_company(industry, company_name)
