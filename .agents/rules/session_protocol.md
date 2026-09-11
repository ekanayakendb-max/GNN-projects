# Session End & History Maintenance Protocol

Whenever the user indicates they want to end the session (e.g., "end the session", "wrap up", "finish for now", "done for today"):

1. **Mandatory History Log Update**:
   - Immediately read and append a new chronological entry to `history.md` in the project root.
   - Format:
     ```markdown
     ### [YYYY-MM-DD HH:MM:SS ±HH:MM] - End of Session: <Brief Summary>
     - **Activity Log:**
       - <Bullet list of accomplishments, scripts written, experiments run, or files modified>
     - **Comments / Observations:**
       - <Key findings, metrics, simulation observations, or decisions made>
     - **Action Needed:**
       - [ ] <Action item ready to be tackled in the next session>
       - [ ] <Next step>
     - **Logged By:** Antigravity Agent & User
     ```
2. **Current Local Timestamp**:
   - Use the current date and local timestamp provided in metadata.
3. **Response to User**:
   - Confirm that `history.md` has been updated and present a concise summary of what is queued up for the next session so the user can easily pick up where they left off.
