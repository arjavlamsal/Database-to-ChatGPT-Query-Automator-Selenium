#without web scraping using chatgpt API
import openai
import pandas as pd

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key'

# Load your spreadsheet data
df = pd.read_excel('your_spreadsheet.xlsx')

# Assuming your product names are in a column named 'Product Name' and descriptions will be stored in a column named 'Description'
product_names = df['Product Name'].tolist()
description_column_index = df.columns.get_loc('Description')

# Function to fetch description using OpenAI's API
def fetch_description(product_name):
    # Define prompt
    prompt = f"Generate a product description for '{product_name}':\n"

    # Call OpenAI's completion API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100
    )

    # Get response description
    description = response.choices[0].text.strip()

    return description

# Loop through each product name and fetch description
for i, product_name in enumerate(product_names):
    # Skip if description already exists
    if pd.notnull(df.iloc[i, description_column_index]):
        continue

    # Fetch description using OpenAI's API
    description = fetch_description(product_name)

    # Update DataFrame with fetched description
    df.iloc[i, description_column_index] = description
    df.to_excel('your_updated_spreadsheet.xlsx', index=False)
