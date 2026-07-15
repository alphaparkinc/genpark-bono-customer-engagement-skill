class BonoCustomerEngagementClient:
    def evaluate_behavior(self, user_idle_seconds: int, cart_abandoned: bool) -> dict:
        trigger = user_idle_seconds > 45 or cart_abandoned
        coupon = "SAVE10NOW" if trigger and cart_abandoned else "WELCOME5" if trigger else ""
        return {"trigger_modal": trigger, "modal_coupon_code": coupon}