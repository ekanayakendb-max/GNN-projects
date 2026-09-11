# Project Activity History & Change Log (`history.md`)

> **Project:** VS Workshop GNN (PTV Vissim & Graph Neural Networks)  
> **Research Group:** TRANSIIT Research Group, SIIT  
> **Usage:** This file maintains a chronological, append-only log of project activities, meeting notes, decisions, comments, and actionable items. Each new entry is appended to the bottom of the file with a date and timestamp.

---

## Log Entry Template

Whenever a new record is added, the following structure is used:

```markdown
### [YYYY-MM-DD HH:MM:SS ±HH:MM] - <Title / Summary of Activity>
- **Activity Log:** Summary of what was done, discussed, or executed.
- **Comments / Observations:** Notes, technical insights, roadblocks, or findings.
- **Action Needed:**
  - [ ] Action item 1
  - [ ] Action item 2
- **Logged By:** User / Agent / Collaborator
```

---

## Chronological Activity Log

### [2026-09-11 14:47:00 +07:00] - Project Kickoff & Initialization
- **Activity Log:**
  - Initialized project workspace for the VS Workshop GNN (PTV Vissim + Graph Neural Networks).
  - Created [`start.md`](file:///e:/SIIT/TRANSIIT/Group%20meetings/Projects/VS%20workshop%20GNN/start.md) establishing project architecture, recommended directory structure, environment setup instructions, Vissim COM interface testing script, and workshop roadmap.
  - Created [`history.md`](file:///e:/SIIT/TRANSIIT/Group%20meetings/Projects/VS%20workshop%20GNN/history.md) to log ongoing activities, comments, and pending actions.
- **Comments / Observations:**
  - System environment contains PTV Vissim 2025 (`VISSIM2025_EXAMPLES` configured) and Python 3.14.
  - Python COM interface with Vissim requires 64-bit Python environment matching 64-bit Vissim.
- **Action Needed:**
  - [ ] Set up Python virtual environment (`.venv`) and install core dependencies (`pywin32`, `networkx`, `pandas`, etc.).
  - [ ] Run initial Vissim COM test script to verify communication with PTV Vissim 2025.
  - [ ] Create repository skeleton directories (`configs/`, `data/`, `models/`, `scripts/`, `notebooks/`).
- **Logged By:** Antigravity Agent & User
