from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample product data
products = [
    {"id": 1, "name": "Steel Rod", "priceUSD": 100, "country": "India"},
    {"id": 2, "name": "Copper Wire", "priceUSD": 200, "country": "China"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = {"id": len(products)+1, **data}
    products.append(new_product)
    return jsonify(new_product)

if __name__ == '__main__':
    app.run(debug=True)
