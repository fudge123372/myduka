from flask import Flask, render_template

# ✅ create app FIRST
app = Flask(__name__)

# ✅ THEN routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

# ✅ THEN run app
if __name__ == "__main__":
    app.run(debug=True)