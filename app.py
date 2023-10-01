from flask import Flask, request, jsonify
from gramformer import Gramformer
from autocorrect import Speller
import subprocess

app = Flask(__name__)

def process(text):
    gf = Gramformer(models=1, use_gpu=False)
    spell = Speller()
    corrected = spell(text)
    ans = ""
    res = gf.correct(corrected)
    for ele in res:
        ans += ele
    return ans

@app.route('/', methods=["POST"])
def post():
    data = request.get_json()
    res = process(data["text"])
    return res

if __name__ == '__main__':
    command = "python3 -m spacy download en"
    subprocess.call(command, shell=True)
    app.run()
