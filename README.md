# Campus Helpdesk Agent Toolchain

This repository is an educational mock implementation for the assignment
“Building and Auditing an AI-Agent Toolchain”.

## Contents
- `skills/timetable-helper/`: progressive-disclosure Skill, sample CSV, references and helper script.
- `.claude-plugin/plugin.json`: plugin manifest.
- `commands/`: custom slash command.
- `hooks/`: illustrative protected-folder hook; validate output schema against the exact Claude Code release.
- `.mcp.json`: local stdio MCP server configuration.
- `mcp-server/`: Python MCP server and fictional mock data.

## Important
All campus timetable, fee and hostel data are fictional. Do not connect this demo
to real student records. The package `@nimbus/mcp-skill-bridge@2.3` was not
verified and is not used.

## Test timetable helper
```bash
python skills/timetable-helper/scripts/timetable_lookup.py CSE-A Monday
```

## Test MCP server
```bash
cd mcp-server
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mcp dev server.py
```

## Plugin marketplace
Create a separate marketplace repository and validate its marketplace manifest
against the current Claude Code plugin documentation before installation.
