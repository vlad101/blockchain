# Blockchain

Python implementation of a Blockchain.

## Getting Started

### Test Coin

Each block has a timestamp, an index, data, hash of the previous block, a generated cryptographic hash (the block’s index, timestamp, data, and the hash of the previous block’s hash).

### Genesis Block

The genesis block, first block, is the first manually added block that has a an index 0, a current timestamp, an arbitrary data, and an arbitrary hash value of the previous block.

### Next Block

Next block function will take the previous block in the chain as a parameter, create the data for the block to be generated, and return the new block with the data. When new blocks hash information from previous blocks, the integrity of the blockchain increases with each new block.

### Test Function

Blockchain, a simple python list, is created. The first element of the list is the genesis block. The twenty succeeding blocks are added with a for loop.

### Django REST Framework

## POST /get-token/

Get token class defines the create behavior of the user token.

**POST Example:** *curl -d '{"username": "<username>","password": "<password>"}' -X POST http://localhost:8000/get-token/ -H "Content-Type: application/json"*

```
{
	"token": "1707e0e2f23bca6e1dfb90faab10bc88108c4197"
}
```

## GET /transactions/

Get class defines the get behavior of the rest api. The user has to be the owner of the transaction to have that object's permission.

**GET Example:** *curl -H "Authorization: Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197" http://localhost:8000/transactions/*

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "sender": "First1 Last1",
        "recipient": "First2 Last2",
        "amount": "999.99",
        "date_created": "2017-12-12T15:10:28.584893-05:00",
        "date_modified": "2017-12-13T10:28:56.115815-05:00"
    },
    {
        "id": 3,
        "sender": "First3 Last3",
        "recipient": "First4 Last4",
        "amount": "10.99",
        "date_created": "2017-12-13T10:33:24.726317-05:00",
        "date_modified": "2017-12-13T10:33:24.726317-05:00"
    }
]
```

Create class defines the create behavior of the rest api.

**POST Example:** *curl -H "Authorization: Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197" -d '{"sender": "First5 Last5","recipient": "First6 Last6","amount": "11.99"}' -X POST http://localhost:8000/transactions/ -H "Content-Type: application/json"*

```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 6,
    "sender": "First5 Last5",
    "recipient": "First6 Last6",
    "amount": "11.99",
    "date_created": "2017-12-13T14:26:06.001865-05:00",
    "date_modified": "2017-12-13T14:26:06.002367-05:00"
}
```

## GET /transactions/1/

Details class handles the HTTP GET, PUT and DELETE requests.

**GET Details Example:** *curl -H "Authorization: Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197" http://localhost:8000/transactions/1/*

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "sender": "First1 Last1",
    "recipient": "First2 Last2",
    "amount": "999.99",
    "date_created": "2017-12-12T15:10:28.584893-05:00",
    "date_modified": "2017-12-13T10:28:56.115815-05:00"
}
``` 

**PUT Example:** *curl -H "Authorization: Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197" -d '{"sender": "First6 Last6","recipient": "First7 Last7","amount": "11.99"}' -X PUT http://localhost:8000/transactions/14/ -H "Content-Type: application/json"*

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 6,
    "sender": "First6 Last6",
    "recipient": "First7 Last7",
    "amount": "11.99",
    "date_created": "2017-12-13T14:26:06.001865-05:00",
    "date_modified": "2017-12-13T14:33:42.657926-05:00"
}
```

**DELETE Example:** *curl -H "Authorization: Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197" -X DELETE http://localhost:8000/transactions/7/*

```
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

## Authors

* **Vladimir Efros** - *Initial work*