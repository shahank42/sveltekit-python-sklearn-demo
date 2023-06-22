from flask import Flask
from flask import request
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)


def predict_xor(val1, val2):
    X = np.array([[val1, val2]])
    model_file_path = "ai/xor_model"
    model = pickle.load(open(model_file_path, "rb"))
    result = model.predict(X)
    return result[0]


@app.route("/xor", methods=["POST"])
def xor():
    if request.method == "POST":
        vals = request.get_json(force=True)
        prediction = predict_xor(int(vals["val1"]), int(vals["val2"]))
        return str(prediction)
    

if __name__ == "__main__":
    app.run(debug=True)