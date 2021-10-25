from models import cookies
from db import conn

ins = cookies.insert().values(
    cookie_name="chocholate chip",
    cookie_recipe_url="http://cookie.com/1",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
)

r = conn.execute(ins)

print(r)
