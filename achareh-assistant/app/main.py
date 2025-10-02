from conversation import ConversationManager
from services import detect_service, get_service_pricing, get_user_orders
from database import init_db, save_message

def run():
    init_db()
    cm = ConversationManager()

    user_id = "user_1"

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        save_message(user_id, "user", user_input)
        intent, slug = detect_service(user_input)

        if intent == "service":
            response = f"Service detected: {slug}"
            pricing = get_service_pricing(slug)
            response += f"\nPricing info: {pricing}"
        elif intent == "orders":
            response = get_user_orders(user_id)
        else:
            response = cm.respond(user_input)

        print("Assistant:", response)
        save_message(user_id, "assistant", response)

if __name__ == "__main__":
    run()
