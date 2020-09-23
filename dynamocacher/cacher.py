from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, JSONAttribute
import json, pickle, logging, hashlib, os
from datetime import datetime
class Cacher(Model):
  """
  cache for function
  """
  cacheKey = UnicodeAttribute(hash_key=True)
  data = JSONAttribute(default={})
  timestamp = NumberAttribute()
  def __repr__(self):
    return json.dumps({
        'cacheKey': self.cacheKey,
        'data': self.data,
        'timestamp': self.timestamp
                })
  def __init__(self, tableName = 'initName', user= None, pw = None, **kwargs):
    self.Meta.table_name = tableName
    if user and pw:
      self.Meta.aws_access_key_id = user
      self.Meta.aws_secret_access_key = pw

    super().__init__(**kwargs)
  @staticmethod
  def hashValue(inputDict:dict):
      return hashlib.sha256(json.dumps(inputDict).encode()).hexdigest()

  @classmethod
  def getCache(cls, input, timeout = 86400):
    # check cache for value
    cache = next(cls.query(cls.hashValue(input)), None)
    if cache and (datetime.now().timestamp() - cache.timestamp < timeout):
      print('cache found')
      return cache.data
    else:
      print('cache not found or expired')
      return None
  @classmethod
  def addCache(cls, input:dict, output:dict):
    cache = cls(
        cacheKey = cls.hashValue(input),
        data = output,
        timestamp = datetime.now().timestamp()
    )
    return cache.save()
