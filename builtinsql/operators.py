from operator import and_, or_
from sqlalchemy.sql.elements import not_
from sqlalchemy.sql.expression import select
from sqlalchemy.sql import select
from sqlalchemy import ( cast, and_, or_, not_ )
from sqlalchemy.sql.sqltypes import Numeric
from db import conn
from models import cookies
from pprint import pprint


def operators():
    # Add
    stmt = select([cookies.c.cookie_name, 'SKU-' + cookies.c.cookie_sku])
    rows = [row for row in conn.execute(stmt)]
    print("SKU Added :")
    pprint(rows)

    # Cast
    stmt = select(
        [
            cookies.c.cookie_name,
            cast((cookies.c.quantity * cookies.c.unit_cost), Numeric(12, 2)
                ).label('inv_cost')
        ]
    )
    result = [
        f"{row.cookie_name} - {row.inv_cost}" for row in conn.execute(stmt)]
    print("Cast Result :")
    pprint(result)

    # Conjunctions - AND
    stmt = select([cookies]).where(
        and_(
            cookies.c.quantity > 5,
            cookies.c.unit_cost < 0.60
        )
    )
    rst = [
        f"Cookie Name : { row.cookie_name } - Unit Cost : {row.unit_cost} Quantity : {row.quantity}"
        for row in conn.execute(stmt)
    ]
    print("And Conjunction :")
    pprint(rst)

    # Conjuctions - OR
    stmt = select([cookies]).where(
        or_(
            cookies.c.quantity.between(0,6),
            cookies.c.cookie_name.contains('chip')
        )
    )
    rst = [ row.cookie_name for row in conn.execute(stmt) ]
    pprint("OR Conjunction :")
    pprint(rst)