# SnowBridge Setup Guide

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure OpenAI API Key (Optional)

The app works with or without an OpenAI API key. If you have one:

1. Create a `.env` file in the project root:
```bash
cp .env.example .env
```

2. Add your OpenAI API key to `.env`:
```
OPENAI_API_KEY=your_actual_api_key_here
```

**Note:** If no API key is provided, the app will use a fallback keyword-based urgency scoring system.

### 3. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Features Implemented

✅ **AI Triage System** - Analyzes requests and assigns urgency scores (1-10)  
✅ **Requester View** - Simple form for submitting snow removal requests  
✅ **Volunteer Feed** - Sorted by urgency with color-coded badges  
✅ **Claim Job Functionality** - Volunteers can claim and help with requests  
✅ **Demo Data Seeder** - 5 diverse sample requests for testing  
✅ **Database Reset** - Clear/reset button for testing  
✅ **Accessibility Features** - Large buttons, clear labels, high contrast  
✅ **Emergency Disclaimer** - Safety information for users  

## Project Structure

```
snowbridge_project/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variable template
├── .gitignore         # Git ignore rules
├── README.md          # Project overview
├── ROADMAP.md         # Development roadmap
├── AGENT.md           # Agent context and guidelines
├── NOTES.md           # Team notes
└── SETUP.md           # This file
```

## Testing

1. **Test Requester Flow:**
   - Navigate to "I Need Help"
   - Fill out the form with various scenarios (medical, general, etc.)
   - Submit and verify AI triage assigns appropriate urgency scores

2. **Test Volunteer Flow:**
   - Navigate to "I Can Help"
   - View the sorted feed (highest urgency first)
   - Claim a job and verify status updates

3. **Test Database Functions:**
   - Use "Clear Database" to reset
   - Use "Seed Demo Data" to load sample requests

## Troubleshooting

- **OpenAI API Errors:** The app will automatically fall back to keyword-based scoring if the API fails
- **Port Already in Use:** Change the port with `streamlit run app.py --server.port 8502`
- **Missing Dependencies:** Run `pip install -r requirements.txt` again
