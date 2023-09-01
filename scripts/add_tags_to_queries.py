import os
import openai
import json

# Initialize OpenAI API
openai.api_key = os.environ.get("OPENAI_API_KEY", "sk-*")

# Load the JSON file containing query descriptions
with open("query_descriptions.json", "r") as f:
    query_descriptions = json.load(f)

# Initialize an empty dictionary to store categorized descriptions
categorized_descriptions = {}

# Function to categorize a description using OpenAI API
def categorize_description(description):
    try:
        # Use OpenAI API to categorize the description
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Categorize and attach tags to the following API description: {description}"
                                        "Assign following tags to query descriptions:"
                                        "\n* Account & Wallet Management: Combines Account Management, Wallet,"
                                        " Token Information, Active Addresses."
                                        "\n* Network & Analytics: Combines Network Analysis, Gas Usage, "
                                        "Transaction Cost, Analytics, Daily Metrics, Top Spenders, "
                                        "Multi-Metrics, Statistical Data, Network Efficiency, Network Monitoring."
                                        "\n* Blockchain & Tokens: Combines Blockchain Network, ERC20 Tokens, "
                                        "Token Transfer, Block Data, Latest Blocks, Historical Data, "
                                        "Gas Fees, Native Tokens, Decentralized Exchange, Chain IDs, ERC-20 Transactions."
                                        "\n* Transaction & Block Explorer: Combines Transaction Details, Warehouse, Transaction Hashes, Block Explorer."
                                        "\n* Smart Contracts & DEX: Combines Smart Contracts, Decentralized Exchange."
                                        f" provide result in json list of strings for each query, say nothing but this json in response stringified"},
        ]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )
        category_str = response['choices'][0]['message']['content'].strip()
        categories = json.loads(category_str)
        return categories
    except Exception as e:
        categories = categorize_description(description)
        if categories != ["Uncategorized"]:
            return categories
        print(f"Error: {e}")
        return ["Uncategorized"]

# Loop through each query description and categorize it
for query_id, description in query_descriptions.items():
    categories = categorize_description(description)
    categorized_descriptions[query_id] = {
        "description": description,
        "categories": categories
    }

# Save the categorized descriptions to a new JSON file
with open("categorized_descriptions.json", "w") as f:
    json.dump(categorized_descriptions, f, indent=4)

print("Categorization complete. Check the 'categorized_descriptions.json' file.")
