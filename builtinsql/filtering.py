from operator import concat
from sqlalchemy.sql.expression import select
from db import conn
from models import cookies

def filter():
    # simple where clause
    stmt = select([ cookies ]).where(cookies.c.cookie_name == 'peanut butter')
    rp = conn.execute(stmt)
    record = rp.first()
    print("Items :",record.items())

    stmt = select([ cookies ]).where(cookies.c.cookie_name.like('%chip%'))
    rp = conn.execute(stmt)
    records = [ record.cookie_name for record in  rp.fetchall() ]
    print("Like :",records)

    stmt = select([ cookies ]).where(cookies.c.quantity.between(5, 10))
    rp = conn.execute(stmt)
    records = [ (record.quantity, record.cookie_name) for record in  rp.fetchall() ]
    print("Beetween :",records)

    # Other methods are
    # 1.concat(column_two)
    # 2.distinct()
    # 3.in_([List])
    # 4.is_(None)
    # 5.contains(string)
    # 6.endwith(string)
    # 7.like(string)
    # 8.startswith(string)
    # 9.ilike(string)