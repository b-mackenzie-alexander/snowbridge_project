# SnowBridge Project Notes

**Project Status:** ✅ Initialized and Fully Functional

## Team Roles & Completed Tasks

| Name | Role | Status | Completed Tasks |
|------|------|--------|----------------|
| **Beatrice** | Architect | ✅ Complete | Built `triage_request()` function with OpenAI integration and fallback logic, implemented state management with `st.session_state` |
| **Abdoul** | Frontend | ✅ Complete | Linked Submit form to AI triage function, built complete volunteer job board with sorting and claim functionality |
| **Ariel** | UX | ✅ Complete | Mapped and implemented full "Happy Path": Request → AI Triage → Volunteer Feed → Claim Job → Status Update |
| **Robert** | UI | ✅ Complete | Created CSS/Markdown styling for urgency-based color coding (Red/Orange/Green), designed job cards with badges |
| **Angela** | Creative | ✅ Complete | Crafted 5 diverse demo scenarios, wrote Emergency Support disclaimer and user instructions for both views |
| **Christian** | PM/Lead | ✅ Complete | Set up database schema, created seeder function, implemented sorting logic, added admin tools |

## Implementation Details

### AI Triage Logic ✅
- **Function:** `triage_request(request_text, title, location)`
- **Primary Method:** OpenAI GPT-3.5-turbo API with structured JSON output
- **Fallback Method:** Keyword-based urgency scoring (works without API key)
- **Keywords for Level 10 Priority:** "dialysis", "chemo", "oxygen", "emergency", "stuck", "trapped", "can't breathe", "heart", "stroke", "ambulance", "911"
- **Output Format:**
  ```json
  {
    "urgency_score": 1-10,
    "category": "Medical" | "Mobility" | "Access" | "General",
    "summary": "Max 5 words",
    "is_critical": boolean
  }
  ```

### Database Schema ✅
- **Storage:** `st.session_state['jobs']` (in-memory list)
- **Job Structure:**
  ```python
  {
    "id": int,
    "title": str,
    "location": str,
    "request_text": str,
    "ai_analysis": {
      "urgency_score": int,
      "category": str,
      "summary": str,
      "is_critical": bool
    },
    "status": "OPEN" | "CLAIMED"
  }
  ```

### Demo Data Seeder ✅
Created 5 diverse scenarios:
1. **Critical (Score 10):** Dialysis patient - Emergency access blocked
2. **High (Score 7):** Medicine in mailbox - Access needed
3. **Medium (Score 6):** Wheelchair ramp blocked - Mobility issue
4. **Low (Score 3):** Driveway clearing - General request
5. **Critical (Score 9):** Oxygen delivery blocked - Medical emergency

### UI/UX Features ✅
- **Color Coding:**
  - 🔴 Red (Score 8-10): Critical/Medical emergencies
  - 🟠 Orange (Score 4-7): High priority needs
  - 🟢 Green (Score 1-3): Standard requests
- **Accessibility:** Large buttons, clear labels, high contrast, expandable instructions
- **Visual Feedback:** Urgency alerts, success messages, balloons on submission

### Key Files Created
- `app.py` - Main Streamlit application (465 lines)
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore rules
- `SETUP.md` - Setup and usage guide
- `ROADMAP.md` - Updated project roadmap

## Technical Notes

### Dependencies
- `streamlit>=1.28.0` - Web framework
- `openai>=1.3.0` - AI triage API
- `python-dotenv>=1.0.0` - Environment variable management

### Environment Setup
- Create `.env` file with `OPENAI_API_KEY` (optional - app works without it)
- App automatically falls back to keyword-based scoring if API unavailable

### Running the App
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Testing Checklist
- ✅ Submit request with medical keywords → High urgency score
- ✅ Submit general request → Low urgency score
- ✅ View volunteer feed → Sorted by urgency (highest first)
- ✅ Claim job → Status updates to "CLAIMED"
- ✅ Clear database → Resets to demo data
- ✅ Seed demo data → Loads 5 sample jobs
- ✅ Test without API key → Fallback logic works

## Project Completion Summary
All phases of the 45-minute sprint roadmap have been completed. The application is fully functional with:
- Complete requester workflow
- Complete volunteer workflow
- AI-powered triage system
- Database management
- Accessibility features
- Professional UI/UX

**Ready for demonstration and further development!** 🎉