# pynamoCacher
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
class Cache(Cacher):
  class Meta:
      table_name = 'dynamoCache'
      region = 'us-east-1'
      aws_access_key_id = USER
      aws_secret_access_key = PW
      billing_mode= 'PAY_PER_REQUEST'
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
output = Cache.getCache(sampleInput)
print(output)
```

```json
{"pine": "apple"}
```
