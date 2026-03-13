# Trade Opportunities API

This project is a FastAPI-based Trade Opportunities API that analyzes market sectors and generates structured markdown reports using Groq LLM.

The API collects market information, analyzes trends using AI, and produces a markdown report that can be saved as a `.md` file.

---

## Features

- FastAPI REST API
- AI-powered sector analysis (Groq LLM)
- Market data collection
- Markdown report generation
- Authentication support
- Rate limiting
- Session tracking
- Structured project architecture
- Swagger API documentation

---

## Project Structure

trade_api/
│
├── app/
│ ├── main.py
│ ├── config.py
│
│ ├── routes/
│ │ analyze.py
│
│ ├── services/
│ │ groq_service.py
│ │ search_service.py
│
│ ├── security/
│ │ auth.py
│ │ rate_limiter.py
│ │ session.py
│
│ ├── models/
│ │ request_model.py
│
│ └── utils/
│ markdown_generator.py
│
├── requirements.txt
└── .env

## Installation
### 1. Download Project

download ZIP.

### 2. Create Virtual Environment

python -m venv venv
Windows:
Activate:venv\Scripts\activate

Mac/Linux:source venv/bin/activate


---

### 3. Install Dependencies


---

## Environment Variables

Create `.env` file in project root.

Example:
GROQ_API_KEY=your_api_key_here
SECRET_KEY=123456789

---

## Running the API

Start server:uvicorn app.main:app --reload

Server runs on:http://127.0.0.1:8000


---

## API Documentation

Swagger UI:http://127.0.0.1:8000/docs

---

## API Endpoint

### Analyze Market Sector
GET /analyze/{sector}

Example:http://127.0.0.1:8000/analyze/technology

---

## Example Response
{
"sector": "technology",
"report": "# Market Overview\nThe Indian technology sector..."
}

---

## Markdown Output

The API generates a structured markdown report:

The report can be saved as a `.md` file.

---

## Technologies Used

- Python
- FastAPI
- Groq LLM
- Uvicorn
- Requests
- Python-dotenv

---

## Security Features

- API authentication support
- Rate limiting
- Session tracking
- Input validation

---

## Author

Logeshwaran




