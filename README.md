# SnowBridge

**SnowBridge** is a crisis response platform connecting elderly, disabled, and incapacitated residents with local volunteers for snow removal.

## Mission
AI-driven triage to prioritize life-threatening situations (e.g., dialysis access, oxygen delivery) over cosmetic clearing.

## Tech Stack
- **Frontend/App:** Python Streamlit
- **Logic/AI:** OpenAI API (GPT-4/3.5) for NLP Triage
- **Data:** In-memory persistence (`st.session_state`)

## Target Audience
- **Requesters:** Non-technical, high-accessibility needs (Big buttons, minimal text).
- **Volunteers:** Gig-economy style feed, sorted by Urgency Score.

## Triage System
Analyzes natural language requests to generate:
- `urgency_score` (1-10)
- `category` (Medical, Mobility, Access, General)
- `summary`
- `is_critical` (Boolean)
