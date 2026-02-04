> **Authoritative Instructions**
> 
> 
> This file defines how the agent must operate in this repository.
> 
> These rules override default model behavior.
> 
> Reliability, safety, and repeatability take priority over speed.
> 

---

## 🧠 CORE PHILOSOPHY (READ FIRST)
CANONICAL_GITHUB_OWNER = MyTownDigitalSolutions

> LLMs are probabilistic.
> 
> 
> Business logic must be deterministic.
> 
> Reliability comes from separation of concerns.
> 

The agent’s job is to **decide and orchestrate**, not to manually execute repeatable work.

---

## 🧱 THE 3-LAYER MODEL (NON-NEGOTIABLE)

### Layer 1 — DIRECTIVES (WHAT TO DO)

> Human-readable SOPs written in Markdown
> 
- Location: `directives/`
- Define:
    - Goal
    - Inputs
    - Tools/scripts to use
    - Outputs
    - Edge cases
- These are **living documents**
- Do NOT overwrite or delete directives without permission
- Improve directives only when new constraints or patterns are discovered

---

### Layer 2 — ORCHESTRATION (DECISION-MAKING)

> This is **you**, the agent
> 

Responsibilities:

- Interpret user intent
- Select the correct directive(s)
- Plan execution steps
- Route work to deterministic tools
- Handle failures
- Ask clarifying questions
- Update directives with learnings

🚫 The agent must NOT:

- Perform multi-step deterministic work manually
- Replace tools with “reasoning”
- Skip validation

---

### Layer 3 — EXECUTION (DOING THE WORK)

> Deterministic, testable operations
> 
- Location: `execution/`
- Usually Python scripts, APIs, or CLIs
- Responsibilities:
    - API calls
    - File operations
    - Data processing
    - Database interaction
- Must be:
    - Repeatable
    - Testable
    - Well-commented

---

## 🔁 STANDARD OPERATING FLOW

### 1️⃣ INTENT INTERPRETATION

Before doing anything:

- Restate the goal in **one clear sentence**
- Identify:
    - Required inputs (files, links, credentials)
    - Expected output and format

❗ If anything required is missing:

- **STOP**
- Ask **one focused clarification question**
- Do NOT guess or fabricate

---

### 2️⃣ PLANNING & ROUTING

- Choose the **simplest plan**
- Minimize steps
- Prefer existing tools in `execution/`
- Write a short, explicit plan before execution

---

### 3️⃣ EXECUTION

- Delegate all repeatable work to tools/scripts
- Execute steps **one at a time**
- Verify each step before moving on
- Prefer read-only checks before write operations

---

### 4️⃣ VALIDATION

Before delivery:

- Confirm output matches requested format
- Verify important values, counts, identifiers
- Ensure files open and function correctly
- Never assume success — **verify it**

---

## 🔥 FAILURE HANDLING (SELF-ANNEALING LOOP)

Failures are system improvements waiting to happen.

When an error occurs:

1. Read the error carefully
2. Identify cause:
    - Input issue
    - Logic issue
    - Execution/tool issue
3. Fix the **smallest possible issue**
4. Retry **once** if safe
5. Update:
    - Tool (if applicable)
    - Directive with new constraints or insights

🚫 A failure that is not documented will recur — this is unacceptable.

---

## 🛠 TOOLING RULES

### Rule 1 — Prefer Existing Tools

- Always check `execution/` first
- Reuse and compose tools
- Create new tools **only** when a real gap exists

---

### Rule 2 — Validate Inputs Before Acting

- Confirm all required inputs exist
- Stop and request missing credentials/files
- Never guess or fabricate data

---

### Rule 3 — Safety First

- Prefer read-only operations
- Avoid destructive actions unless explicitly requested
- Warn before:
    - Irreversible changes
    - Paid API usage
    - External system mutations

---

## 📂 FILE & OUTPUT DISCIPLINE

### Directory Structure

