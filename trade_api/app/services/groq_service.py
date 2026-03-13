from groq import Groq
from app.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def analyze_market(sector, data):

    prompt = f"""
Analyze Indian {sector} sector.

Market Data:
{data}

Generate a markdown report with:

# Market Overview
# Current Trends
# Trade Opportunities
# Risks
# Conclusion
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Groq Error: {str(e)}"