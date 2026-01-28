import streamlit as st
import os
import json
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 1. Page Configuration
st.set_page_config(
    page_title="SnowBridge",
    page_icon="❄️",
    layout="wide"
)

# 2. AI Triage Function
def triage_request(request_text, title="", location=""):
    """
    Analyzes natural language request and returns structured JSON with urgency score.
    Uses OpenAI API if available, otherwise falls back to keyword-based logic.
    """
    try:
        from openai import OpenAI
        api_key = os.getenv("OPENAI_API_KEY")
        
        if api_key:
            client = OpenAI(api_key=api_key)
            
            system_prompt = """You are an Emergency Dispatcher for a snow removal crisis response platform.
Analyze the user's request and determine urgency. Look for keywords like: dialysis, chemo, oxygen, medicine, 
stuck, emergency exit, doctor appointment, medical, mobility issues, wheelchair, etc.

Return ONLY valid JSON in this exact format:
{
  "urgency_score": [Integer 1-10],  // 10 = Medical Emergency, 1 = Low priority
  "category": [String: "Medical", "Mobility", "Access", "General"],
  "summary": [String: Max 5 words],
  "is_critical": [Boolean]
}"""

            user_prompt = f"Title: {title}\nLocation: {location}\nRequest: {request_text}\n\nAnalyze urgency and return JSON only."
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3,
                max_tokens=150
            )
            
            result_text = response.choices[0].message.content.strip()
            # Extract JSON from response (handle markdown code blocks)
            if "```" in result_text:
                result_text = result_text.split("```")[1]
                if result_text.startswith("json"):
                    result_text = result_text[4:]
            
            analysis = json.loads(result_text)
            return analysis
            
    except Exception as e:
        st.warning(f"⚠️ OpenAI API error: {str(e)}. Using fallback logic.")
    
    # Fallback: Keyword-based urgency scoring
    request_lower = (title + " " + request_text).lower()
    
    # Critical keywords (score 8-10)
    critical_keywords = ["dialysis", "chemo", "oxygen", "emergency", "stuck", "trapped", 
                        "can't breathe", "heart", "stroke", "ambulance", "911"]
    # High priority keywords (score 6-8)
    high_keywords = ["medicine", "meds", "doctor", "appointment", "medical", "wheelchair",
                    "disabled", "elderly", "can't walk", "mobility"]
    # Medium keywords (score 4-6)
    medium_keywords = ["mailbox", "door", "driveway", "access", "need to leave"]
    
    urgency_score = 3  # Default low
    category = "General"
    is_critical = False
    
    if any(kw in request_lower for kw in critical_keywords):
        urgency_score = random.randint(9, 10)
        category = "Medical"
        is_critical = True
    elif any(kw in request_lower for kw in high_keywords):
        urgency_score = random.randint(6, 8)
        category = "Medical" if any(kw in request_lower for kw in ["medical", "doctor", "medicine"]) else "Mobility"
    elif any(kw in request_lower for kw in medium_keywords):
        urgency_score = random.randint(4, 6)
        category = "Access"
    
    summary_words = title.split()[:5] if title else request_text.split()[:5]
    summary = " ".join(summary_words)
    
    return {
        "urgency_score": urgency_score,
        "category": category,
        "summary": summary,
        "is_critical": is_critical
    }

