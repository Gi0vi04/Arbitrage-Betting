from api.odds import fetch_event_odds, fetch_events
from utils.constants import LEAGUES
from utils.helpers import save_results

def find_arbitrage_opportunities(odds):
    # Extract bookmakers odds
    bookmakers = odds["bookmakers"]
    # If we have less than two bookmakers we can skip
    if len(bookmakers) < 2:
        return None

    # Initialize best and second for home and away (price, index)
    best_home = (-1, None)
    second_home = (-1, None)
    best_away = (-1, None)
    second_away = (-1, None)

    for index, bookmaker in enumerate(bookmakers):
        home = bookmaker["markets"][0]["outcomes"][0]["price"]
        away = bookmaker["markets"][0]["outcomes"][1]["price"]

        # Check if we should update best_home or second_home
        if home > best_home[0]:
            second_home = best_home
            best_home = (home, index)
        elif home > second_home[0]:
            second_home = (home, index)

        # Check if we should update best_away or second_away
        if away > best_away[0]:
            second_away = best_away
            best_away = (away, index)
        elif away > second_away[0]:
            second_away = (away, index)
    
    # Initialize fields for the result
    home_bookmaker = ""
    away_bookmaker = ""
    home_price = 0
    away_price = 0

    # If bookmakers are different (different indexes), we can use best_home and best_away
    if best_home[1] != best_away[1]:
        home_price = best_home[0]
        away_price = best_away[0]

        home_bookmaker = bookmakers[best_home[1]]["title"]
        away_bookmaker = bookmakers[best_away[1]]["title"]
    else:
        # If bookmakers are the same, we need to pick the second best option
        option1 = best_home[0] + second_away[0]
        option2 = second_home[0] + best_away[0]

        if option1 > option2:
            home_price = best_home[0]
            away_price = second_away[0]

            home_bookmaker = bookmakers[best_home[1]]["title"]
            away_bookmaker = bookmakers[second_away[1]]["title"]
        else:
            home_price = second_home[0]
            away_price = best_away[0]

            home_bookmaker = bookmakers[second_home[1]]["title"]
            away_bookmaker = bookmakers[best_away[1]]["title"]

    return {
        "event": f"{odds["sport_title"]} | {odds["home_team"]} - {odds["away_team"]}",
        "home_price": home_price,
        "away_price": away_price,
        "home_bookmaker": home_bookmaker,
        "away_bookmaker": away_bookmaker,
        "perc": 2 - ((1/home_price) + (1/away_price))
    }

if __name__ == "__main__":
    results = []
    
    # Iterate through each league
    for league in LEAGUES:
        try:
            # Fetch events for the selected league
            events = fetch_events(league)

            # Iterate through each event
            for event in events:
                # Fetch h2h odds for the selected event
                odds = fetch_event_odds(league, event["id"], "h2h")

                # Compare odds and get the results
                result = find_arbitrage_opportunities(odds)
                if result:
                    results.append(result)

        except Exception as e:
            print(e)
            break
        
    save_results(sorted(results, key=lambda result: result["perc"], reverse=True))
    print("Calcolo terminato\n")