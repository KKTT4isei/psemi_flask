from flask import Flask, render_template , request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index2.html')

@app.route("/routing.html")
def routing():
    return render_template('routing.html')

@app.route("/get.html",methods=['GET'])
def gethtml():
    request_data=request.args.get('data') 
    return render_template('get.html',request_data=request_data)

@app.route("/post.html",methods=['POST'])
def posthtml():
    request_data=request.form.get('data')
    return render_template('post.html',request_data=request_data)

if __name__ == "__main__":
    app.run(port=8080)