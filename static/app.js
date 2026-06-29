async function fetchMarket() {
  try {
    const response = await fetch("/market");
    const data = await response.json();

    document.getElementById("nifty").textContent = data.nifty ?? "N/A";
    document.getElementById("banknifty").textContent = data.bank_nifty ?? "N/A";
    document.getElementById("market").textContent = data.market_status ?? "N/A";

    const lastUpdate = document.getElementById("last_update");
    if (lastUpdate) lastUpdate.textContent = data.last_update ?? "";
  } catch (err) {
    console.error("Market fetch failed:", err);
  }
}

async function fetchSignal() {
  try {
    const response = await fetch("/signal");
    const data = await response.json();

    const el = document.getElementById("signal");
    if (el) el.textContent = `${data.signal ?? "—"} — ${data.reason ?? ""}`;
  } catch (err) {
    console.error("Signal fetch failed:", err);
  }
}

fetchMarket();
fetchSignal();
setInterval(fetchMarket, 5000);
setInterval(fetchSignal, 5000);
