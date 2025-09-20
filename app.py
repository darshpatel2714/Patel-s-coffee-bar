from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Coffee and Order classes
class Coffee:
    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)

    def total(self):
        return sum(item.price for item in self.items)

    def clear(self):
        self.items.clear()

# Global menu and order
menu = [
    Coffee("Honey coffee", 250, "c1.png"),
    Coffee("Ginger coffee", 230, "c3.png"),
    Coffee("Madras coffee", 300, "c4.png"),
    Coffee("Filter coffee", 200, "c2.png"),
]

order = Order()

# Routes
@app.route('/')
def index():
    return render_template("index.html", menu=menu)

@app.route('/add/<int:item_id>')
def add_item(item_id):
    order.add_item(menu[item_id])
    return redirect(url_for('index'))

@app.route('/order')
def show_order():
    return render_template("order.html", order=order)

@app.route('/checkout')
def checkout():
    total = order.total()
    order.clear()
    return render_template("checkout.html", total=total)

if __name__ == '__main__':
    app.run(debug=True)
