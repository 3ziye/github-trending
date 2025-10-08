# Google AI Mode Scraper

[![Oxylabs promo code](https://github.com/oxylabs/google-ai-mode-scraper/blob/main/ScraperAPI%2BGoogleAI-1090x275px.png)](https://oxylabs.io/products/scraper-api/serp/google-ai-mode?utm_source=877&utm_medium=affiliate&utm_campaign=llm_scrapers&groupid=877&utm_content=google-ai-mode-scraper-github&transaction_id=102f49063ab94276ae8f116d224b67)

[![](https://dcbadge.limes.pink/api/server/Pds3gBmKMH?style=for-the-badge&theme=discord)](https://discord.gg/Pds3gBmKMH) [![YouTube](https://img.shields.io/badge/YouTube-Oxylabs-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@oxylabs)

[Google AI Mode scraper](https://oxylabs.io/products/scraper-api/serp/google-ai-mode) lets you send prompts and reliably extract AI responses at scale without blocks. Built on the [Web Scraper API](https://oxylabs.io/products/scraper-api/web), it delivers parsed data in JSON format while handling proxies, headless browsers, and anti-bot systems for you. You can use scraped Google AI Mode data to power SEO and GEO projects, build training datasets, or support other data tasks.

## How it works

Scrape Google AI Mode responses by sending a POST request with your prompt and authentication credentials. See the Python example below, or explore more language samples [here](https://github.com/oxylabs/google-ai-mode-scraper/tree/3e23bc41979eeb78326e9bd9d02b743aa371efb1/Code%20examples).

> [!TIP]
> Get a **free trial** by registering on the [dashboard](https://dashboard.oxylabs.io/).

### Request sample (Python)
First, install the requests library in your Python environment:

```bash
pip install requests
```

Then, create the following `.py` file. Make sure to use your Web Scraper API `USERNAME` and `PASSWORD`:

```python
import json
import requests


# API parameters.
payload = {
    'source': 'google_ai_mode',
    'query': 'best health trackers under $200',
    'render': 'html',
    'parse': True,
    'geo_location': 'United States'
}

# Get a response.
response = requests.post(
    'https://realtime.oxylabs.io/v1/queries',
    # Replace with your credentials.
    auth=('USERNAME', 'PASSWORD'),
    json=payload,
)

# Print the response to stdout.
print(response.json())

# Save the response to a JSON file.
with open('response.json', 'w') as file:
    json.dump(response.json(), file, indent=2)
```

### Request parameters

| Parameter | Description | Default Value |
| :---- | :---- | :---- |
| `source` (mandatory) | Sets the scraper. | `google_ai_mode` |
| `query` (mandatory) | The prompt or question to submit to Google AI Mode. Cannot exceed 400 characters. | – |
| `render` (mandatory) | Setting to `html` is required for this source. | – |
| `parse` | Returns parsed data when set to `true`. | `false` |
| `geo_location` | Specify a country to send the prompt from. [More info](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/features/localization/proxy-location). | - |
| `callback_url` | URL to your callback endpoint. [More info](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/push-pull#callback). | – |

Check out [documentation](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/targets/google/ai-mode) to learn more.

### Output samples
#### JSON example
Below is a trimmed JSON output sample. See the full JSON output [here](https://github.com/oxylabs/google-ai-mode-scraper/blob/3e23bc41979eeb78326e9bd9d02b743aa371efb1/output-sample.json).

```json
{
  "results": [
    {
      "content": {
        "links": [
          {
            "url": "https://www.tomsguide.com/best-picks/best-cheap-fitness-trackers",
            "text": "We've tested the best cheap fitness trackers available right now"
          },
          {
            "url": "https://www.garagegymreviews.com/best-budget-fitness-tracker",
            "text": "Expert-Tested: Best Budget Fitness Tracker (2025)"
          },
          {"url": "...", "text": "..."}
        ],
        "prompt": "best health trackers under $200",
        "citations": [
          {
            "url": "https://www.garagegymreviews.com/best-budget-fitness-tracker",
            "text": "For the best health trackers under $200, the top contenders are the Fitbit Charge 6 , Fitbit Inspire 3 , and..."
          },
          {
            "url": "https://www.techradar.com/best/best-cheap-fitness-trackers",
            "text": "For the best health trackers under $200, the top contenders are the Fitbit Charge 6 , Fitbit Inspire 3 , and..."
          },
          {"url": "...", "text": "..."}
        ],
        "response_text": "For the best health trackers under $200, the top contenders are the Fitbit Charge 6 , Fitbit Inspire 3 , and...",
        "parse_status_code": 12000
      },
      "created_at": "2025-09-03 10:13:11",
      "updated_at": "2025-09-03 10:13:26",
      "page": 1,
      "url": "https://www.google.com/search?udm=50&q=best+health+trackers+under+$200&uule=w+CAIQICINdW5pdGVkIHN0YXRlc