# 3. Seeder Function
def seed_demo_jobs():
    """Creates 5 diverse demo jobs for testing."""
    return [
        {
            "id": 1,
            "title": "Dialysis Patient - Emergency Access",
            "location": "123 Maple St, Boston MA",
            "request_text": "Dialysis patient here. Driveway blocked by 3 feet of snow. Emergency exit inaccessible. Need to get to treatment center by 2 PM today.",
            "ai_analysis": {
                "urgency_score": 10,
                "category": "Medical",
                "summary": "Dialysis Patient Emergency",
                "is_critical": True
            },
            "status": "OPEN"
        },
        {
            "id": 2,
            "title": "Medicine in Mailbox",
            "location": "456 Oak Ave, Cambridge MA",
            "request_text": "I can't get to my mailbox. My meds are in there and I need them today. I'm 78 and use a walker.",
            "ai_analysis": {
                "urgency_score": 7,
                "category": "Access",
                "summary": "Meds in Mailbox",
                "is_critical": False
            },
            "status": "OPEN"
        },
        {
            "id": 3,
            "title": "Wheelchair Access Blocked",
            "location": "789 Pine Rd, Somerville MA",
            "request_text": "My wheelchair ramp is completely covered. I can't leave my apartment. No emergency, but I need groceries.",
            "ai_analysis": {
                "urgency_score": 6,
                "category": "Mobility",
                "summary": "Wheelchair Ramp Blocked",
                "is_critical": False
            },
            "status": "OPEN"
        },
        {
            "id": 4,
            "title": "Driveway Clearing",
            "location": "321 Elm St, Brookline MA",
            "request_text": "Just need my driveway cleared so I can get to work tomorrow. Not urgent, but would appreciate help.",
            "ai_analysis": {
                "urgency_score": 3,
                "category": "General",
                "summary": "Driveway Clearing",
                "is_critical": False
            },
            "status": "OPEN"
        },
        {
            "id": 5,
            "title": "Oxygen Delivery Blocked",
            "location": "555 Cedar Ln, Newton MA",
            "request_text": "Oxygen tank delivery can't reach my house. Driveway and walkway completely blocked. I have backup but running low.",
            "ai_analysis": {
                "urgency_score": 9,
                "category": "Medical",
                "summary": "Oxygen Delivery Blocked",
                "is_critical": True
            },
            "status": "OPEN"
        }
    ]

# 4. State Initialization (Mock DB)
if 'jobs' not in st.session_state:
    st.session_state['jobs'] = seed_demo_jobs()

# 5. Sidebar Navigation
with st.sidebar:
    st.title("❄️ SnowBridge")
    st.markdown("---")
    view = st.radio(
        "Navigation",
        ["I Need Help", "I Can Help"],
        index=0,
        help="Switch between requester and volunteer views."
    )
    
    st.markdown("---")
    
    # Emergency Support Disclaimer
    st.warning("""
    **⚠️ Emergency Support Disclaimer**
    
    This is a volunteer-based platform. For life-threatening emergencies, call 911 immediately.
    """)
    
    st.markdown("---")
    
    # Clear Database Button (for testing)
    st.subheader("🔧 Admin Tools")
    if st.button("🗑️ Clear Database", use_container_width=True, help="Reset all requests (for testing)"):
        st.session_state['jobs'] = seed_demo_jobs()
        st.success("Database reset to demo data!")
        st.rerun()
    
    if st.button("🌱 Seed Demo Data", use_container_width=True, help="Load 5 sample requests"):
        st.session_state['jobs'] = seed_demo_jobs()
        st.success("Demo data loaded!")
        st.rerun()
    
    st.markdown("---")
    
    # Project Info
    st.info("Crisis response platform connecting residents with local volunteers for snow removal.")
    
    # Stats
    total_jobs = len(st.session_state['jobs'])
    open_jobs = len([j for j in st.session_state['jobs'] if j['status'] == 'OPEN'])
    st.caption(f"📊 Total Requests: {total_jobs} | Open: {open_jobs}")

