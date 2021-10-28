from sqlalchemy import delete
from sqlalchemy.sql.expression import select
from models.mcookie import cookies
from db import conn

def delete_row():
    stmt = delete(cookies).where( cookies.c.cookie_name == "oatmeal raisin" )
    rst = conn.execute(stmt)
    print("Row count found and deleted :", rst.rowcount)

    stmt = select([cookies]).where(cookies.c.cookie_name == "oatmeal raisin" )
    rst = conn.execute(stmt)
    print("Rows Found :", rst.rowcount)