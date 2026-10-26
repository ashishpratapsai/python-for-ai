from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Institura Tools")

STUDENTS = {
    "rahul sharma": {"marks": 85, "batch": "IIT-JEE-2026", "fee": "paid"},
    "amit kumar": {"marks": 35, "batch": "IIT-JEE-2026", "fee": "pending"},
    "priya patel": {"marks": 92, "batch": "NEET-2026", "fee": "paid"},
    "sneha singh": {"marks": 96, "batch": "NEET-2026", "fee": "paid"},
    "rohan verma": {"marks": 78, "batch": "IIT-JEE-2026", "fee": "pending"},
}


@mcp.tool()
def add(a:int, b:int)-> int:
    """Add two numbers together"""
    return a+b

@mcp.tool()
def get_student(name:str)-> dict:
    """Get student record by name Return marks, batch, and fee status"""
    key = name.lower().strip()
    if key in STUDENTS:
        return STUDENTS[key]
    return {"error": f"Student'{name}' not found"}


@mcp.tool()
def check_fee_status(name: str) -> str:
    """Check if student fee is Paid or pending"""

    key = name.lower().strip()
    if key in STUDENTS:
        status = STUDENTS[key]["fee"]
        return f"{name}: fee is {status}"
    return f"Student '{name}' not found"


if __name__=="__main__":
    mcp.run()
