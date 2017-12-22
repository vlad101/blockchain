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

## Django REST Framework

### POST /get-token/

Get token class defines the create behavior of the user token.

**POST Example:** *curl -d '{"username": "<username>","password": "<password>"}' -X POST http://localhost:8000/get-token/ -H "Content-Type: application/json"*

```
{
	"token": "1707e0e2f23bca6e1dfb90faab10bc88108c4197"
}
```

### GET /blocks/

Get class defines the get behavior of the rest api. The user does not have to be the owner of the block to have that object's permission.

**GET Example:** *curl -H "Authorization: Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197" http://localhost:8000/blocks/*

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id":119,
        "index":0,
        "timestamp":"2017-12-19T12:24:48.131787-05:00",
        "data":"Genesis Block",
        "previous_hash":"0",
        "current_hash":"f75700d932d78fbe6ddd6b65dd7f7f4c33c918c42aef8b4ca75eb5e8f203324b",
        "date_modified":"2017-12-19T12:24:48.172470-05:00",
        "proof_of_work":0,
        'transactions': [52]
    },{
        "id":120,
        "index":1,
        "timestamp":"2017-12-19T12:24:48.197535-05:00",
        "data":"Hey! I'm block 1",
        "previous_hash":"f75700d932d78fbe6ddd6b65dd7f7f4c33c918c42aef8b4ca75eb5e8f203324b",
        "current_hash":"b1da780197d1039d925cbb551993d3b771505598b78b3f113f655024050946d0",
        "date_modified":"2017-12-19T12:24:48.230623-05:00",
        "proof_of_work":0,
        "transactions": [53, 54, 55]
    }
]
```

Create class defines the create behavior of the rest api.

**POST Example:** *curl -H "Authorization: Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197" -d '{"data": "New block"}' -X POST http://localhost:8000/blocks/ -H "Content-Type: application/json"*

```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id":143,
    "index":2,
    "timestamp":"2017-12-19T15:59:48.660301-05:00",
    "data":"New block",
    "previous_hash":"5ff621016cb6f10f4b614b45907c49d3310f20460e21e66dd5adb79d75adc41e",
    "current_hash":"77e84db2bd9d109ae3577f8c6f3aeb6898bdb7423ff2d567d6d99b4f76f36027",
    "date_modified":"2017-12-19T15:59:48.660301-05:00",
    "proof_of_work":0,
    "transactions": []
}
```

### GET /blocks/142/

Details class handles the HTTP GET, PUT and DELETE requests.

**GET Details Example:** *curl -H "Authorization: Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197" http://localhost:8000/blocks/142/*

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{       
    "id":142,
    "index":1,
    "timestamp":"2017-12-19T15:55:21.584692-05:00",
    "data":"I am Block",
    "previous_hash":"93676761b7487714920aba0781628af8f0e18ae1932050c8d1cf911d3d7be09a",
    "current_hash":"5ff621016cb6f10f4b614b45907c49d3310f20460e21e66dd5adb79d75adc41e",
    "date_modified":"2017-12-19T15:55:21.584692-05:00",
    "proof_of_work":0,
    "transactions": []
}
``` 

**PUT Example:** *curl -H "Authorization: Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197" -d '{"data": "Updated Block"}' -X PUT http://localhost:8000/blocks/142/ -H "Content-Type: application/json"*

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id":142,
    "index":1,
    "timestamp":"2017-12-19T15:55:21.584692-05:00",
    "data":"Updated Block",
    "previous_hash":"93676761b7487714920aba0781628af8f0e18ae1932050c8d1cf911d3d7be09a",
    "current_hash":"34f1a46cb39c278ab8c4ba06e190eb1c72862c06c647cf14599e5d6c35ee57f0",
    "date_modified":"2017-12-19T16:05:36.593024-05:00",
    "proof_of_work":0,
    "transactions": []
}
```

**DELETE Example:** *curl -H "Authorization: Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197" -X DELETE http://localhost:8000/blocks/142/*

```
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

### GET /blocks/add/10/

Details class handles the HTTP GET, PUT and DELETE requests.

**GET Example:** *curl -H "Authorization: Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197" http://localhost:8000/blocks/add/10/*

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
        "detail":"10 blocks added successfully"
}
```

### GET /transactions/

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
        "block":173,
        "sender": "First1 Last1",
        "recipient": "First2 Last2",
        "amount": "999.99",
        "owner":"vladefros",
        "date_created": "2017-12-12T15:10:28.584893-05:00",
        "date_modified": "2017-12-13T10:28:56.115815-05:00"
    },
    {
        "id": 3,
        "block":174,
        "sender": "First3 Last3",
        "recipient": "First4 Last4",
        "amount": "10.99",
        "owner":"vladefros",
        "date_created": "2017-12-13T10:33:24.726317-05:00",
        "date_modified": "2017-12-13T10:33:24.726317-05:00"
    }
]
```

Create class defines the create behavior of the rest api.

**POST Example:** *curl -H "Authorization: Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197" -d '{"sender": "First5 Last5","recipient": "First6 Last6","amount": "11.99", "block": 177}}' -X POST http://localhost:8000/transactions/ -H "Content-Type: application/json"*

```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 6,
    "block": 177,
    "sender": "First5 Last5",
    "recipient": "First6 Last6",
    "amount": "11.99",
    "owner":"vladefros",
    "date_created": "2017-12-13T14:26:06.001865-05:00",
    "date_modified": "2017-12-13T14:26:06.002367-05:00"
}
```

### GET /transactions/1/

Details class handles the HTTP GET, PUT and DELETE requests.

**GET Details Example:** *curl -H "Authorization: Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197" http://localhost:8000/transactions/1/*

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "block":174,
    "sender": "First1 Last1",
    "recipient": "First2 Last2",
    "amount": "999.99",
    "owner":"vladefros",
    "date_created": "2017-12-12T15:10:28.584893-05:00",
    "date_modified": "2017-12-13T10:28:56.115815-05:00"
}
```

**PUT Example:** *curl -H "Authorization: Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197" -d '{"sender": "First6 Last6","recipient": "First7 Last7","amount": "11.99","block":174}' -X PUT http://localhost:8000/transactions/14/ -H "Content-Type: application/json"*

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 6,
    "block":174,
    "sender": "First6 Last6",
    "recipient": "First7 Last7",
    "amount": "11.99",
    "owner":"vladefros",
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