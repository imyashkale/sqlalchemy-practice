from sqlalchemy.engine import result
from sqlalchemy.sql import select
from sqlalchemy.sql.base import ColumnSet
from sqlalchemy.sql.expression import desc
from sqlalchemy.sql.selectable import Select
from db import conn
from models import cookies
from pprint import pprint

def querying_data():
    # 1
    stmt = select([cookies])
    result_proxy = conn.execute(stmt)
    result = result_proxy.fetchall()
    pprint("Querying Data 01 :")
    pprint(result)

    #2
    stmt_two = cookies.select()
    result_proxy_two = conn.execute(stmt_two)
    result_two = result_proxy_two.fetchall()
    pprint("Querying Data 02 :")
    pprint(result_two)

    # result proxy methods
    first_row = result_two[0] # first row
    pprint("First Row :")
    pprint(first_row)
    first_row_col = first_row[1] #  column by index
    pprint("First Row's Column :")
    pprint(first_row_col)

    # This select the column
    pprint("Access Column by column object :")
    first_col = first_row[cookies.c.cookie_name]
    pprint(first_col)

    # clist of the cookies
    cookies_available = [item.cookie_name for item in result_two]
    print(cookies_available)

    # Check what are the colums are available
    columns = first_row.keys()
    pprint("Columns Are in the row :")
    pprint(columns)

def controlling_columns():
    '''
    Selecting perticular columns.
    '''
    stmt = select([cookies.c.cookie_name, cookies.c.quantity])
    result_proxy = conn.execute(stmt)
    print("Columns are available :", result_proxy.keys())
    print("Result :", result_proxy.first())

def ordering():
    """
    Ordering the result in perticular order by the key
    """
    stmt = select([ cookies.c.cookie_name, cookies.c.quantity  ]).order_by(cookies.c.quantity)
    # stmt = select([ cookies.c.cookie_name, cookies.c.quantity  ]).order_by(cookies.c.quantity.desc())
    rp = conn.execute(stmt)
    ordered_cookies = [f" Quantity : {cookie.quantity} - Cookie Name : { cookie.cookie_name }" for cookie in rp]
    pprint("Ordered Cookie :")
    pprint(ordered_cookies)

def limiting():
    """
    Limiting the rows returned by query
    """
    LIMIT = 3
    stmt = select([cookies.c.cookie_name, cookies.c.quantity]).order_by(cookies.c.quantity.desc()).limit(LIMIT)
    rp = conn.execute(stmt)
    returned_cookies = [f" Quantity : {cookie.quantity} - Cookie Name : { cookie.cookie_name }" for cookie in rp]
    pprint("Limiting Qyury Result :")
    print(returned_cookies)