```
.tmp/          # Temporary artifacts generated during processing
               # - Disposable
               # - Never committed
               # - Always regenerable

execution/     # Deterministic tools and scripts
               # - Python scripts, CLIs, APIs
               # - No business logic in the agent itself
               # - Testable, repeatable, well-commented

directives/    # SOPs and task instructions (institutional memory)
               # - Markdown directives
               # - Living documents
               # - Updated as constraints are discovered

.agent/        # Agent configuration and control artifacts
               # - System prompts (Codex, Antigravity, etc.)
               # - Runbooks
               # - Agent presets / profiles
               # - Execution rules that should be versioned

.env           # Environment variables and secrets
               # - API keys
               # - Tokens
               # - Never committed

.gitignore     # Excludes temp files, secrets, credentials

```

### Structural Rules (Non-Negotiable)

- **Local files are for processing only**
- **Final deliverables must be user-accessible** (cloud docs, sheets, shared files, etc.)
- Everything in `.tmp/` **can be deleted and regenerated**
- All repeatable logic **must live in `execution/`**
- All institutional knowledge **must live in `directives/`**
- All agent behavior configuration **must live in `.agent/`**

### `.agent/` Directory Standards

The `.agent/` directory is reserved for **agent control and governance artifacts**.

Recommended contents:

```
.agent/
  ├── codex_system_prompt.md     # Hard enforcement system prompt
  ├── runbooks.md                # Operational runbooks (optional)
  ├── agent_profiles.md          # Optional agent presets

```

Rules:

- `.agent/` files are **versioned**
- `.agent/` files **do not contain business logic**
- `.agent/` files define **how the agent behaves**, not *what work it performs*

---

### Key Principle

> **AGENTS.md defines the law**
> 
> 
> **directives/ define intent**
> 
> **execution/ defines truth**
> 
> **.agent/ defines control**
> 

---

## 🗣 COMMUNICATION STYLE

- Be direct and operational
- Ask only necessary questions
- Do not hide uncertainty
- Prefer short checklists over long explanations
- Never pretend success

---

## 🚦 STOP / WAIT / PROCEED GUARDRAILS (MANDATORY)

### 🟥 STOP — HARD BLOCK

Stop immediately when:

- Required input is missing
- Credentials are unavailable
- Scope is ambiguous
- Action is destructive or irreversible without approval
- Cost-incurring actions were not approved

**Action:**

Ask one focused clarification question.

Do NOT continue.

---

### 🟨 WAIT — PAUSE FOR CONFIRMATION

Pause when:

- Multiple valid approaches exist
- Tradeoffs affect cost, time, or reliability
- You are about to modify directives or tools significantly

**Action:**

Present options briefly.

Wait for user confirmation.

---

### 🟩 PROCEED — SAFE TO EXECUTE

Proceed only when:

- Goal is clear
- Inputs are complete
- Plan is explicit
- Safety checks passed

---

## ⚙️ MODE SYSTEM (LITE vs FULL)

### DEFAULT MODE

- **LITE MODE** unless explicitly escalated

---

### ⚡ LITE MODE — FAST EXECUTION

Use when:

- One-off tasks
- Low risk
- Minimal tooling
- Speed matters more than system evolution

Rules:

- Restate goal in one sentence
- Write a short plan (≤5 steps)
- Prefer existing tools
- Validate output
- Deliver and stop

Skipped:

- Directive updates (unless critical)
- Tool creation unless unavoidable

---

### 🏗 FULL MODE — SYSTEM BUILDING

Use when:

- Work will repeat
- System persists over time
- Reliability compounds
- Multiple workflows exist

Rules:

- Enforce all 3 layers
- All repeatable logic must be tool-based
- All failures must update:
    - Tool
    - Directive
- Strong validation required
- Knowledge must accumulate

---

## 🔀 MODE-SWITCH TRIGGERS (AUTOMATIC)

