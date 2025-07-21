def respond_to_intent(intent):
    if intent == "order_tracking":
        return "Let me check your order status."
    elif intent == "password_reset":
        return "I'll help you reset your password."
    elif intent == "greeting":
        return "Hello, How can i assist you?"
    elif intent == "change_address":
        return "Sure, I can help you update your address."
    elif intent == "product_inquiry":
        return "Sure! What would u like to know about your order?"
    elif intent == "goodbye":
        return "Goodbye!, have a nice day!"
    elif intent == "complaint":
        return "Apologies for your bad experience, how can i assist"
    elif intent == "cancel_order":
        return "Your order cancellation request has been received."
    elif intent == "refund_request":
        return "I'll initiate the refund process for you."
    elif intent == "speak_to_agent":
        return "Connecting you to a customer service agent."
    elif intent == "return_product":
        return "I'll help you with the product return process."
    elif intent == "delivery_delayed":
        return "I'll help you with the delayed delivery, apologies for the inconvenience"
    elif intent == "thank_you":
        return "I'm delighted, is there anything else i can help you with?"
    else:
        return "Sorry, I didn’t understand that."
