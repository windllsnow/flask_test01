from flask import  Flask,render_template
app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/blog")
def blog():
    return "<p>b11111111111111!</p>"

@app.route("/blog2")
def blog2():
    return "<p>b2222222222222!</p>"

if __name__ == '__main__':
    app.run()

