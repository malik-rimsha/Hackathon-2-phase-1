---
id: 1
title: Update Constitution
stage: constitution
date: 2025-01-01
surface: agent
model: Qwen
feature: none
branch: main
user: smc
command: /sp.constitution
labels: ["constitution", "setup", "hackathon"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/memory/constitution.yaml
 - .specify/templates/plan-template.md
 - .specify/templates/spec-template.md
 - .specify/templates/tasks-template.md
 - README.md
tests:
 - null
---

## Prompt

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.


/sp.constitution You are an expert in agentic development using Spec-Kit Plus. Your task is to generate a titution File" for a hackathon project: a basic in-memory Todo console application in Python.

The constitution should be a YAML file that defines:
- High-level project guidelines and rules for AI agents.
- Development principles (e.g., clean code, no manual coding).
- Workflow rules: How to interpret specs, generate plans, break into tasks, and implement code.
- Constraints: Use Python 3.13+, UV "Consfor packaging, in-memory storage only.
- Feature requirements: Exactly the 5 basic features (Add task with title/desc, View all tasks with status, Update task details, Delete by ID, Mark complete/incomplete).
- Error handling and best practices: Input validation, modular code structure.
- Iteration rules: How to handle spec updates and store history.

Structure the output as a valid YAML file named "constitution.yaml". Include sections like:
- project_overview
- development_principles
- agent_workflow
- technology_constraints
- feature_specifications
- deliverables_guidelines

Ensure the constitution enforces spec-driven development: Agents must only generate code based on specs, plans, and tasks. No external dependencies beyond Python stdlib. Make it concise yet comprehensive for guiding Spec-Kit Plus agents.

Output only the YAML content, nothing else.

## Response snapshot

I'll help you create a constitution file for your hackathon project. First, let me check if there's an existing constitution template at the expected location.

Now I'll create a constitution YAML file for your hackathon project based on the requirements. I'll generate the content as requested:

[Constitution YAML content was created]

Now that I've created the constitution.yaml file, I need to update the existing constitution template (.md file) with specific values as required by the instructions. Let me update the template with appropriate content for your hackathon project:

[Constitution.md file was updated with specific content]

Now I'll check for any template files that might need updates to align with the new constitution:

[Plan-template.md was updated]

[Spec-template.md was updated]

[Tasks-template.md was updated]

[README.md was updated]

[All templates were verified to align with the constitution]

## Outcome

- ✅ Impact: Created constitution.yaml and updated constitution.md with specific values for the Todo Console Application project, and aligned all related templates
- 🧪 Tests: No tests required for this configuration task
- 📁 Files: 6 files updated (.specify/memory/constitution.md, .specify/memory/constitution.yaml, .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md, README.md)
- 🔁 Next prompts: Implementation of the Todo application based on the constitution
- 🧠 Reflection: The constitution now properly defines the project guidelines, development principles, workflow rules, technology constraints, and feature specifications for the Todo Console Application project.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementing the Todo application based on the constitution