from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load your machine learning models
model = joblib.load('C:\\Users\\Sujay S C\\OneDrive\\Desktop\\Team-DisArray\\earthquake_model_depth.pkl')
model1 = joblib.load('C:\\Users\\Sujay S C\\OneDrive\\Desktop\\Team-DisArray\\earthquake_model_magnitude.pkl')
model2 = joblib.load('C:\\Users\\Sujay S C\\OneDrive\\Desktop\\Team-DisArray\\tsunami_model.pkl')

@app.route('/')
def index():
    # Dummy data for alerts
    alerts = ["Alert 1", "Alert 2", "Alert 3"]
    return render_template('index.html', alerts=alerts)

@app.route('/predict', methods=['POST'])
def predict():
    # Get latitude and longitude from the JSON request data
    data = request.json
    latitude = data['latitude']
    longitude = data['longitude']
    print(latitude)
    # Preprocess the latitude and longitude if needed
    # For example, you may need to convert them to floats
    latitude1 = int(latitude)
    longitude1 = int(longitude)

    # Make predictions using the loaded models
    prediction = model.predict([latitude1, longitude1])
    prediction1 = model1.predict([latitude1, longitude1])
    prediction2 = model2.predict([latitude1, longitude1])

    # Return the predictions as JSON
    return jsonify({'prediction_model': prediction[0], 'prediction_model1': prediction1[0], 'prediction_model2': prediction2[0]})

if __name__ == '__main__':
    app.run(debug=True)
