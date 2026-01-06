from services.news_service import fetch_crypto_news
from services.analysis_service import analyze_crypto_news
from services.post_service import generate_social_posts

def run_crypto_agent():
    news = fetch_crypto_news()

    if not news:
        return {"error": "No news fetched"}

    analysis = analyze_crypto_news(news)
    posts = generate_social_posts(analysis)

    return {
        "news_used": news[:5],
        "analysis": analysis,
        "posts": posts
    }