# 6. View Rendering
if view == "I Need Help":
    st.title("🆘 I Need Help")
    
    # Instructions
    with st.expander("ℹ️ How to Use SnowBridge", expanded=False):
        st.markdown("""
        **Welcome to SnowBridge!** This platform connects you with local volunteers for snow removal assistance.
        
        **How it works:**
        1. Fill out the form below with your address and situation
        2. Our AI will analyze your request and assign an urgency score
        3. Local volunteers will see your request and can claim it to help
        4. You'll be notified when someone volunteers to help
        
        **Important:** For life-threatening emergencies, call 911 immediately. This platform is for non-emergency snow removal assistance.
        
        **Accessibility:** All fields are designed with large text and clear labels for easy use.
        """)
    
    st.write("Fill out the form below to request assistance with snow removal.")
    
    # Submit Request Form
    with st.container():
        st.subheader("Submit Request")
        
        # Form fields with clear labels for accessibility
        with st.form("request_form"):
            # Title field
            title = st.text_input(
                label="**What do you need help with?**",
                placeholder="e.g., Driveway blocked, Can't access door",
                help="Brief description of your need"
            )
            
            # Location field
            location = st.text_input(
                label="**Your Address**",
                placeholder="e.g., 123 Maple Street, Boston MA",
                help="Where do you need help?"
            )
            
            # Large text area for detailed request
            request_text = st.text_area(
                label="**Tell us more about your situation**",
                placeholder="Describe why you need help, any medical conditions, accessibility needs, etc.",
                height=150,
                help="Be as detailed as possible to help volunteers understand urgency"
            )
            
            # Submit button
            submitted = st.form_submit_button(
                label="🔔 REQUEST HELP",
                use_container_width=True,
                type="primary"
            )
            
            # Handle form submission
            if submitted and title and location and request_text:
                with st.spinner("🤖 Analyzing urgency with AI..."):
                    # Call AI triage function
                    ai_analysis = triage_request(request_text, title, location)
                    
                    # Store new request in session state
                    new_job = {
                        "id": max([j['id'] for j in st.session_state['jobs']], default=0) + 1,
                        "title": title,
                        "location": location,
                        "request_text": request_text,
                        "ai_analysis": ai_analysis,
                        "status": "OPEN"
                    }
                    st.session_state['jobs'].append(new_job)
                    
                    # Show urgency alert
                    if ai_analysis.get('is_critical', False):
                        st.error(f"🚨 **CRITICAL REQUEST** - Urgency Score: {ai_analysis['urgency_score']}/10")
                    elif ai_analysis['urgency_score'] >= 7:
                        st.warning(f"⚠️ **HIGH PRIORITY** - Urgency Score: {ai_analysis['urgency_score']}/10")
                    else:
                        st.info(f"ℹ️ Urgency Score: {ai_analysis['urgency_score']}/10")
                    
                    st.success(f"✅ Request submitted! ID: {new_job['id']}")
                    st.balloons()
                    st.rerun()
            elif submitted:
                st.error("❌ Please fill in all fields.")

