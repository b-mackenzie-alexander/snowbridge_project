It is strictly scoped to the 45-minute timeline, forcing the AI to prioritize speed, the "SnowBridge" mission, and the specific Streamlit stack.

Markdown
# Agent Context: SnowBridge (Hackathon MVP)

## 1. Project Mission
**SnowBridge** is a crisis response platform connecting elderly, disabled, and incapacitated residents with local volunteers for snow removal.
* **Primary Goal:** AI-driven triage to prioritize life-threatening situations (e.g., dialysis access, oxygen delivery) over cosmetic clearing.
* **Target Audience:**
    * *Requesters:* Non-technical, high-accessibility needs (Big buttons, minimal text).
    * *Volunteers:* Gig-economy style feed, sorted by Urgency Score.

## 2. Constraints & Timeline
* **Time Limit:** 45 Minutes (Strict Code Freeze).
* **Complexity Level:** Extreme Low-Code / No-Code logic.
* **Forbidden:** Complex databases (Postgres/SQL), Authentication (Auth0/Firebase), Custom CSS animations.
* **Allowed:** Local JSON storage, `st.session_state` for demo persistence, OpenAI API.

## 3. Tech Stack
* **Frontend/App:** Python Streamlit (`import streamlit as st`).
* **Logic/AI:** OpenAI API (`gpt-4-turbo` or `gpt-3.5-turbo`) for NLP Triage.
* **Data:** In-memory Python lists or `session_state` (Mock Database).

## 4. AI Implementation Logic (The Triage System)
The core feature is the **Risk Scoring Engine**. The AI must analyze natural language input and return structured JSON.

**System Prompt Structure:**
```text
Role: Emergency Dispatcher.
Input: User request string (e.g., "I'm 80 and can't get to my mailbox").
Task: Analyze urgency.
Output JSON:
{
  "urgency_score": [Integer 1-10], // 10 = Medical Emergency, 1 = Low priority
  "category": [String: "Medical", "Mobility", "Access", "General"],
  "summary": [String: Max 5 words],
  "is_critical": [Boolean]
}
5. UI Requirements
The app must have a sidebar or toggle to switch between two views:
View A: "I Need Help" (The Requester)
Design: Ultra-simple. High contrast.
Input: One large text area (Simulating Voice-to-Text). Label: "Tell us why you need help."
Action: One massive button: "REQUEST HELP."
View B: "I Can Help" (The Volunteer)
Design: Feed/List view.
Sorting: STRICTLY sorted by urgency_score (Descending).
Visuals:
Score 8-10: Red Card / "CRITICAL" badge.
Score 4-7: Orange Card.
Score 1-3: Green Card.
6. Data Structure (Mock DB)
Use this schema for the st.session_state['jobs'] list:
Python
{
    "id": 1,
    "location": "123 Maple St",
    "request_text": "Need to get to chemo appt",
    "ai_analysis": {
        "urgency_score": 9,
        "category": "Medical",
        "summary": "Chemo Appt Blocked"
    },
    "status": "OPEN" // or "CLAIMED"
}
7. Immediate Instructions for Code Generation
Initialize Streamlit app with st.set_page_config(layout="wide").
Create a mock data seeder (populate 3 initial requests: one high risk, one medium, one low).
Implement the OpenAI API call (mock it with random if API key is missing to prevent crash).
Build the Triage Logic function first.

}
