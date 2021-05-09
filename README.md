# dynamocacher
## Description
A package which allows you to use dynamodb to cache output of a slow or expensive function,
to reduce cost and increase the efficiency

Dax is supported using a Pynamodb fork, and its highly recommended for performance-critical application
50-100x performance difference is expected with dax

## ToDos
- Dax support  : Done
- Auto create table : Done
- policy template : in progress
- example readme : Done



# Examples
[colabNotebook](https://colab.research.google.com/drive/1Uf1deNZ0P1tAiKjeKLs0ErqexYtd1ZGb?usp=sharing)

## SampleUsage

### cache this slow function

```python
def power(input:dict):
  ''' 
  This is a very bad and slow function
  accept a dict containing these keys
    base: float
    power: int
  and return the power embarrasingly slowly
  response
    result: float
  '''
  base = input['base']
  power = input['power']
  result = base
  for i in range (power):
    result *= base
  return {
      'result':result
  }

def powerWithCaching(input:dict):
  cache = Cache.getCache(input, timeout = 3600)
  if cache: return cache
  result = power(input)
  Cache.addCache(input=input, output= result)
  return result
```

### performance
Example code for trying it yourself

```python
sampleInput = {
    'base':  1 + 1e-10,
    'power': 86289369
}

%timeit power(sampleInput) # 3.72 s ± 35 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
%timeit powerWithCaching(sampleInput) # 238 ms ± 482 µs without dax
%timeit powerWithCaching(sampleInput) # 5.43 ms with dax
```



## SetUp

```python
from dynamocacher.cacher import Cacher

class Cache(Cacher):
  class Meta:
      table_name = 'dynamoCache'
      region = 'us-east-1'
      aws_access_key_id = USER
      aws_secret_access_key = PW
      billing_mode= 'PAY_PER_REQUEST'
      dax_read_endpoints = ['....:8111'] # optional dax, note that dax will speed up dynamodb significantly
      dax_write_endpoints = ['....:8111']# optional dax, note that dax will speed up dynamodb significantly
```

### createTable
```python
Cache.create_table()
```
## basic

### addCache

```python
sampleInput = {
    'query': 'testQuery',
    'fruit': 'strawberry'
}
Cache.addCache(
    input = sampleInput,
    output = sampleReturn
)

```


### getCache

```python
output = Cache.getCache(sampleInput, timeout = 3600) # ignore cache older than 3600 seconds
```


## creating a table with sam
```yaml
  Properties:
  TableName: dynamoCache
  PrimaryKey:
    Name: cacheKey
    Type: String
  Tags:
    Department: Engineering
    AppType: Serverless
```