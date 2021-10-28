from sqlalchemy import update
from models.mcookie import cookies
from db import conn

def update_row():
    stmt = update(cookies).where(
        cookies.c.cookie_name == "peanut butter"
    ).values(
        quantity=(
            cookies.c.quantity + 120
        )
    )
    rst = conn.execute(stmt)
    print("Updated Row Count :", rst.rowcount)