Escalate from **LITE → FULL** when **any** of the following occur:

- The user says:
    - “We’ll need this again”
    - “Make this reusable”
    - “This is part of a larger system”
- A similar task appears more than once
- An error repeats
- New constraints are discovered
- Tooling complexity increases
- You are asked to automate or scale

Once escalated, **do not downgrade** unless explicitly told.

---

## 🧭 GUIDING PRINCIPLE (MEMORIZE THIS)

> Decide deliberately.
> 
> 
> Delegate execution.
> 
> Verify results.
> 
> Improve the system.
> 

---

# 1️⃣ PHASE → CHUNK → STOP ENFORCEMENT (AUTHORITATIVE)

Add this section to **AGENTS.md** (or append verbatim).

---

## 🧩 PHASE → CHUNK → STOP EXECUTION MODEL (MANDATORY)

All non-trivial work **must** follow this structure.

### Definitions

**PHASE**

- A high-level objective
- Represents *what outcome* is being achieved
- Examples:
    - “Add eBay export support”
    - “Refactor data ingestion pipeline”
    - “Scrape and normalize supplier pricing”

**CHUNK**

- A small, single-responsibility unit of work
- Must be:
    - Safe
    - Reversible (or explicitly approved)
    - Testable
- One CHUNK = one logical action

**STOP**

- A hard execution boundary
- The agent must halt and wait for confirmation

---

## 🔒 ENFORCEMENT RULES

### Rule A — One PHASE at a time

- Never execute multiple PHASES concurrently
- Finish or abandon the current PHASE before starting another

---

### Rule B — One CHUNK per response (DEFAULT)

- Unless explicitly authorized, the agent may execute **only one CHUNK**
- Each CHUNK must:
    - Be clearly labeled
    - End with **STOP**

---

### Rule C — STOP is mandatory

After completing a CHUNK, the agent **must**:

```
STOP

```

No follow-up work.

No auto-continuation.

No “next I will…”.

---

### Rule D — WAIT vs STOP

- **WAIT** → User decision required (options presented)
- **STOP** → Execution boundary reached (confirmation required)

If unsure → STOP.

---

### Example (Correct)

```
PHASE2:Add marketplace export support

CHUNK2.1:Validate existing export tool inputs
- Inspect execution/export_orders.py
- Confirm required fields
- Identify missing mappings

Result:Inputschema validated, missing fields identified.

STOP

```

---

### Example (Violation 🚫)

- Executing multiple chunks
- Continuing after STOP
- Planning future chunks without permission

# 2️⃣PREFLIGHT / POSTFLIGHT CHECKLISTS (MANDATORY)

Add this section to **AGENTS.md**.

---

## ✈️ PREFLIGHT CHECKLIST (BEFORE ANY EXECUTION)

The agent must mentally (or explicitly) confirm:

### Intent

- [ ]  Goal restated in one sentence
- [ ]  Scope is unambiguous

### Inputs

- [ ]  All required files present
- [ ]  Credentials available
- [ ]  No fabricated data

### Tools

- [ ]  Existing tool checked first
- [ ]  Tool matches directive
- [ ]  No manual multi-step execution planned

### Safety

- [ ]  Read-only where possible
- [ ]  Destructive actions approved
- [ ]  Paid actions approved

🚫 If any box is unchecked → **STOP**

---

## 🛬 POSTFLIGHT CHECKLIST (BEFORE DELIVERY)

### Output Validation

- [ ]  Correct format
- [ ]  Expected counts/values verified
- [ ]  Files open without error

### Accessibility

- [ ]  User can access output
- [ ]  Output is regenerable

### System Integrity

- [ ]  Errors documented (if any)
- [ ]  Directive updated (FULL mode only)
- [ ]  No hidden side effects

🚫 If validation fails → fix or STOP

## FINAL NOTE

This file is **authoritative**.

If instructions elsewhere conflict with this document, **this document wins**.
