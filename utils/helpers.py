from utils.dates import display_date, to_local

def print_result(result):
    timestamp = result["timestamp"]

    event = result["event"]
    commence_time = result["commence_time"]
    is_live = result["is_live"]
    perc = result["perc"]

    home_bookmaker = result["home_bookmaker"]
    away_bookmaker = result["away_bookmaker"]

    home_price = result["home_price"]
    away_price = result["away_price"]

    return f"""
TIMESTAMP: {display_date(to_local(timestamp))}

EVENT: {event}
TIME: {display_date(to_local(commence_time))} ({"LIVE" if is_live else "NOT STARTED"})

Profit: {perc:.4f}

── BET 1 ─────────────────────
Bookmaker        : {home_bookmaker}
Market           : 1 (Home)
Odds             : {home_price}
Stake percentage : {(1/home_price * 100):.2f}%

── BET 2 ─────────────────────
Bookmaker        : {away_bookmaker}
Market           : 2 (Away)
Odds             : {away_price}
Stake percentage : {(1/away_price * 100):.2f}%

"""

def save_results(results, threshold, mode):
    # If threshold is specified we filter the results
    if threshold:
        results = [result for result in results if result["perc"] >= threshold]
    
    # Normalize the file write mode
    mode = "w" if mode == "overwrite" else "a"

    with open("results.txt", mode, encoding="utf-8") as f:
        for result in results:
            f.write(print_result(result) + "\n")
