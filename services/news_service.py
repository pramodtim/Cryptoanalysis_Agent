import feedparser
from datetime import datetime, timezone, timedelta

CRYPTO_RSS_FEEDS = [
    "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "https://cointelegraph.com/rss",
    "https://decrypt.co/feed"
]

MAX_AGE_HOURS = 36


def is_recent(entry) -> bool:
    if not hasattr(entry, "published_parsed"):
        return False

    published = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
    age = datetime.now(timezone.utc) - published
    return age <= timedelta(hours=MAX_AGE_HOURS)


def fetch_crypto_news(limit_per_source: int = 5):
    articles = []

    for feed_url in CRYPTO_RSS_FEEDS:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            if not is_recent(entry):
                continue

            articles.append({
                "source": feed.feed.get("title", "Unknown"),
                "title": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "published": entry.get("published", "unknown")
            })

    return articles[:limit_per_source * len(CRYPTO_RSS_FEEDS)]
