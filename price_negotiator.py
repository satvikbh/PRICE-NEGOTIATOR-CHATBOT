import re
import random

class PriceNegotiatorChatbot:
    def __init__(self, initial_price, min_price, max_price, discount_rate):
        self.initial_price = initial_price
        self.min_price = min_price
        self.max_price = max_price
        self.discount_rate = discount_rate
        self.current_price = initial_price

    def negotiate_price(self, customer_offer):
        # Check if the customer's offer is within the acceptable range
        if self.min_price <= customer_offer <= self.max_price:
            # Accept the offer
            self.current_price = customer_offer
            return f"Okay, I can offer the product at {self.current_price}."
        else:
            # Counter the offer
            new_price = self.current_price * (1 - self.discount_rate)
            if new_price < self.min_price:
                new_price = self.min_price
            self.current_price = new_price
            return f"I'm sorry, but I can only offer the product at {self.current_price}."

def extract_offer(message):
    """ Extract the offer from the user's message using regex """
    offer = re.findall(r'\d+', message)
    if offer:
        return int(offer[0])
    return None

def start_chatbot():
    # Initialize the chatbot with some values
    initial_price = 1000
    min_price = 700
    max_price = 1200
    discount_rate = 0.05

    chatbot = PriceNegotiatorChatbot(initial_price, min_price, max_price, discount_rate)

    print("Welcome to the Price Negotiator Chatbot!")
    print(f"The starting price is {chatbot.current_price}. What's your offer?")

    while True:
        customer_input = input("You: ")
        
        # Extract the offer from customer input
        offer = extract_offer(customer_input)
        if offer is not None:
            # Get the chatbot's response to the offer
            response = chatbot.negotiate_price(offer)
            print(f"Chatbot: {response}")
            
            # Exit condition if price is accepted
            if chatbot.current_price == offer:
                print("Chatbot: Deal accepted! Thank you for your purchase.")
                break
        else:
            print("Chatbot: Please make a valid offer (e.g., 'I offer 800').")

if __name__ == "__main__":
    start_chatbot()
