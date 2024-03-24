from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load your machine learning models
model = joblib.load('C:\\Users\\Sujay S C\\OneDrive\\Desktop\\Team-DisArray\\earthquake_model_depth.pkl')
model1 = joblib.load('C:\\Users\\Sujay S C\\OneDrive\\Desktop\\Team-DisArray\\earthquake_model_magnitude.pkl')

@app.route('/')
def index():
    # Dummy data for alerts
    alerts = ["KMC to declare disaster plot no-construction zone", "Imminent famine in nothern Gaza is 'entirely man-made disaster':Guterres"]
    return render_template('index.html', alerts=alerts)

@app.route('/predict', methods=['POST'])
def predict():
    # Get latitude and longitude from the JSON request data
    data = request.json
    latitude = data['latitude']
    longitude = data['longitude']

    # Preprocess the latitude and longitude if needed
    # For example, you may need to convert them to floats
    latitude = float(latitude)
    longitude = float(longitude)

    # Make predictions using the loaded models
    prediction = model.predict([[latitude, longitude]])
    prediction1 = model1.predict([[latitude, longitude]])

    # Return the predictions as JSON
    return jsonify({'prediction_model': prediction[0], 'prediction_model1': prediction1[0]})

if __name__ == '__main__':
    app.run(debug=True)
