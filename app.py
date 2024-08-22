from flask import Flask, render_template, request
from price_negotiator import PriceNegotiatorChatbot  # Import the chatbot class

app = Flask(__name__)

# Initialize the chatbot with some values
chatbot = PriceNegotiatorChatbot(initial_price=1000, min_price=700, max_price=1200, discount_rate=0.05)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        customer_offer = float(request.form['customer_offer'])
        response = chatbot.negotiate_price(customer_offer)
        return render_template('index.html', response=response)
    except ValueError:
        return render_template('index.html', response="Please enter a valid number for the offer.")

if __name__ == '__main__':
    app.run(debug=True)
