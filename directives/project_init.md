# DIRECTIVE: Project Initialization (Repo Bootstrap)

## Purpose
Initialize or retrofit a repository to conform to the Production-Grade Agent Constitution.
This directive creates the standard directory structure and governance starter files
without overwriting existing user content. It is safe and idempotent to re-run.

---

## Trigger Conditions
Use this directive when:
- A new repository is created
- A repository lacks standard agent governance files
- The user requests:
  - “project init”
  - “repo bootstrap”
  - “set this up with your standard structure”
  - “apply my agent constitution”

---

## Inputs

Required:
- Access to the repository filesystem (read/write)

Optional:
- Project name (for README.md)
- Governance source:
  - Local templates
  - Remote GitHub repo (e.g. Repo_Setup_Templates)
  - Explicit file URLs

Constraints:
- Do NOT guess missing values
- If a required governance file source is unclear → STOP and ask

---

## Outputs

### Required Directories (create if missing)
- `.tmp/`
- `execution/`
- `directives/`
- `.agent/`

### Required Files (create if missing; NEVER overwrite without permission)
- `AGENTS.md`
- `README.md`
- `directives/DIRECTIVE_TEMPLATE.md`
- `directives/project_init.md`
- `.agent/codex_system_prompt.md`

Validation criteria:
- All directories exist
- All required files exist and are non-empty
- No existing user files are overwritten

---

## Execution Tools

Preferred:
- Deterministic filesystem or bootstrap tools (if present)

Fallback:
- Minimal, deterministic file creation actions supported by the environment

If a new execution tool is required:
- STOP
- Request permission before creating it

---

## Step-by-Step Flow

1. Inspect repository root
2. Create missing directories
3. For each required file:
   - If file exists → leave unchanged
   - If file missing → create from canonical template
4. Ensure `.gitignore` excludes:
   - `.env`
   - `.tmp/`
   - credential files
5. Validate outputs against checklist
6. Report a concise summary of actions taken

---

## Edge Cases & Constraints

- Never overwrite existing files unless explicitly approved
- Never delete user files
- Never introduce paid API usage
- If an existing structure conflicts with the standard layout → STOP
- If governance templates are unavailable → STOP and ask how to proceed

---

## Validation Checklist
- [ ] `.tmp/` exists
- [ ] `execution/` exists
- [ ] `directives/` exists
- [ ] `.agent/` exists
- [ ] `AGENTS.md` exists
- [ ] `directives/DIRECTIVE_TEMPLATE.md` exists
- [ ] `directives/project_init.md` exists
- [ ] `.agent/codex_system_prompt.md` exists
- [ ] `README.md` exists
- [ ] No existing user files overwritten

---

## Failure Learnings (Append-Only)

- Date:
- What failed:
- Root cause:
- Fix applied:
- Preventive update:
