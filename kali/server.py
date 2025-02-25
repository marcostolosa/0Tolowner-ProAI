from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_command():
    command = request.json.get('command')
    try:
        # Executa o comando no shell
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return jsonify({"result": result.stdout, "error": result.stderr}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  