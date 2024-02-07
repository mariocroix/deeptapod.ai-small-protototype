import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

if not os.path.exists('pipe_in'):
    os.mkfifo('pipe_in')
if not os.path.exists('pipe_out'):
    os.mkfifo('pipe_out')

cpp_process = subprocess.Popen(['./function'], cwd='.')


@app.route('/split_sentence', methods=['POST'])
def split_sentence():
    data = request.get_json()
    sentence = data['sentence']
    with open('pipe_in', 'w') as pipe_in:
        pipe_in.write(sentence)

    words = []
    with open('pipe_out', 'r') as pipe_out:
        for line in pipe_out:
            words.append(line.strip())

    return jsonify({'words': words})


if __name__ == '__main__':
    app.run(debug=True, port='1234')

cpp_process.terminate()
os.remove('pipe_in')
os.remove('pipe_out')
