from datetime import datetime
from sqlalchemy import Table
from sqlalchemy.sql.schema import Column, ForeignKey, MetaData
from sqlalchemy.sql.sqltypes import DateTime, Integer, Numeric, String
from db import conn


metadata  = MetaData(bind=conn)

cookies = Table(
    'cookies',
    metadata,
    Column('cookie_id',Integer(),primary_key=True),
    Column('cookie_name',String(50),index=True),
    Column('cookie_recipe_url',String(255)),
    Column('cookie_sku',String()),
    Column('quantity',Integer()),
    Column('unit_cost',Numeric(12,2))
)

users = Table(
    'users',
    metadata,
    Column('user_id',Integer(),primary_key=True),
    Column('customer_number',Integer(),autoincrement=True),
    Column('username',String(15),nullable=True,unique=True),
    Column('email_address',String(25),nullable=False),
    Column('phone',String(20),nullable=False),
    Column('password',String(25),nullable=False),
    Column('created_on',DateTime(),default=datetime.now),
    Column('updated_on',DateTime(),default=datetime.now, onupdate=datetime.now)
)

orders = Table(
    'orders',
    metadata,
    Column('order_id',Integer(),primary_key=True),
    Column('user_id',ForeignKey('users.user_id'))
)

items = Table(
    'items',
    metadata,
    Column('item_id',Integer(),primary_key=True),
    Column('order_id',ForeignKey('orders.order_id')),
    Column('cookie_id',ForeignKey('cookies.cookie_id')),
    Column('quantity',Integer()),
    Column('extended_cost',Numeric(12,2))
)
metadata.drop_all()
metadata.create_all()