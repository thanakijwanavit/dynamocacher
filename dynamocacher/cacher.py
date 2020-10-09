from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, JSONAttribute, BinaryAttribute
import json, pickle, logging, hashlib, os, zlib, lzma
from datetime import datetime
class Cacher(Model):
  """
  cache for function
  """
  cacheKey = UnicodeAttribute(hash_key=True)
  data = JSONAttribute(default={})
  compressedData = BinaryAttribute(null=True)
  timestamp = NumberAttribute()
  def __repr__(self):
    return json.dumps({
        'cacheKey': self.cacheKey,
        'data': self.data,
        'timestamp': self.timestamp
                })

  @staticmethod
  def hashValue(inputDict:dict):
      return hashlib.sha256(json.dumps(inputDict).encode()).hexdigest()

  @classmethod
  def getCache(cls, input, timeout = 86400, verbose=False, compression = True):
    # check cache for value
    cache = next(cls.query(cls.hashValue(input)), None)
    if cache and (datetime.now().timestamp() - cache.timestamp < timeout):
      logging.debug('log found')
      if not compression:
        return cache.data
      try:
        return cls.decompress(cache.compressedData)
      except:
        logging.exception('error decompressiong, perhaps data is not compressed?')
        return cache.data
    else:
      logging.warning('cache not found or expired')
      return None
  @classmethod
  def addCache(cls, input:dict, output:dict, compression = True):
    cache = cls(
        cacheKey = cls.hashValue(input),
        data = output if not compression else {},
        timestamp = datetime.now().timestamp(),
        compressedData = cls.compress(input) if compression else None
    )
    try:
        return cache.save()
    except Exception as e:
        logging.exception(f'{e}')
  @staticmethod
  def compress(inputDict:dict,method = zlib)->bin:
    return zlib.compress(json.dumps(inputDict).encode())
  @staticmethod
  def decompress(data:bin, method = zlib)->dict:
    return json.loads(zlib.decompress(data).decode())
