from sqlalchemy.sql.expression import select
from db import conn
from models import cookies
from sqlalchemy.sql import func

def sum_columns_value():
    stmt = select([func.sum(cookies.c.quantity)])
    rp = conn.execute(stmt)
    sm = rp.scalar()
    print("Total cookie types :",sm)

def count():
    stmt = select([ func.count( cookies.c.cookie_name ).label("count") ])
    rp = conn.execute(stmt)
    record = rp.first()
    print("KEYS :", record.keys())
    print("Count :", record.count)