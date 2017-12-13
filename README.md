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

## GET /transactions/

Create class defines the create behavior of the rest api.

**GET Example:** *curl http://localhost:8000/transactions/?format=json*

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

**POST Example:** *curl -d '{"sender": "First5 Last5","recipient": "First6 Last6","amount": "11.99"}' -X POST http://localhost:8000/transactions/ -H "Content-Type: application/json"*

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

**GET Details Example:** *curl http://localhost:8000/transactions/1?format=json*

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

**PUT Example:** *curl -d '{"sender": "First6 Last6","recipient": "First7 Last7","amount": "11.99"}' -X PUT http://localhost:8000/transactions/6/ -H "Content-Type: application/json"*

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

**DELETE Example:** *curl -X DELETE http://localhost:8000/transactions/7/*

```
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

## Authors

* **Vladimir Efros** - *Initial work*