from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app) 

model = joblib.load("training_model.pkl")

@app.route('/recommend-training', methods=['POST'])
def recommend_training():
    try:
        data = request.json

        features = [[
            float(data.get('subject_knowledge', 0)),
            float(data.get('engagement', 0)),
            float(data.get('management', 0)),
            float(data.get('preparedness', 0)),
            float(data.get('professionalism', 0))
        ]]

        prediction = model.predict(features)[0]

        return jsonify({"recommended_training": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Required for AWS EB(WSGI servers)
application = app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
