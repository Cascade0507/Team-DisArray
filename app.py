from flask import Flask, render_template

app = Flask(__name__)

# Sample disaster alerts data
alerts_data = [
    "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ipsam!",
    "Lorem ipsum dolor sit",
    "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ipsam!"
]

# Route to render the home page
@app.route('/')
def home():
    return render_template('index.html', alerts=alerts_data)

if __name__ == '__main__':
    app.run(debug=True)
