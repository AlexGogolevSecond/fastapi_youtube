
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey


metadata = MetaData()

roles = Table(
    'roles',
    metadata
)


