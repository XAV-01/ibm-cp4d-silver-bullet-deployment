import os
import warnings
import json
import sys
import select

warnings.filterwarnings("ignore")

#import traceback
#import pandas as pd

#print('Pandas version =', pd.__version__)
# print('seaborn version =', sns.__version__)

# os.system('pip install xxx.whl')

############### main code ##################
def getEnvVariables() :
    vars = {}
    for name, value in os.environ.items():
        vars[name] = value
    return vars

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
    

def predictData(json_data) :
    rawPrediction, probability, prediction, predictedLabel = [1,0],[1.0, 0.0], 0, "NO"
    include=["F", "f", "W", "w"]
    if json_data["SEXE"] in include : 
        if json_data["AGE"] > 15 and json_data["AGE"] < 50 :
            prediction = 1
            predictedLabel = "YES"
            rawPrediction, probability = [0,1],[0.0, 1.0]
    return rawPrediction, probability, prediction, predictedLabel


def processData(json_data) :
    preds_value = []
    preds_fields = []
    for i in range(len(json_data)) :
        fields = json_data[i]["fields"]
        for j in range(len(json_data[i]["values"])) :
            pred = []
            values = json_data[i]["values"][j]
            data = {}
            for k in range(len(fields)) :
                data[fields[k]] = values[k]
                pred.append(values[k])
            rawPrediction, probability, prediction, predictedLabel = predictData(data)
            pred.append(rawPrediction)
            pred.append(probability)
            pred.append(prediction)
            pred.append(predictedLabel)
            preds_value.append(pred)
            
    for k in range(len(fields)) :
        preds_fields.append( fields[k] )
    preds_fields.append("rawPrediction")
    preds_fields.append("probability")
    preds_fields.append("prediction")
    preds_fields.append("predictedLabel")

    return preds_fields, preds_value


def runCode() : 
    data = loadInputData()
    if data["status"] == "Data loaded" :
        #values = processDatas(inputData["json_data"]) 
        fields, values = processData(data["json_data"][0]["input_data"]) 
        #values = [data]

    else :
        values = [data]

    #fields =  ["AGE","SEXE","rawPrediction","probability","prediction","predictedLabel"]
    jsondata={"fields": fields, "values": values}
    json_string=json.dumps(jsondata, indent=4, ensure_ascii=False)
    print(jsondata, end='')

runCode()
