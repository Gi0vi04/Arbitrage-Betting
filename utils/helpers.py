def print_result(result):
    event = result["event"]

    perc = result["perc"]
    
    home_bookmaker = result["home_bookmaker"]
    away_bookmaker = result["away_bookmaker"]
    
    home_price = result["home_price"]
    away_price = result["away_price"]

    output = []
    output.append("\n" + "=" * 60)
    output.append(event)
    output.append("-" * 60)
    output.append(f"Profit teorico: {perc:.4f}")

    output.append(f"\nBET 1:")
    output.append(f"Bookmaker: {home_bookmaker}")
    output.append(f"Risultato: 1")
    output.append(f"Quota: {home_price}")
    output.append(f"Percentuale puntata: {(1/home_price * 100):.2f}%")

    output.append(f"\nBET 2:")
    output.append(f"Bookmaker: {away_bookmaker}")
    output.append(f"Risultato: 2")
    output.append(f"Quota: {away_price}")
    output.append(f"Percentuale puntata: {(1/away_price * 100):.2f}%")

    output.append("=" * 60)

    final_output = "\n".join(output)
    
    return final_output

def save_results(results):
    with open("results.txt", "w") as f:
        for result in results:
            f.write(print_result(result) + "\n")
