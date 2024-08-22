from flask import Flask, render_template, request
from price_negotiator import PriceNegotiatorChatbot

app = Flask(__name__)

# Initialize the chatbot
chatbot = PriceNegotiatorChatbot(initial_price=100, min_price=50, max_price=200, discount_rate=0.1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    customer_offer = float(request.form['customer_offer'])
    response = chatbot.negotiate_price(customer_offer)
    return response

if __name__ == '__main__':
    app.run(debug=True)