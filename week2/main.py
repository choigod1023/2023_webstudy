from bson import json_util
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['JSON_AS_ASCII'] = False


@app.route('/submit', methods=['POST', 'GET'])
def arduino():
    if request.method == 'POST':
        parameter = request.form
        print(type(parameter))
        result = json.dumps(parameter, ensure_ascii=False, indent=4)
        print((result))
        return result
    else:
        parameter = request.args.to_dict()
        result = json.dumps(parameter, ensure_ascii=False, indent=4)
        print((result))
        return result


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
