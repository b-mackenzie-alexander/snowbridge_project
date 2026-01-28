import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="SnowBridge",
    page_icon="❄️",
    layout="wide"
)

# 2. State Initialization (Mock DB)
if 'jobs' not in st.session_state:
    st.session_state['jobs'] = [
        {
            "id": 1,
            "location": "123 Maple St",
            "request_text": "Dialysis patient here. Driveway blocked by 3 feet of snow. Emergency exit inaccessible.",
            "ai_analysis": {
                "urgency_score": 10,
                "category": "Medical",
                "summary": "Medical Emergency: Driveway Blocked"
            },
            "status": "OPEN"
        },
        {
            "id": 2,
            "location": "456 Oak Ave",
            "request_text": "I can't get to my mailbox. My meds are in there.",
            "ai_analysis": {
                "urgency_score": 7,
                "category": "Access",
                "summary": "Meds in Mailbox"
            },
            "status": "OPEN"
        }
    ]

# 3. Sidebar Navigation
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
    # Project Info
    st.info("Crisis response platform connecting residents with local volunteers for snow removal.")

# 4. View Rendering
if view == "I Need Help":
    st.title("🆘 I Need Help")
    st.write("Fill out the form below to request assistance with snow removal.")
    # Placeholder for Requester Form
    with st.container():
        st.subheader("Submit Request")
        st.info("Form implementation (Abdoul) will go here.")

elif view == "I Can Help":
    st.title("🏘️ I Can Help")
    st.write("Browse snow removal requests in your area. Sorted by urgency.")
    # Placeholder for Volunteer Feed
    with st.container():
        st.subheader("Volunteer Feed")
        st.info("Feed implementation (Abdoul) will go here.")

# 5. Global CSS/Styling (Optional/Placeholder for Robert)
# 5. Global CSS/Styling (Robert)
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stApp > header {
        background-color: transparent;
    }
    /* Urgency Badges */
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
    /* Card Styling */
    .job-card {
        background-color: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
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
