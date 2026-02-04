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
After confirmation, the agent MUST execute the following command EXACTLY.
No substitutions. No additional flags.
gh repo create MyTownDMIncorporated/<folder-name> \
  --template MyTownDigitalSolutions/Repo_Setup_Templates \
  --private

Rules:
- `<folder-name>` MUST be replaced with the derived local folder name
- Do NOT change the template repository
- Do NOT create an empty repository
- Do NOT change visibility

If this command fails:
→ STOP and report the error.

---

## PROCEED — LINK LOCAL FOLDER TO REMOTE

After successful repository creation, the agent MUST execute the following commands IN ORDER:

git init
git branch -M main
git remote add origin https://github.com/MyTownDMIncorporated/<folder-name>.git
git pull origin main


Rules:
- Do NOT push local files
- Do NOT overwrite local files
- Do NOT resolve conflicts automatically

If any command fails:
→ STOP and report the error.

---

## SUCCESS VERIFICATION (MANDATORY)

The agent MUST verify ALL of the following:

- The GitHub repository exists online
- The local repository has `origin` set correctly
- The local working directory contains files from the template repository
- No local files were overwritten without approval

If ANY verification fails:
→ STOP and report which check failed.

---

## OUTPUT FORMAT (STRICT)

The agent MUST output:

- Repository name created
- Template repository used
- Confirmation that local and remote are linked
- Confirmation that no unauthorized overwrites occurred

The agent MUST end execution with the word:

STOP


