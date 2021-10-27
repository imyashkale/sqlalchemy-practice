from sqlalchemy.sql.expression import insert
from sqlalchemy.sql.functions import user
from models import cookies,users,orders,items
from db import conn

def insert_stmt():
    '''
    INSERT EXAMPLES
    '''
    # Insert 01
    stmt = cookies.insert().values(
        cookie_name="chocholate chip",
        cookie_recipe_url="http://cookie.com/1",
        cookie_sku="CC01",
        quantity="12",
        unit_cost="0.50"
    )
    result_one = conn.execute(stmt)
    print("INSERTION 01",result_one.inserted_primary_key)

    # Insert 02
    stmt = cookies.insert()
    result_two = conn.execute(
        stmt,
        cookie_name="Dark chocolate chip",
        cookie_recipe_url="http://cookie.com/dark",
        cookie_sku='CC02',
        quantity='1',
        unit_cost="0.75"
    )
    print("INSERTION 02",result_two.inserted_primary_key)

    #Insert 03
    stmt = insert(cookies).values(
        cookie_name="Extra Dark chocolate chip",
        cookie_recipe_url="http://cookie.com/extradark",
        cookie_sku='CC03',
        quantity='10',
        unit_cost="0.90"
    )
    result_three = stmt.execute()
    print("INSERTION 03",result_three.inserted_primary_key)


def multiple_insert_stmt():
    '''
    Insert Multiple .
    '''
    inventory_items = [
        {
            'cookie_name':"peanut butter",
            'cookie_recipe_url':"http://cookie.com/peanutbutter",
            'cookie_sku':'CC04',
            'quantity':'6',
            'unit_cost':"0.80"
        },
        {
            'cookie_name':"oatmeal raisin",
            'cookie_recipe_url':"http://cookie.com/oatmealraisin",
            'cookie_sku':'CC05',
            'quantity':'8',
            'unit_cost':"0.40"
        }
    ]
    stmt = cookies.insert()
    result = conn.execute(stmt, inventory_items )
    print("MULTIPLE INSERION RESULT :",result)

def prepare_for_relationship():
    rst = users.delete().execute()
    print("Cleared :", rst.rowcount)

    customers = [
        {
            'username': "cookiemon",
            'email_address': 'mon@cookie.com',
            'phone': '111-111-111',
            'password':'cookiemon#21'
        },
        {
            'username': "cakeeater",
            'email_address': 'cakeeater@cookie.com',
            'phone': '222-222-222',
            'password':'cakeeater#21'
        },
        {
            'username': "pieguy",
            'email_address': 'pieguy@cookie.com',
            'phone': '333-333-333',
            'password':'pieguy#21'
        }
    ]
    stmt = users.insert()
    rst = conn.execute(stmt, customers)
    print("User Inserted rows count :", rst.rowcount)

    stmt = insert(orders).values( user_id = 1, order_id=1 )
    rst = conn.execute(stmt)
    print("Order Created For user 01 Id 01")

    lineitems = [
        {
            'order_id': 1,
            'cookie_id': 1,
            'quantity': 2,
            'extended_cost':1.00
        },
        {
            'order_id': 1,
            'cookie_id': 3,
            'quantity': 12,
            'extended_cost':3.00
        }
    ]
    stmt = items.insert()
    rst = conn.execute(stmt, lineitems)
    print("Inserted rows count :", rst.rowcount)

    stmt = insert(orders).values( user_id=2, order_id=2 )
    rst = conn.execute(stmt)
    print("Order Created For user 02 Id 02")
    lineitems = [
        {
            'order_id': 2,
            'cookie_id': 1,
            'quantity': 24,
            'extended_cost':12.00
        },
        {
            'order_id': 2,
            'cookie_id': 4,
            'quantity': 6,
            'extended_cost':6.00
        }
    ]
    stmt = items.insert()
    rst = conn.execute(stmt, lineitems)
    print("Inserted rows count :", rst.rowcount)

