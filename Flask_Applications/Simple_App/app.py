from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template("index.html")
   
'''@app.route('/greet',methods=["POST","GET"])
def greet():
    if request.method == "GET":
        name = request.args.get("name","World")
        return render_template("index.html")
    else:
        name = request.form.get("name","World")
        return render_template("greet.html",name=name)'''
        
        
registrants = {}

def debug():
    print(registrants)
    return

@app.route('/list',methods=["POST"])
def list_registrants():
    debug()
    return render_template("list.html",regs =list(registrants.keys()))

@app.route('/registar')
def registar():
    name = request.get.get("name")
    level = request.get.get("level")
    registrants[name] = 0
    debug()
    return render_template("registar.html")
    
#if __name__=="__main__":
#  app.run(debug=True)
