from flask import Flask, request, jsonify

app = Flask(__name__)

def calculator(operation, num1, num2):
    if operation == '-':
        return num1 - num2

@app.route('/calculate', methods=['GET'])
def calculate():
    operation = request.args.get('operation')
    num1 = request.args.get('num1',type=float) 
    num2 = request.args.get('num2',type=float)  

    result = calculator(operation, num1, num2)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)