# Business Case Chatbot

An AI-powered chatbot for analyzing business cases — market entry, ROI, cost-benefit, growth strategy, valuation, and more. Built with FastAPI (Python) + HTML frontend, powered by the Claude API.

## Project Structure

```
business-case-chatbot/
├── backend/
│   ├── main.py            # FastAPI app
│   ├── requirements.txt   # Python dependencies
│   └── .env.example       # Environment variable template
├── frontend/
│   └── index.html         # Chat UI
├── .gitignore
└── README.md
```

## Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/gaganaramesh09/business-case-chatbot.git
cd business-case-chatbot
```

### 2. Set up the backend
```bash
cd backend
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add your API key
```bash
cp .env.example .env
# Edit .env and add your Anthropic API key
```

### 4. Start the backend
```bash
uvicorn main:app --reload
# Runs on http://localhost:8000
```

### 5. Open the frontend
Open `frontend/index.html` in your browser. That's it!

## API Endpoint

`POST /chat`

```json
{
  "messages": [
    { "role": "user", "content": "Help me evaluate a market entry into Southeast Asia." }
  ]
}
```

## Features
- Market entry analysis
- ROI & financial modeling
- Cost-benefit analysis
- Growth strategy frameworks
- Company valuation
- Make vs buy decisions
- Full conversation context maintained
