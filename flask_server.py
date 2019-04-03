from flask import Flask, render_template, url_for, jsonify, request
import mnist_number

# 멀티스레드 라이브러리
import multiprocessing as mp
from threading import Thread

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/ml_result/<filename>')
def ml_result(filename):
    return filename

@app.route('/mnist_number')
def route_mnist_number():
    return render_template('mnist_number.html')

@app.route('/mnist_number/_ajax/train')
def route_train():
    print('hi')
    train_set_size = request.args.get('train_set_size', 5000, type=int)
    learning_rate = request.args.get('learning_rate', 0.1, type=float)
    train_steps = request.args.get('train_steps', 2500, type=int)
    batch_test_set_size = request.args.get('batch_test_set_size', 10000, type=int)
    print(train_set_size, learning_rate, train_steps, batch_test_set_size)
    mnist_number.run_with_variables(train_set_size, learning_rate, train_steps, batch_test_set_size)
    return jsonify(src_weights_map='static/weights.png')

@app.route('/mnist_fashion')
def route_mnist_fashion():
    return render_template('mnist_fashion.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
