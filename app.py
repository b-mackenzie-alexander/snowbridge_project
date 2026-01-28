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
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)
