from flask import Flask, request, jsonify

app = Flask(__name__)

def alkuluku(luku):
    if luku < 2:
        return False
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            return False
    return True

@app.route("/alkuluku/<int:luku>")
def tarkista_luku(luku):
    tulos = alkuluku(luku)
    vastaus = {
        "Number": luku,
        "isPrime": tulos
    }
    return jsonify(vastaus)

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)