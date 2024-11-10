from flask import Flask, jsonify
import pandas as pd
import json
import os

app = Flask(__name__)

battingDataframesDir = "csvs/iplsite/batting/dataframes"
battingJsonDir = "csvs/iplsite/batting/"

auctionDataDir = "csvs/iplsite/batting/dataframes"


def convertToJson(baseDir, jsonDir):

    os.makedirs(jsonDir, exist_ok=True)

    for filename in os.listdir(baseDir):
        if filename.endswith(".csv"):
            filePath = os.path.join(baseDir, filename)
            dataFrame = pd.read_csv(filePath)
            jsonData = dataFrame.to_json(orient="records", date_format="epoch", double_precision=10, force_ascii=True, date_unit="ms")
            splittedFileName = filename.split('_')
            jsonFilename = f"{splittedFileName[1]}.json"
            jsonFilePath = os.path.join(jsonDir, jsonFilename)
            
            with open(jsonFilePath, 'w') as jsonFile:
                json.dump(json.loads(jsonData), jsonFile, indent=4)


@app.route('/batting/<year>')
def battingStats(year):
    directory = "csvs\\iplsite\\batting\\json"
    jsonFilename = f"{year}.json"
    jsonFilePath = os.path.join(directory, jsonFilename)
    
    if os.path.exists(jsonFilePath):
        with open(jsonFilePath, 'r') as jsonFile:
            battingStatsData = json.load(jsonFile)
        return jsonify(battingStatsData)
    else:
        return jsonify({"error": "File not found"}), 404
    

@app.route('/auction/<year>')
def auctionData(year):
    pass
    

if __name__ == '__main__':
    app.run(debug=True)


def newData():
    convertToJson(battingDataframesDir, battingJsonDir)
    convertToJson()



if __name__ == '__main__':
    app.run(debug=True)