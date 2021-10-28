from operator import and_
from pprint import pprint
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import func, user
from db import conn
from models.mcookie import cookies,users,items,orders
from models.memployee import employee



def perform_join():
    '''
        join & outerjoin methods

    '''
    clms = [
        orders.c.order_id,
        users.c.username,
        users.c.phone,
        cookies.c.cookie_name,
        items.c.quantity,
        items.c.extended_cost
    ]
    cookiemon_orders = select(clms).select_from(
        orders.join(users).join(items).join(cookies)
    ).where(
        users.c.username == 'cookiemon'
    )
    rst = conn.execute(cookiemon_orders).fetchall()
    pprint(rst[0].keys())
    rst = [ row for row in rst ]
    pprint(rst)

    #USING THE OUTER JOIN TO SELECT FROM MULTIPLE TABLES
    clms = [
        users.c.username,
        func.count(orders.c.order_id)
    ]
    all_orders = select(clms).select_from(
        users.outerjoin(orders)
    ).group_by(
        users.c.username
    )
    rst = conn.execute(all_orders).fetchall()
    rst = [row for row in rst ]
    pprint("OUTER JOIN RESULT :")
    pprint(rst)


def perform_aliases():
    manager = employee.alias('mgr')
    stmt = select([employee.c.name],
        and_(employee.c.manager_id == manager.c.id,
            manager.c.name == 'Fred'
        )
    )
    pass