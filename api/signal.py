from api.market import get_market_data


def get_signal() -> dict:
    """
    Placeholder signal logic.
    Compares the current Nifty price against a fixed short-term reference level.
    Replace this function body with real indicator logic when ready.
    """
    try:
        data = get_market_data()
        raw = data.get("nifty", "0").replace(",", "")
        price = float(raw)

        # Placeholder threshold — treat 23,500 as the short-term moving average proxy
        reference = 23_500.0

        if price > reference:
            return {
                "signal": "BUY",
                "reason": "Price is above the short-term moving average.",
            }
        elif price < reference:
            return {
                "signal": "SELL",
                "reason": "Price is below the short-term moving average.",
            }
        else:
            return {
                "signal": "HOLD",
                "reason": "Price is at the short-term moving average.",
            }

    except Exception:
        return {
            "signal": "HOLD",
            "reason": "Signal unavailable — using default.",
        }
