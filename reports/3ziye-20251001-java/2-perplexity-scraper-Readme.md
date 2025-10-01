# Perplexity Scraper

[![Oxylabs promo code](https://github.com/oxylabs/perplexity-scraper/blob/main/ScraperAPI%2BPerplexity-1090x275px.png)](https://oxylabs.io/products/scraper-api/serp/perplexity?utm_source=877&utm_medium=affiliate&utm_campaign=llm_scrapers&groupid=877&utm_content=perplexity-scraper-github&transaction_id=102f49063ab94276ae8f116d224b67)

[![](https://dcbadge.limes.pink/api/server/Pds3gBmKMH?style=for-the-badge&theme=discord)](https://discord.gg/Pds3gBmKMH) [![YouTube](https://img.shields.io/badge/YouTube-Oxylabs-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@oxylabs)


The [Perplexity Scraper](https://oxylabs.io/products/scraper-api/serp/perplexity) by Oxylabs allows developers to send prompts to Perplexity and automatically collect both AI-generated responses and structured metadata. Instead of just raw HTML, it can also provide results as parsed JSON, website PNG, XHR/Fetch requests, or Markdown output. 

You can use the [Oxylabs’ Web Scraper API](https://oxylabs.io/products/scraper-api) with Perplexity for AI content auditing, research tracking, and analyzing SEO performance. It handles dynamic AI-generated content, fully supports real-time SERP extraction, and integrates seamlessly with Oxylabs' global proxy infrastructure, without the need to manage proxies, browsers, or worry about anti-bot systems.

## How it works

The Perplexity scraper handles the rendering, parsing, and delivery of results in any requested format. You need to provide your prompt, credentials, and a few optional parameters, as shown below.

### Request sample (Python)

```python
import json
import requests

# API parameters.
payload = {
    'source': 'perplexity',
    'prompt': 'top 3 smartphones in 2025, compare pricing across US marketplaces',
    'geo_location': 'United States',
    'parse': True
}

# Get a response.
response = requests.post(
    'https://realtime.oxylabs.io/v1/queries',
    auth=('USERNAME', 'PASSWORD'),
    json=payload
)

# Print response to stdout.
print(response.json())

# Save response to a JSON file.
with open('response.json', 'w') as file:
    json.dump(response.json(), file, indent=2)
```

More request examples in different programming languages are available [here](https://github.com/oxylabs/perplexity-scraper/tree/main/Code%20examples).

**Note:** By default, all requests to Perplexity use JavaScript rendering. Make sure to set a sufficient timeout (e.g. 180s) when using the Realtime integration method.

### Request parameters

| Parameter | Description | Default value |
|-----------|-------------|---------------|
| `source`* | Sets the Perplexity scraper | `perplexity` |
| `prompt`* | The prompt or question to submit to Perplexity. | – |
| `parse` | Returns parsed data when set to true. | `true` |
| `geo_location` | Specify a country to send the prompt from. [More info](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/features/localization/proxy-location). | – |
| `callback_url` | URL to your callback endpoint. [More info](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/push-pull#callback). | – |

\* Mandatory parameters

---

### Output samples

Web Scraper API returns either an HTML document or a JSON object of Perplexity scraper output, which contains structured data from the results page.

**HTML example:**

![HTML Example](image.png)

**Structured JSON output snippet:**

```json
{
    "results": [
        {
            "content": {
                "url": "https://www.perplexity.ai/search/top-3-smartphones-in-2025-comp-wvA0dso7TgW3NpgF8Jd8tg",
                "model": "turbo",
                "top_images": ["url + title"],
                "top_sources": ["url + title + source"],
                "prompt_query": "top 3 smartphones in 2025, compare pricing across US marketplaces",
                "answer_results": ["answer in JSON"],
                "displayed_tabs": [
                    "search",
                    "images",
                    "sources"
                ],
                "related_queries": [                
                    "How do the prices of the top 3 smartphones compare across US marketplaces",
                    "What features make the Galaxy S25 Ultra stand out as the best in 2025",
                    "Why is the Pixel 9a considered a top budget option despite its lower price",
                    "How does the iPhone 16 Pro Max's pricing differ from Samsung and Google models",
                    "What factors should I consider when choosing among these top smartphones in 2025"
                ],
                "answer_results_md": ["answer in Markdown"],
                "parse_status_code": 12000
            },
            "created_at": "2025-07-16 12:14:32",
            "updated_at": "2025-07-16 12:15:28",
            "page": 1,
            "url": "https://www.perplexity.ai/search/top-3-smartphones-in-2025-comp-wvA0dso7TgW3NpgF8Jd8tg",
            "job_id": "7