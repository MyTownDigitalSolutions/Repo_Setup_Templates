## Purpose

Describe **what this directive accomplishes** and **why it exists**.
One paragraph max.

---

## Trigger Conditions

When should this directive be used?

- User requests X
- System encounters Y
- Workflow requires Z

---

## Inputs

List all required inputs.
Be explicit.

- Files:
- URLs:
- Credentials:
- Environment variables:
- User-provided parameters:

🚫 Do not guess missing inputs.

---

## Outputs

Describe the expected outputs.

- Format:
- Location:
- Accessibility (cloud/local):
- Validation criteria:

---

## Execution Tools

List deterministic tools/scripts to use **in order**.

1. execution/<tool_name>.py
2. execution/<tool_name>.py

If no tool exists, STOP and request permission before creating one.

---

## Step-by-Step Flow

High-level steps only (no implementation details).

1. Validate inputs
2. Execute tool A
3. Verify output
4. Deliver result

---

## Edge Cases & Constraints

Document known issues, limits, or special handling.

- API rate limits
- Data inconsistencies
- Known failure modes

---

## Validation Checklist

- [ ]  Output format correct
- [ ]  Counts / identifiers verified
- [ ]  Files open successfully
- [ ]  User-accessible

---

## Failure Learnings (Living Section)

Append-only.

- Date:
- What failed:
- Root cause:
- Fix applied:
- Preventive update:
