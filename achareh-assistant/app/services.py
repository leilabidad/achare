import requests

BASE_URL = "https://achareh.co/api/v1"

def detect_service(text: str):
    services = {
        "نظافت": "home-cleaning",
        "کولر": "cooler-repair",
        "تعمیر": "general-repair"
    }
    for k, v in services.items():
        if k in text:
            return "service", v
    if "سفارش" in text or "پیگیری" in text:
        return "orders", None
    return "unknown", None

def get_service_pricing(slug: str):
    try:
        url = f"{BASE_URL}/services/{slug}/pricing"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            if "pricing_rules" in data:
                return data["pricing_rules"]
            return "No pricing rules available"
        return f"Error {r.status_code}"
    except Exception as e:
        return str(e)

def get_user_orders(user_id: str):
    return f"Orders for {user_id}: [Sample order: Home Cleaning, status: done]"
