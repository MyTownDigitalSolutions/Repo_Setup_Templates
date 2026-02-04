# RUNBOOK: Create GitHub Repo From Template Using Folder Name

## EXECUTION AUTHORITY
This file is an EXECUTABLE RUNBOOK for AI agents.
It is not documentation.
It must be followed literally and in order.

If any step cannot be executed exactly as written,
the agent must STOP immediately.

---

## PURPOSE
Create a new GitHub repository using a template repository,
where the new repository name is derived from the local folder name.
Then link the local folder to the newly created remote repository.

---

## PREREQUISITES (MANDATORY)
Before executing any steps, the agent must verify:

- GitHub CLI (`gh`) is installed
- GitHub CLI is authenticated
- The agent is operating inside the local folder that should become the repository

If any prerequisite is not met:
→ STOP and report the failure.

---

## DERIVE REPOSITORY NAME (READ-ONLY)
- Determine the current working directory name.
- Use this directory name EXACTLY as the new repository name.
- Do NOT modify, sanitize, or transform the name.

Example:
- Local folder: `BarberCRM`
- Repository name: `BarberCRM`

---

## WAIT — USER CONFIRMATION (MANDATORY)
Before creating the repository, the agent MUST pause and ask for confirmation.

The agent must present the following information verbatim:

- GitHub owner: `MyTownDMIncorporated`
- New repository name: `<derived folder name>`
- Template source: `MyTownDigitalSolutions/Repo_Setup_Templates`
- Visibility: `private`

The agent must ask:
> “Proceed to create this GitHub repository?”

If the response is anything other than an explicit confirmation:
→ STOP immediately.

---

## CREATE REMOTE REPOSITORY (PROCEED)
After confirmation, the agent must execute this command EXACTLY:

