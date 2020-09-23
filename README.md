# dynamocacher
## Description
A package which allows you to use dynamodb to cache 

## ToDos
- Dax support
- Auto create table
- policy template
- example readme



# Examples

[colabNotebook](https://colab.research.google.com/drive/1Uf1deNZ0P1tAiKjeKLs0ErqexYtd1ZGb?usp=sharing)

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
```
## createTable
```python
Cache.create_table()
```

## addCache

```python
sampleInput = {
    'query': 'testQuery',
    'fruit': 'strawberry'
}
sampleInput2 = {
    'query': 'testQuery',
    'fruit': 'orange'
}
sampleReturn = {
    'pine': 'apple'
}

Cache.addCache(
    input = sampleInput,
    output = sampleReturn
)

```


## getCache

```python
output = Cache.getCache(sampleInput, timeout = 3600) # ignore cache older than 3600 seconds
print(output)
```

```json
{"pine": "apple"}
```
