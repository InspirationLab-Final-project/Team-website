from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/progress')
def progress():
    return render_template('progress.html')

@app.route('/milestones')
def milestones():
    return render_template('milestones.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
