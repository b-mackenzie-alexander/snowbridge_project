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
                # Store new request in session state
                new_job = {
                    "id": len(st.session_state['jobs']) + 1,
                    "title": title,
                    "location": location,
                    "request_text": request_text,
                    "ai_analysis": {
                        "urgency_score": 5,  # Placeholder - will be set by AI triage
                        "category": "Pending",
                        "summary": title
                    },
                    "status": "OPEN"
                }
                st.session_state['jobs'].append(new_job)
                st.success(f"✅ Request submitted! ID: {new_job['id']}")
                st.balloons()
            elif submitted:
                st.error("❌ Please fill in all fields.")

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
