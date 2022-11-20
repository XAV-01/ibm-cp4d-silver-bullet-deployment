# Update

- Added input to score function
- online deployment is working fine


## add input to score function

Notice thet `json_string` is created from `payload` and passed to subprocess using `input=json_string`.

Changed to score function
```python
        def score(payload):
            # output = subprocess.run(["python", prj_info['main_file']], capture_output=True, text=True).stdout
            import json
            import ast
            json_string=json.dumps(payload, ensure_ascii=False)
            p = subprocess.run(["python", '-i', prj_info['main_file']], capture_output=True, input=json_string, text=True)

            stdout = p.stdout
            #print('stdout:', stdout)
            stderr = p.stderr
            #print('stdout:', stderr)

            if p.returncode:
                if send_email_when_fail:
                    ############### send email with error msg ##################
                    message = """Subject: {} Error happened\r\n
                            Receipients: {}
                            This message is sent from Cloud Pak for Data platform.
                            ### Start of Error Message ###
                            {}
                            ### End of Error Message ###""".format(date_str, receivers, stderr)
                    send_email(smtp_server, sender, receivers, message)
                return {"predictions": [{"values": ["stderr", stderr]}]}  

            else:
                if send_email_when_successful:
                    ############### send successful notification ###############
                    message = """Subject: {} Job has completed successfully\r\n
                    Receipients: {}
                    This message is sent from Cloud Pak for Data platform.
                    ### Start of Message ###
                    {}
                    ### End of Message ###""".format(date_str, receivers, stdout)
                    send_email(smtp_server, sender, receivers, message)
                json_string = "no_str"
                try :
                    jsondata = ast.literal_eval(stdout)
                    #jsondata = json.loads(json_string)
                    #values = {"predictions_2": [{"msg": [jsondata]}]} 
                    values = jsondata
                except Exception as e :
                    values = {"error": [{"msg": [stdout , json_string, " - err: " + str(e)]}]}
                return {"predictions": [values]}
                #return {"predictions": [{"values": ["v","ok" ,values]}]}  

        return score

```

In case of error stdout, json_string and err is passed int json predictions object

## online deployment 
from Deployments / space / simple_predictor_online go to Test tab

Data to predict
```json
{"input_data": [{
"fields": ["AGE","SEXE"],
"values": [
  [33,"F"],
  [59,"F"],
  [28,"M"]
]}]}
```

Prediction result
```json
{
    "predictions": [
        {
            "fields": [
                "AGE",
                "SEXE",
                "rawPrediction",
                "probability",
                "prediction",
                "predictedLabel"
            ],
            "values": [
                [
                    33,
                    "F",
                    [
                        0,
                        1
                    ],
                    [
                        0,
                        1
                    ],
                    1,
                    "YES"
                ],
                [
                    59,
                    "F",
                    [
                        1,
                        0
                    ],
                    [
                        1,
                        0
                    ],
                    0,
                    "NO"
                ],
                [
                    28,
                    "M",
                    [
                        1,
                        0
                    ],
                    [
                        1,
                        0
                    ],
                    0,
                    "NO"
                ]
            ]
        }
    ]
}
```
