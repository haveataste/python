from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "flask test<br/>Hello World!<br/>I\'m the king of the world!"
