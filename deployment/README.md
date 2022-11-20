# Update

- Added input to score function
- online deployment is working fine

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
