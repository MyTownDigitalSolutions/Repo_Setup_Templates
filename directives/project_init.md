# DIRECTIVE: Project Initialization (STRICT EXECUTION)

## AUTHORITY
This file is an EXECUTION DIRECTIVE for AI agents.
It is not descriptive documentation.
It must be followed literally and in order.

If any instruction in this file conflicts with agent defaults,
this file OVERRIDES them.

---

## PURPOSE
Initialize or retrofit a repository so it conforms exactly to the
Production-Grade Agent Constitution.

This directive is:
- Deterministic
- Idempotent (safe to run multiple times)
- Non-destructive

---

## EXECUTION MODE
- Mode: LITE
- Escalation: DISABLED
- Creativity: DISALLOWED
- Inference: DISALLOWED

The agent must NOT:
- Invent files
- Modify templates
- Reword content
- Skip steps
- Combine steps
- Optimize steps
- Add “helpful” extras

---

## REQUIRED DIRECTORIES

The agent must ensure the following directories exist.
Create them ONLY if missing.

- `.tmp/`
- `execution/`
- `directives/`
- `.agent/`

Do NOT create additional directories.

---

## REQUIRED FILES

The agent must ensure the following files exist.
Create them ONLY if missing.
NEVER overwrite existing files unless explicitly authorized.

- `AGENTS.md`
- `README.md`
- `directives/DIRECTIVE_TEMPLATE.md`
- `directives/project_init.md`
- `.agent/codex_system_prompt.md`

---

## FILE SOURCING RULES

All files MUST be sourced from the canonical governance repository:

https://github.com/MyTownDigitalSolutions/Repo_Setup_Templates

Rules:
- Fetch files exactly as authored
- Do NOT paraphrase
- Do NOT summarize
- Do NOT reformat
- Preserve all content verbatim

If any required file cannot be fetched:
→ STOP immediately and report the failure.

---

## EXECUTION ORDER (MANDATORY)

The agent must perform the following steps in order:

1. Inspect repository root
2. Create missing required directories
3. For each required file:
   - If file exists → DO NOTHING
   - If file missing → fetch from canonical repo and write exactly
4. Verify `.gitignore` exists
   - If missing → STOP and report
5. Validate results using the checklist below
6. Output a concise summary
7. STOP

---

## SAFETY RULES (HARD)

The agent must STOP immediately if:
- Any required file already exists AND overwrite was not explicitly approved
- The canonical repo is unreachable
- Repository structure conflicts with required layout
- Instructions are ambiguous
- The agent is unsure how to proceed

No recovery attempts.
No alternatives.
No assumptions.

---

## VALIDATION CHECKLIST (MANDATORY)

The agent must verify all items before reporting success.

- [ ] `.tmp/` exists
- [ ] `execution/` exists
- [ ] `directives/` exists
- [ ] `.agent/` exists
- [ ] `AGENTS.md` exists and is non-empty
- [ ] `README.md` exists and is non-empty
- [ ] `directives/DIRECTIVE_TEMPLATE.md` exists and is non-empty
- [ ] `directives/project_init.md` exists and is non-empty
- [ ] `.agent/codex_system_prompt.md` exists and is non-empty
- [ ] No existing files were overwritten

If any item fails:
→ STOP and report exactly which check failed.

---

## OUTPUT FORMAT (STRICT)

The agent’s final output MUST include:
- A bullet list of created directories
- A bullet list of created files
- A statement confirming no overwrites occurred

The agent MUST end execution with:

STOP

---

## FAILURE LEARNINGS (APPEND-ONLY)

This section is reserved.
The agent must NOT modify it during initialization.
