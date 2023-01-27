#aqui se importa Flask
from flask import Flask

app=Flask(__name__)

#implementar decorador 
@app.route("/")
def index():
    return "Hola Mundo Flask cambios nuevos"

@app.route("/hola")
def hola():
    return "Hola desde hola"

@app.route("/nueva")
def nueva():
    return "Hola desde Nueva"


if __name__=="__main__":
    app.run(debug=True, port=3000)