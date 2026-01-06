from utils.llm_client import get_groq_client
from pathlib import Path

client = get_groq_client()

PROMPT_PATH = Path(__file__).parent.parent / "prompts" / "post_prompt.txt"

def generate_social_posts(analysis_text: str) -> str:
    prompt_template = PROMPT_PATH.read_text()
    prompt = prompt_template.format(analysis_text=analysis_text)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

