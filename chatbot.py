print("Customer Service Chatbot")
print("Type 'exit' to stop the chatbot")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How can I help you?")
    
    elif user == "price":
        print("Bot: Our product price starts from ₹999.")
    
    elif user == "delivery":
        print("Bot: Delivery takes 3-5 business days.")
    
    elif user == "refund":
        print("Bot: Refund will be processed within 5 days.")
    
    elif user == "exit":
        print("Bot: Thank you! Have a nice day.")
        break
    
    else:
        print("Bot: Sorry, I didn't understand that.")