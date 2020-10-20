import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():   
    m = 50
    n = 0
    n1 = 1
    e = 0
    cont = "0, 1,"

    for e in range(e, m):
        x = n1
        n1 = n1 + n
        n = x
        e = e + 1
        cont += str(n1) + ","

    return cont

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)