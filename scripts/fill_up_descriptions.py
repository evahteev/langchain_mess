import json
import os

import openai
from typing import Dict

# Initialize OpenAI API (replace with your actual LLM initialization)
openai.api_key = os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "sk-*")


async def trigger_llm(prompt: str) -> str:
    # Trigger the LLM using the Chat API and get the generated description
    # Replace this with your actual LLM API call
    model_engine = "gpt-4"  # Change to your preferred model
    user_message = {
        "role": "system",
        "content": "You are a helpful assistant that generates Public API documentation descriptions."
                   " All API Endpoints there were created are to serve Block Explorer pages and available publicly. "
    }
    assistant_message = {
        "role": "user",
        "content": prompt
    }
    conversation = [user_message, assistant_message]

    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=conversation
    )

    return response['choices'][0]['message']['content'].strip()


def generate_llm_prompts(queries_metadata: Dict) -> Dict:
    llm_prompts = {}

    for query_id, query_data in queries_metadata.items():
        name = query_data.get("name", "Unnamed Query")
        sql = query_data.get("SQL", "No SQL provided")
        parameters = query_data.get("parameters", [])
        visualizations = query_data.get("visualizations", [])

        # Generate the LLM prompt for this query
        prompt = f"""Based on the given query metadata, generate an API documentation description. The metadata for query {name} includes:
- SQL: "{sql}"
- Parameters: {', '.join([param.get('name', 'Unnamed Parameter') + ' (' + param.get('type', 'Unknown Type') + ')' for param in parameters])}
- Visualizations: {', '.join(visualizations)}

Provide a detailed description that includes:
1. The purpose of the query.
2. What parameters are expected and their types.
3. Outputs produced.
4. Visualizations which were created that make sense dont generate any description on TABLE Visualizations.

Format the description in a way that is suitable for API documentation. No Formating/StylingAllowed
The description should be between 250-500 characters long."""

        llm_prompts[query_id] = prompt

    return llm_prompts


async def main():
    # Read queries metadata from JSON file
    with open("queries_metadata.json", 'r') as f:
        queries_metadata = json.load(f)

    # Generate LLM prompts
    generated_prompts = generate_llm_prompts(queries_metadata)

    descriptions_dict = {}
    # Trigger LLM and get generated descriptions
    for query_id, prompt in generated_prompts.items():
        description = await trigger_llm(prompt)
        print(f"Generated API documentation description for Query {query_id}:\n{description}\n")
        descriptions_dict[query_id] = description

    # Save descriptions to JSON file
    with open("descriptions.json", 'w') as f:
        json.dump(descriptions_dict, f, indent=4)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
