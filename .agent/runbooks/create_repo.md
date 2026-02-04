RUNBOOK: Create GitHub Repo From Template Using Folder Name

EXECUTION AUTHORITY
This file is an EXECUTABLE RUNBOOK for AI agents.
It is not documentation.
It must be followed literally and in order.

If any step cannot be executed exactly as written, the agent MUST STOP immediately.

PURPOSE
Create a new GitHub repository using a template repository.
The new repository name MUST be derived from the current local folder name.
Then link the local folder to the newly created remote repository.

PREREQUISITES (MANDATORY)
Before executing any steps, the agent MUST verify:
- GitHub CLI (gh) is installed
- GitHub CLI is authenticated
- Git is installed
- The agent is operating inside the local folder that should become the repository

If any prerequisite is not met: STOP and report the failure.

DERIVE REPOSITORY NAME (READ-ONLY)
1. Determine the current working directory name.
2. Use this directory name EXACTLY as the GitHub repository name.
3. Do NOT modify, sanitize, lowercase, or transform the name.

Example:
Local folder: BarberCRM
Repository name: BarberCRM

WAIT — USER CONFIRMATION (MANDATORY)
Before creating the repository, the agent MUST present the following information verbatim:
- GitHub owner: MyTownDMIncorporated
- New repository name: <derived folder name>
- Template source: MyTownDigitalSolutions/Repo_Setup_Templates
- Visibility: private

The agent MUST ask:
Proceed to create this GitHub repository from the template?

If the response is anything other than an explicit confirmation (for example “yes”): STOP immediately.

PROCEED — CREATE REMOTE REPOSITORY
After confirmation, the agent MUST execute this command EXACTLY, replacing <folder-name> with the derived folder name:

gh repo create MyTownDigitalSolutions/<folder-name> --template MyTownDigitalSolutions/Repo_Setup_Templates --private

Do NOT add flags.
Do NOT change visibility.
Do NOT change the template.

If this command fails: STOP and report the error.

PROCEED — LINK LOCAL FOLDER TO REMOTE
After successful repository creation, the agent MUST execute the following commands IN ORDER, exactly as written:

git init
git branch -M main
git remote add origin https://github.com/MyTownDigitalSolutions/<folder-name>.git
git pull origin main

Do NOT push local files.
Do NOT overwrite local files.
Do NOT resolve conflicts automatically.

If any command fails: STOP and report the failure.

SUCCESS VERIFICATION (MANDATORY)
The agent MUST verify all of the following:
- The GitHub repository exists online
- The local repository has origin set correctly
- The local working directory contains files from the template repository
- No local files were overwritten without approval

If any verification fails: STOP and report which check failed.

OUTPUT FORMAT (STRICT)
The agent MUST output:
- Repository name created
- Template repository used
- Confirmation that local and remote are linked
- Confirmation that no unauthorized overwrites occurred

The agent MUST end execution with the word:

STOP
