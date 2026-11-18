from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Campus Helpdesk")
BASE_DIR = Path(__file__).resolve().parent

TIMETABLE = {
    ("CSE-A", "Monday"): [
        {"subject": "Artificial Intelligence", "time": "09:00-10:00", "room": "A101"},
        {"subject": "Database Management Systems", "time": "10:00-11:00", "room": "A102"}
    ],
    ("CSE-B", "Monday"): [
        {"subject": "Python Programming", "time": "09:00-10:00", "room": "A201"}
    ]
}
FEES = {
    "STU001": {"status": "Paid", "amount_due": 0},
    "STU002": {"status": "Pending", "amount_due": 15000}
}

@mcp.tool()
def get_timetable(batch: str, day: str) -> dict:
    """Retrieve scheduled classes for an exact batch and weekday from mock data."""
    if not batch.strip() or not day.strip():
        raise ValueError("Batch and day must be non-empty.")
    key = (batch.strip().upper(), day.strip().title())
    return {
        "batch": key[0],
        "day": key[1],
        "classes": TIMETABLE.get(key, []),
        "message": "No timetable entries found." if key not in TIMETABLE else "OK"
    }

@mcp.tool()
def get_fee_status(student_id: str) -> dict:
    """Retrieve fee status and amount due for a mock student ID only."""
    if not student_id.strip():
        raise ValueError("Student ID cannot be empty.")
    sid = student_id.strip().upper()
    if sid not in FEES:
        raise ValueError("Student ID not found in mock database.")
    return {"student_id": sid, **FEES[sid]}

@mcp.resource("hostel://rules")
def hostel_rules() -> str:
    """Read the fictional hostel rules document."""
    return (BASE_DIR / "hostel-rules.md").read_text(encoding="utf-8")

if __name__ == "__main__":
    mcp.run(transport="stdio")
