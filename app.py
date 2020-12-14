from flask import Flask, request, jsonify, make_response
from model import classification
import base64
import os

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_prediction():
    # make_response(jsonify({"message": "Testing Api"}), 200)
    json = {
        "message": "Testing Api"
        }
    return json

@app.route('/', methods = ['POST'])
def post_prediction():
    response = {
        "batch": list()
    }
    json_data=request.get_json(force=True)
    batch  = json_data['batch']
    if len(batch)!=0:
        for img in batch: 
            if len(img) !=0:
                # Converting base64 into byte
                imgdata = base64.b64decode(img) 
                filename = 'image.png'
                with open(filename, 'wb') as f: 
                    # Creating Image out of byte
                    f.write(imgdata) 
                # call the function to detect leaf or not
                output = classification(filename)
                response["batch"].append(output)                 
            else:
                response["batch"].append("Empty Image String")
        return response 
    else:
        return response

if __name__ == '__main__':
   app.run(debug = True)