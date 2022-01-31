from apps.models import Model
class dbmodel(Model):
    __table__ = 'detail_kos'
    __primary_key__ = 'link'
    __timestamps__ = False
