from utils.llm_client import get_groq_client
from pathlib import Path

client = get_groq_client()

PROMPT_PATH = Path(__file__).parent.parent / "prompts" / "analysis_prompt.txt"

def analyze_crypto_news(articles: list) -> str:
    news_text = ""
    for i, article in enumerate(articles[:5], start=1):
        news_text += f"{i}. {article['title']}\n{article['summary']}\n\n"

    prompt_template = PROMPT_PATH.read_text()
    prompt = prompt_template.format(news_text=news_text)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
