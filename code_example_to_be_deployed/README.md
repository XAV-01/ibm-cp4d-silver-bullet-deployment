# Update

- Getting input to score function

## get input from score function

loadInputData function
```python
 def loadInputData() : 
    data_len = 0
    json_data = []
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        data1 = sys.stdin.readlines()
        try:
            data_len = len(data1)
            for i in range(len(data1)) : 
                _json_data = json.loads(data1[i])
                json_data.append(_json_data)
            msg = "Data loaded"
        except Exception as e :
            msg = "Err loading data :" + str(e)
            json_data = data1
    else:
        msg = "No data"
    #jsondata={"values": [[33,"F",data,json_data,[1,33],[9,41],[0.18,0.82],1,"O"]]}
    jsondata={"status": msg, "json_data" : json_data, "data_len":data_len}
    return jsondata
    
```

The rest of the code illustrate how to make a simple prdiction and return the result
