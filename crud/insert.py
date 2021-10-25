from sqlalchemy.sql.expression import insert
from models import cookies
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



