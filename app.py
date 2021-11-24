from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Executando o Lab"

if __name__ == '__main__':
    app.run()