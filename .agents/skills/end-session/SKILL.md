---
name: end-session
description: >-
  Wrap up and conclude the current development/research session.
  Synthesizes session activities, records observations and blockers, and appends a structured,
  timestamped log entry to history.md with an actionable checklist ready for the next session.
  Activate this skill whenever the user says to end the session, wrap up, finish for today,
  or conclude the working session.
---

# End Session Workflow Skill

This skill provides a standardized end-of-session runbook to gracefully conclude a session, persist project context, and prepare the workspace for a seamless restart in the next session.

---

## Trigger Conditions

Activate this skill when the user states phrases such as:
- *"End the session"* / *"End session"*
- *"Wrap up for today"* / *"Let's stop here"*
- *"Conclude the session"*
- *"Done for now"*

---

## Step-by-Step Procedure

### Step 1: Review Session Trajectory & Accomplishments
Gather all key events from the current session:
1. Files created, updated, or deleted (e.g., scripts, configuration files, notebooks, documentation).
2. Tests or simulation runs performed (e.g., Vissim COM connections, script executions).
3. Technical decisions made or architectural insights discovered.
4. Unresolved issues, errors, or roadblocks encountered.

### Step 2: Formulate Next Session's Action Items
Define clear, concrete next steps that can be immediately picked up in the next session. Format them as unchecked markdown checklist items:
- `- [ ] <Specific task or milestone>`

### Step 3: Append Entry to `history.md`
Append a new entry at the bottom of [`history.md`](file:///e:/SIIT/TRANSIIT/Group%20meetings/Projects/VS%20workshop%20GNN/history.md) adhering to the standard template:

```markdown
### [YYYY-MM-DD HH:MM:SS ±HH:MM] - End of Session: <Title / Short Summary>
- **Activity Log:**
  - <Bullet 1: Concrete achievement>
  - <Bullet 2: Files created or modified>
  - <Bullet 3: Commands or tests executed>
- **Comments / Observations:**
  - <Notes, simulation parameters, findings, or warnings>
- **Action Needed:**
  - [ ] <First task for next session>
  - [ ] <Second task for next session>
- **Logged By:** Antigravity Agent & User
```

> **Note on Timestamp:** Use the exact current local timestamp provided in session metadata (or query via PowerShell `Get-Date -Format "yyyy-MM-dd HH:mm:ss K"` if needed).

### Step 4: Verify the Update
Check the file content or diff of [`history.md`](file:///e:/SIIT/TRANSIIT/Group%20meetings/Projects/VS%20workshop%20GNN/history.md) to ensure the formatting is clean, properly aligned, and no previous entries were overwritten.

### Step 5: Deliver Closing Briefing to the User
Provide a concise, professional closing response:
1. Confirm that [`history.md`](file:///e:/SIIT/TRANSIIT/Group%20meetings/Projects/VS%20workshop%20GNN/history.md) has been updated with the session record.
2. Present a brief summary of what was accomplished today.
3. Highlight the immediate checklist queued up for when the next session resumes.
