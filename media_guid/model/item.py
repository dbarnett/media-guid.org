# -*- coding: utf-8 -*-
"""Items that can be associated with a GUID"""

import random
import uuid

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from media_guid.model import DeclarativeBase, metadata, DBSession

def sequence_encode(n, L):
    encoded = []
    while n != 0:
        n, i = divmod(n, len(L))
        encoded.insert(0, L[i])
    return encoded

def format_with_colons(chars):
    chars = list(chars)
    segments = []
    while len(chars) > 0:
        c2 = chars.pop(-1)
        c1 = (chars.pop(-1) if len(chars) > 0 else '0')
        segments.insert(0, c1+c2)
    return ':'.join(segments)

zero_to_9_a_to_z = [chr(i) for i in range(ord('0'), ord('9')+1) + range(ord('a'), ord('z')+1)]

def get_media_id(context):
    n = uuid.uuid4().int
    return format_with_colons(sequence_encode(n, zero_to_9_a_to_z))

class GUIDItem(DeclarativeBase):
    __tablename__ = 'guid_items'
    #{ Columns
    
    id = Column(Unicode(40), primary_key=True, default=get_media_id)
    
    item_name = Column(Unicode(80))

    item_description = Column(Unicode)

    item_type = Column(Unicode(30))
    
    contact_name = Column(Unicode(50))

    contact_email = Column(Unicode(50))

    #}
