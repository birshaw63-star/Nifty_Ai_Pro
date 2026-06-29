from api.market import get_market_data, get_nifty_closes


def get_signal() -> dict:
    """
    Generate a BUY / SELL / HOLD signal based on a 20-period simple moving average
    of Nifty 50 daily closes.  Replace or extend this function with additional
    indicators when needed — the response contract (signal, reason, ma20) must
    stay the same so the frontend and /signal endpoint need no changes.
    """
    try:
        # Current price
        data = get_market_data()
        raw = data.get("nifty", "0").replace(",", "")
        price = float(raw)

        # 20-period simple moving average of daily closes
        closes = get_nifty_closes(20)
        if len(closes) < 20:
            raise ValueError(f"Only {len(closes)} closes available, need 20.")

        ma20 = sum(closes) / len(closes)

        if price > ma20:
            signal = "BUY"
            reason = "Price is above the 20-period moving average."
        elif price < ma20:
            signal = "SELL"
            reason = "Price is below the 20-period moving average."
        else:
            signal = "HOLD"
            reason = "Price is at the 20-period moving average."

        return {
            "signal": signal,
            "reason": reason,
            "ma20": f"{ma20:,.2f}",
        }

    except Exception:
        return {
            "signal": "HOLD",
            "reason": "Signal unavailable — using default.",
            "ma20": "N/A",
        }
