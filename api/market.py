import yfinance as yf


def get_market_data():
    try:
        nifty = yf.Ticker("^NSEI")
        bank = yf.Ticker("^NSEBANK")

        nifty_price = nifty.fast_info.get("lastPrice", "N/A")
        bank_price = bank.fast_info.get("lastPrice", "N/A")

        return {
            "nifty": nifty_price,
            "bank_nifty": bank_price,
            "market_status": "LIVE"
        }

    except Exception:
        return {
            "nifty": "Error",
            "bank_nifty": "Error",
            "market_status": "Offline"
        }