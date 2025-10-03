# Achareh Assistant

A simple AI-powered assistant that simulates Achareh service requests.

## Features
- Detect user intent (service request, order tracking, general chat)
- Fetch service pricing via Achareh API
- Track and store conversations in SQLite
- Dockerized for easy deployment

## Structure
"""
achareh-assistant/
├── app/
│   ├── main.py
│   ├── services.py
│   ├── conversation.py
│   └── database.py
├── requirements.txt
├── Dockerfile
└── README.md
"""

## Setup

```bash
git clone <repo-url>
cd achareh-assistant
pip install -r requirements.txt
python app/main.py
