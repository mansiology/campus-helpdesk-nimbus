import json
import sys
from pathlib import Path

try:
    payload = json.load(sys.stdin)
    target_text = payload.get("tool_input", {}).get("file_path", "")
    if not target_text:
        raise ValueError("Missing target path")
    target = Path(target_text).resolve()
    protected = (Path.cwd() / "protected").resolve()
    if target == protected or protected in target.parents:
        # Verify this response schema against the Claude Code hook docs
        # for the exact CLI version before deploying.
        print(json.dumps({
            "decision": "block",
            "reason": "Writing to the protected folder is prohibited."
        }))
    sys.exit(0)
except Exception:
    print(json.dumps({
        "decision": "block",
        "reason": "Unable to validate requested file path."
    }))
    sys.exit(0)
