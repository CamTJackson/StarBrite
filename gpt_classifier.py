from openai import OpenAI
from config import MODEL_NAME, TEMPERATURE

client = OpenAI()

def classify_target(prompt):

    response = client.responses.create(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        input=prompt
    )

    return response.output_text
