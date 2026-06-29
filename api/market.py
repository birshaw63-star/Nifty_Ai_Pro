import requests

_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

_BASE = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1m&range=1d"


def _fetch_meta(symbol: str) -> dict:
    url = _BASE.format(symbol=symbol)
    r = requests.get(url, headers=_HEADERS, timeout=10)
    r.raise_for_status()
    return r.json()["chart"]["result"][0]["meta"]


def get_market_data() -> dict:
    try:
        nifty_meta = _fetch_meta("%5ENSEI")
        bank_meta = _fetch_meta("%5ENSEBANK")

        nifty_price = nifty_meta.get("regularMarketPrice", 0)
        bank_price = bank_meta.get("regularMarketPrice", 0)
        state = nifty_meta.get("marketState", "UNKNOWN")

        market_status = "LIVE" if state == "REGULAR" else f"CLOSED ({state})"

        return {
            "nifty": f"{nifty_price:,.2f}",
            "bank_nifty": f"{bank_price:,.2f}",
            "market_status": market_status,
        }

    except Exception:
        return {
            "nifty": "Error",
            "bank_nifty": "Error",
            "market_status": "Offline",
        }
