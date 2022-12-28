from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    array =[0,1,2,3,4,5,6,7,8,9]
    sukinano = {'ゲーム' : 'BATTLEFIELD' , '車' : 'WRX STI', 'アーティスト' : 'サカナクション'}
    return render_template('index.html',array=array,sukinano=sukinano)
    
if __name__ == "__main__":
    app.run(port=8080)