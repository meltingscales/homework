# easy-python-stock-api

For this homework, you're going to consume API data from a simple API, and make a chart of it.

## Running the server

2. Run:

```bash
    python easy-python-stock-api/stockTradingServer.py
    # then, visit http://localhost:8000/ to check if the stock API is working.
```

## Completing the homework

See `./easy-python-stock-api/homework.py` and fill it in. Run it to check to see if you've done it correctly. Graphs should pop up.

I recommend using Postman to test out the Web API if you're not familiar.

## Extra Credit

Add 4 more stock endpoints to the `stockTradingServer.py`!

## Extra Extra Credit

Add date time stamps for each stock, along with the dollar cost. Make sure the reporting still works.

Example:

```py
'TSLA': [
    [100.0, '04-16-25'],
    [105.0, '04-17-25'], 
    [102.5, '04-18-25'], 
    [101.8, '04-19-25']
],
```

This will necessitate changing the function signatures and the reporting functions within `./easy-python-stock-api/homework.py` as well.