
import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from IPython.display import Markdown, display
from openai import OpenAI


load_dotenv(override=True)
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    print("No API key found. Please check your .env file.")
elif not google_api_key.startswith("sk-proj-"):
    print("API key found, but format looks wrong. Should start with 'sk-proj-'.")
elif google_api_key.strip() != google_api_key:
    print("API key contains extra spaces. Remove leading/trailing whitespace.")
else:
    print("API key found and valid!")

# Configure Gemini client
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

# Define prompts
system_prompt = """
You are a sharp-witted, sarcastic, snarky assistant who summarizes website content.
Ignore navigation, menus, ads, and layout fluff.
Focus only on the meaningful text.

Your summary should be:
- Concise but witty
- Written in clean, well-structured Markdown
- Slightly sarcastic, but still informative
- Able to detect and summarize news/announcements if present

Absolutely do NOT wrap your Markdown in code blocks.
Your output **must** be raw markdown.
"""

user_prompt_prefix = """
Here are the raw text contents of a website.
Write a short, structured Markdown summary with humor and attitude.

### Requirements:
- Keep it short but insightful.
- Use headings, bullets, and bold text where useful.
- If the site includes announcements or news, give a short section for that.
- Ignore navigation menus, cookie popups, ads, and unrelated UI text.

Website contents:
"""
# Helper functions
def messages_for(website_text: str):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website_text}
    ]

# Main summarization function
def summarize(url: str):
    print(f"Fetching contents from: {url}")
    website_text = fetch_website_contents(url)

    response = gemini.chat.completions.create(
        model="gemini-2.5-flash",
        messages=messages_for(website_text)
    )
    return response.choices[0].message.content

# Display function
def display_summary(url: str):
    summary_markdown = summarize(url)
    display(Markdown(summary_markdown))

display_summary("https://www.nationalgeographic.com") 
