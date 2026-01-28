2. roadmap.md
Role: This is your PM’s heartbeat. Check these off every 10-15 minutes.
# 45-Minute Sprint Roadmap: SnowBridge

### Phase 1: Infrastructure (Min 0-10)
- [ ] **Beatrice:** Scaffold `app.py` with `st.sidebar` navigation (Requester vs. Volunteer).
- [x] **Abdoul:** Create the `Submit Request` form (Title, Location, Large Text Area).
- [ ] **Christian:** Set up the `session_state` database schema and a "Clear Database" reset button for testing.
- [ ] **Ariel/Robert:** Finalize the "Accessibility First" color palette.

### Phase 2: The "Brain" (Min 10-25)
- [ ] **Beatrice:** Write the OpenAI function to "Triage" text into JSON.
- [ ] **Christian:** Create a "Seeder" script to inject 5 diverse demo jobs (e.g., 1 Critical, 2 Medium, 2 Low).
- [ ] **Angela:** Write the copy for the "Emergency Support" disclaimer and app instructions.
- [ ] **Robert:** Design the CSS for the "Urgent Alert" banner using `st.markdown`.

### Phase 3: Integration (Min 25-35)
- [ ] **Abdoul:** Link the "Submit" button to the AI function and save result to Christian's DB.
- [ ] **Christian:** Implement the sorting logic: `df.sort_values(by="urgency_score", ascending=False)`.
- [ ] **Ariel:** Perform a "Stress Test"—submit a nonsense request and a critical request to see if AI handles both.

### Phase 4: Polish & Pitch (Min 35-45)
- [ ] **Beatrice/Abdoul:** Fix any "Red Error" bugs in the Streamlit UI.
- [ ] **Christian:** Ensure the "Claim Job" button updates the status from 'Open' to 'In Progress'.
- [ ] **Angela:** Finalize the pitch deck or "About" section in the app.
- [ ] **PM:** Final tech check. "Is the API key working? Is the screen sharing ready?"