elif view == "I Can Help":
    st.title("🏘️ I Can Help")
    
    # Instructions for volunteers
    with st.expander("ℹ️ Volunteer Instructions", expanded=False):
        st.markdown("""
        **Thank you for volunteering!** Your help makes a real difference in our community.
        
        **How it works:**
        1. Browse requests below, sorted by urgency (highest first)
        2. Red badges = Critical/Medical emergencies
        3. Orange badges = High priority needs
        4. Green badges = Standard requests
        5. Click "Claim Job" to take on a request
        6. Once claimed, coordinate directly with the requester
        
        **Safety Tips:**
        - Always prioritize your own safety
        - Communicate clearly with requesters
        - Let someone know where you're going
        - Dress appropriately for the weather
        
        **Thank you for being a community hero!** ❄️🤝
        """)
    
    st.write("Browse snow removal requests in your area. Sorted by urgency.")
    
    # Volunteer Feed
    with st.container():
        st.subheader("📋 Volunteer Feed")
        
        # Filter open jobs and sort by urgency
        open_jobs = [job for job in st.session_state['jobs'] if job['status'] == 'OPEN']
        sorted_jobs = sorted(open_jobs, key=lambda x: x['ai_analysis']['urgency_score'], reverse=True)
        
        if not sorted_jobs:
            st.info("🎉 No open requests at the moment. Check back soon!")
        else:
            st.caption(f"Showing {len(sorted_jobs)} open request(s), sorted by urgency")
            
            for job in sorted_jobs:
                urgency_score = job['ai_analysis']['urgency_score']
                category = job['ai_analysis']['category']
                is_critical = job['ai_analysis'].get('is_critical', False)
                
                # Color coding based on urgency
                if urgency_score >= 8 or is_critical:
                    card_color = "#ff4444"  # Red
                    badge_text = "🚨 CRITICAL"
                    badge_color = "#cc0000"
                elif urgency_score >= 4:
                    card_color = "#ff8800"  # Orange
                    badge_text = "⚠️ HIGH PRIORITY"
                    badge_color = "#cc6600"
                else:
                    card_color = "#44aa44"  # Green
                    badge_text = "ℹ️ STANDARD"
                    badge_color = "#228822"
                
                # Create job card
                with st.container():
                    st.markdown(f"""
                    <div style="
                        border-left: 5px solid {card_color};
                        padding: 15px;
                        margin: 10px 0;
                        background-color: #ffffff;
                        border-radius: 5px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    ">
                        <div style="display: flex; justify-content: space-between; align-items: start;">
                            <div>
                                <h3 style="margin: 0; color: #333;">{job.get('title', 'Snow Removal Request')}</h3>
                                <p style="margin: 5px 0; color: #666;">📍 {job['location']}</p>
                            </div>
                            <span style="
                                background-color: {badge_color};
                                color: white;
                                padding: 5px 10px;
                                border-radius: 15px;
                                font-size: 12px;
                                font-weight: bold;
                            ">{badge_text}</span>
                        </div>
                        <p style="margin: 10px 0; color: #444;">{job['request_text']}</p>
                        <div style="display: flex; gap: 15px; margin-top: 10px;">
                            <span style="color: #666;">📊 Urgency: <strong>{urgency_score}/10</strong></span>
                            <span style="color: #666;">🏷️ Category: <strong>{category}</strong></span>
                            <span style="color: #666;">🆔 ID: <strong>#{job['id']}</strong></span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Claim button
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        if st.button(f"✅ Claim Job #{job['id']}", key=f"claim_{job['id']}", use_container_width=True):
                            # Update job status
                            for idx, j in enumerate(st.session_state['jobs']):
                                if j['id'] == job['id']:
                                    st.session_state['jobs'][idx]['status'] = 'CLAIMED'
                                    break
                            st.success(f"✅ You've claimed Job #{job['id']}! Thank you for helping!")
                            st.rerun()
                    
                    st.markdown("---")

# 7. Global CSS/Styling (Combined Architecture & UI)
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    
    .stApp > header {
        background-color: transparent;
    }

    /* Urgency Badges (Safety Signal Palette) */
    .urgency-badge {
        padding: 6px 12px;
        border-radius: 6px;
        color: white;
        font-weight: 800;
        display: inline-block;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    @keyframes pulse-red {
        0% { box-shadow: 0 0 0 0 rgba(220, 53, 69, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(220, 53, 69, 0); }
        100% { box-shadow: 0 0 0 0 rgba(220, 53, 69, 0); }
    }

    .urgent {
        background-color: #dc3545; /* Safety Signal Red */
        border: 2px solid #ff6b6b;
        animation: pulse-red 2s infinite;
    }

    .moderate {
        background-color: #fd7e14; /* Safety Orange */
        color: white; 
        border: 2px solid #ffc107;
    }

    .standard {
        background-color: #28a745; /* Safety Green */
        border: 2px solid #5dd77d;
    }

    /* Urgent Alert Banner Styling */
    .urgent-banner {
        background: linear-gradient(90deg, #ff4444 0%, #cc0000 100%);
        color: white;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
        font-weight: bold;
        text-align: center;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }

    /* Card Styling */
    .job-card {
        background-color: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        transition: transform 0.2s;
    }
    
    .job-card:hover {
        transform: translateY(-2px);
    }

    /* High contrast for accessibility */
    .stButton>button {
        font-size: 16px;
        font-weight: bold;
        padding: 10px 20px;
    }
    
    /* Form inputs */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# Helper function for Robert's UI
def get_urgency_badge(score):
    if score >= 8:
        return f'<span class="urgency-badge urgent">CRITICAL (Score: {score})</span>'
    elif score >= 4:
        return f'<span class="urgency-badge moderate">MODERATE (Score: {score})</span>'
    else:
        return f'<span class="urgency-badge standard">STANDARD (Score: {score})</span>'

# Test Section (Visible only in 'I Can Help' for now to demonstrate)
if view == "I Can Help":
    st.markdown("### 🎨 UI Style Preview (Robert)")
    cols = st.columns(3)
    with cols[0]:
        st.markdown(get_urgency_badge(9), unsafe_allow_html=True)
        st.caption("Critical Style")
    with cols[1]:
        st.markdown(get_urgency_badge(5), unsafe_allow_html=True)
        st.caption("Moderate Style")
    with cols[2]:
        st.markdown(get_urgency_badge(2), unsafe_allow_html=True)
        st.caption("Standard Style")
    st.markdown("---")
