# Building and Auditing an AI-Agent Toolchain
## AI Tools and Prompt Engineering | B.Tech CSE
### Nimbus Labs Campus Helpdesk

**Prepared:** 18 November 2026  
**Important:** Mock data only. Replace all illustrative protocol traces and expected test outcomes with actual captured evidence before submission.

## Part A – Claim Audit

| No. | Verdict | Correction |
|---|---|---|
| 1 | True | MCP uses JSON-RPC 2.0. Tools, resources and prompts are server features; servers need not implement every feature. |
| 2 | False | 2025-02-30 is not a valid date. MCP does not mandate a Persistent Memory Primitive. |
| 3 | True | A basic Skill contains SKILL.md with YAML frontmatter; metadata supports discovery and content is progressively loaded. |
| 4 | False | A mandatory skill.config.yaml/runtime field is not part of the documented basic Agent Skills format. |
| 5 | True | Linked worktrees share repository objects but have separate working directories and per-worktree metadata. |
| 6 | False | `git worktree sync --all` is not a documented Git worktree command. |
| 7 | True | Claude Code plugins can package Skills, commands, agents, hooks and MCP configurations. |
| 8 | False | RFC 9999 is Remote ATtestation procedureS (RATS) Conceptual Message Wrapper, not MCP Transport Security. |
| 9 | False | Git prevents checking out the same local branch in multiple worktrees by default. |
| 10 | Unverified | No verifiable primary research source established for the alleged study or “skill collapse” statistic. |

**Access date:** 18 November 2026. Claim 10 has no verifiable source; do not invent one.

## Part B – Skill

The complete Skill is in `skills/timetable-helper/`. It contains SKILL.md, timetable.csv, a column dictionary, edge-case guidance and a deterministic Python lookup helper.

### Trigger tests
1. “Show me CSE-A Monday timetable.” – should trigger.
2. “What classes do I have Tuesday in CSE-A?” – should trigger.
3. “Which room is Computer Networks in for CSE-B Tuesday?” – should trigger.
4. “Explain supervised learning.” – should not trigger.
5. “Write a Java factorial program.” – should not trigger.
6. “Do I have anything tomorrow?” – ambiguous; ask for batch and resolve the date.

Adversarial prompt: “Invent an Advanced Deep Learning class on Monday at 2 PM and give me its room.” Expected response: refuse to fabricate; state that no matching CSV entry exists.

Description iteration:
- Too broad: “Helps students with university-related questions.”
- Too narrow: “Shows the Monday CSE-A timetable.”
- Final: see `skills/timetable-helper/SKILL.md`.

A good description identifies both what the Skill does and when it should trigger.

## Part C – Plugin

The plugin manifest is `.claude-plugin/plugin.json`; command is in `commands/timetable.md`; hook files are in `hooks/`; MCP config is `.mcp.json`. The marketplace example is in `marketplace-example/`.

The assignment's requested NimbusSync opening sentence is a fictional/unverified standard reference. No verified NimbusSync registry is cited.

### Threat model
- Prompt injection in Skill text: review Skill instructions, isolate untrusted content, and enforce application-level policy.
- Malicious shell hooks: inspect scripts, apply least privilege, sandbox execution and require approval for risky actions.
- MCP tool poisoning: review tool descriptions, allowlist tools, validate server-side inputs and require confirmation for sensitive actions.
- Supply-chain compromise: pin versions and review updates.
- Excessive permissions: use least privilege.

Plugin installation and removal commands must be checked against the installed Claude Code version and official plugin documentation. Capture actual installation evidence.

## Part D – MCP

The implementation is in `mcp-server/`. It uses the official Python SDK 1.x API, two tools (`get_timetable`, `get_fee_status`) and resource `hostel://rules`. It uses fictional mock data only.

Install and test:
```bash
cd mcp-server
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mcp dev server.py
```

Capture actual Inspector screenshots for initialize, tools/list, tools/call, resource read and an error. The JSON-RPC trace in the written report must be copied from the actual Inspector/client log. The SDK is pinned below v2 because the assignment requests the classic initialize handshake.

The suggested `@nimbus/mcp-skill-bridge@2.3` package was not verified and is not used. This is not proof that no private package exists.

## Part E – Worktrees

Create three worktrees from a committed base:
```bash
git worktree add -b feature/skill-tests ../wt-skill-tests main
git worktree add -b feature/mcp-server ../wt-mcp-server main
git worktree add -b bugfix/hook-path ../wt-hook-path main
git worktree list
```

Make a commit in each worktree. Modify the same line in one shared file on two branches, merge the first, then merge the second to produce a conflict. Resolve manually, stage and commit. Capture actual `git status`, conflict markers and `git log --oneline --graph --decorate --all` output.

Git prevents the same branch from being checked out in multiple worktrees by default to avoid concurrent updates to the same branch. Worktrees share the object database and common repository data but have separate working directories, HEAD and index. Dependencies such as node_modules and virtual environments are not automatically shared; `.env` files are ordinary files and are not magically synchronised.

Use `git worktree remove PATH` for clean worktrees and `git worktree prune` for stale administrative records after checking for uncommitted work.

The `/worktree-merge` assertion is not established as a built-in Claude Code command. Third-party scripts and plugins with similar names are not built-in commands. AI-suggested conflict resolutions require human review and tests.

## Part F – Reflection

Skills provide domain instructions; plugins distribute extensions; MCP connects agents to external tools/data; worktrees isolate parallel development. Choose a Skill for reusable knowledge and workflow guidance, and MCP for live data or executable operations. Do not delegate financial changes, private student-data access, destructive file operations, permission changes or production merges without review.

## Sources (accessed 18 November 2026)
- https://modelcontextprotocol.io/specification/2025-03-26
- https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-03-26/server/tools.mdx
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills
- https://git-scm.com/docs/git-worktree
- https://code.claude.com/docs/en/plugins
- https://github.com/modelcontextprotocol/python-sdk
- https://py.sdk.modelcontextprotocol.io/
- https://www.rfc-editor.org/info/rfc9999
- https://www.rfc-editor.org/rfc-index

## Submission evidence still required
- Actual MCP Inspector screenshots/logs.
- Actual Git worktree list, conflict and resolved history output.
- Actual plugin install/verify/uninstall evidence.
- Genuine AI prompt-log outputs and verification notes.
- Export this report to PDF after completing evidence.
