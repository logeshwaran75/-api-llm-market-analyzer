import requests


def search_sector(sector):

    try:

        url = f"https://newsapi.org/v2/everything?q={sector}&pageSize=5&apiKey=demo"

        response = requests.get(url)

        return response.text[:2000]

    except Exception as e:

        return f"Search Error: {str(e)}"