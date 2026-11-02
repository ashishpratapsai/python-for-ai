import sqlite3
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Institura Tool")

DB_PATH = Path(__file__).parent/"institura.db"

def get_db():
    """Return a connection with dict-like rows"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn



def init_db():
    """Create table and seed data. safe to run multiple times."""
    with get_db() as conn:
        #IF NOT EXISTS = don't crash if table already there
        conn.execute("""
CREATE TABLE IF NOT EXISTS students (
id      INTEGER PRIMARY KEY,
name    TEXT UNIQUE,
marks   INTEGER,
batch   TEXT,
fee     TEXT
)



""")
        # Only seed if table is empty
        count = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
        if count == 0:
            conn.executemany(
                "INSERT INTO students(name,marks,batch,fee) VALUES (?, ?, ?, ?)",
                [
                    ("rahul sharma", 85, "IIT-JEE-2026", "paid"),
                    ("amit kumar",   35, "IIT-JEE-2026", "pending"),
                    ("priya patel",  92, "NEET-2026",    "paid"),
                    ("sneha singh",  96, "NEET-2026",    "paid"),
                    ("rohan verma",  78, "IIT-JEE-2026", "pending"),
                ]
            )
        conn.commit()

# ---- MCP Resource -----

@mcp.resource("institura://students/all")
def list_all_students()->str:
    """All student names - Claude, read this before calling `get_student`."""
    with get_db() as conn:
        rows = conn.execute("SELECT name FROM students").fetchall()
    return "\n".join(row["name"] for row in rows)


# --- MCP tools ---

@mcp.tool()
def get_student(name:str)-> dict:
    """Get students' full record: written marks, batch, fee status. """
    with get_db() as conn:
        row = conn.execute(
            "SELECT * From students WHERE name = ?",
            [name.lower().strip()]
        ).fetchone()
    if row:
        return dict(row)
    return {"error": f"Student '{name}' not found. Read resource institura://students/all for valid names."}


@mcp.tool()
def update_marks(name:str, marks:int)->str:
    """Update students' marks. Marks must be between 0 and 100."""
    if not 0 <= marks <=100:
        return f"Error: marks must be 0-100, got {marks}"

    with get_db() as conn:
        result = conn.execute(
            "UPDATE students SET marks = ? Where name = ?",
            [marks, name.lower().strip()]

        )
        conn.commit()

        if result.rowcount == 0:
            return f"Error: student '{name}' not found."

    return f"Updated {name}'s marks to {marks}"


@mcp.tool()
def check_fee_status(name: str)-> str:
    """Check if a student's fees are paid or pending."""
    with get_db() as conn:
        row = conn.execute(
            "SELECT fee FROM students WHERE name =?",
            [name.lower().strip()]        
        ).fetchone()

    if row:
        return f"{name}: fee is {row['fee']}"
    return f"Student '{name}' not found"


# Init DB when server starts 
init_db()

if __name__=="__main__":
    mcp.run()




