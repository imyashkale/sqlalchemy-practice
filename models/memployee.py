from sqlalchemy.schema import Table
from sqlalchemy.sql.schema import Column ,ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, Numeric, String
from models.mcookie import metadata


employee = Table(
    'employee',
    metadata,
    Column('id',Integer,primary_key=True),
    Column('manager',None,ForeignKey('employee.id')),
    Column('name',String(255))
)

