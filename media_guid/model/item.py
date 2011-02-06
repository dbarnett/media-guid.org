# -*- coding: utf-8 -*-
"""Items that can be associated with a GUID"""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from media_guid.model import DeclarativeBase, metadata, DBSession


class GUIDItem(DeclarativeBase):
    __tablename__ = 'guid_items'
    #{ Columns
    
    id = Column(Integer, primary_key=True)
    
    item_type = Column(Unicode(30))
    
    contact_name = Column(Unicode(50))

    contact_email = Column(Unicode(50))

    #}
