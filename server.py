from flask import Flask

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir une route pour la page principale
@app.route('/')
def hello_world():
    return "<h1>Hello, World!</h1>"

# Lancer le serveur web
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)