def print_result(result):
    event = result["event"]
    perc = result["perc"]

    home_bookmaker = result["home_bookmaker"]
    away_bookmaker = result["away_bookmaker"]

    home_price = result["home_price"]
    away_price = result["away_price"]

    return f"""
EVENT: {event}

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

def save_results(results):
    with open("results.txt", "w", encoding="utf-8") as f:
        for result in results:
            f.write(print_result(result) + "\n")
