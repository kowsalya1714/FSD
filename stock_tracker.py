# ============================================================
#   STOCK PORTFOLIO TRACKER
#   Key Concepts: dictionary, input/output, basic arithmetic,
#                 file handling (optional)
# ============================================================

import csv
import os

# ── HARDCODED DICTIONARY OF STOCK PRICES ────────────────────
stock_prices = {
    "AAPL":  180,
    "TSLA":  250,
    "GOOGL": 140,
    "AMZN":  185,
    "MSFT":  420,
    "NVDA":  900,
    "META":  500,
    "NFLX":  630,
    "AMD":   170,
    "BABA":   80
}

# ── DISPLAY AVAILABLE STOCKS ─────────────────────────────────
def show_available_stocks():
    print("\n" + "=" * 40)
    print("   AVAILABLE STOCKS & PRICES")
    print("=" * 40)
    for ticker, price in stock_prices.items():
        print(f"  {ticker:<8} :  ${price}")
    print("=" * 40)

# ── GET USER INPUT ───────────────────────────────────────────
def get_portfolio():
    portfolio = {}  # { "AAPL": quantity, "TSLA": quantity, ... }

    print("\nEnter stock name and quantity (type 'done' to finish):\n")

    while True:
        stock = input("  Stock symbol (or 'done'): ").strip().upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print(f"  ⚠  '{stock}' not found. Available: {', '.join(stock_prices.keys())}\n")
            continue

        try:
            qty = int(input(f"  Quantity for {stock}: ").strip())
            if qty <= 0:
                print("  ⚠  Quantity must be a positive number.\n")
                continue
        except ValueError:
            print("  ⚠  Please enter a valid number.\n")
            continue

        # If same stock entered twice, add quantities
        if stock in portfolio:
            portfolio[stock] += qty
            print(f"  ✓  Updated {stock}: total {portfolio[stock]} shares\n")
        else:
            portfolio[stock] = qty
            print(f"  ✓  Added {qty} shares of {stock}\n")

    return portfolio

# ── CALCULATE & DISPLAY RESULTS ──────────────────────────────
def display_results(portfolio):
    print("\n" + "=" * 50)
    print("         YOUR PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"  {'STOCK':<8}  {'PRICE':>8}  {'QTY':>6}  {'TOTAL':>12}")
    print("-" * 50)

    grand_total = 0

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        total = price * qty          # Basic Arithmetic
        grand_total += total
        print(f"  {stock:<8}  ${price:>7}  {qty:>6}  ${total:>11,.2f}")

    print("=" * 50)
    print(f"  {'TOTAL INVESTMENT':>35}  ${grand_total:>11,.2f}")
    print("=" * 50)

    return grand_total

# ── SAVE TO TXT FILE ─────────────────────────────────────────
def save_to_txt(portfolio, grand_total):
    filename = "portfolio_report.txt"
    with open(filename, "w") as f:
        f.write("=" * 50 + "\n")
        f.write("      STOCK PORTFOLIO REPORT\n")
        f.write("=" * 50 + "\n")
        f.write(f"  {'STOCK':<8}  {'PRICE':>8}  {'QTY':>6}  {'TOTAL':>12}\n")
        f.write("-" * 50 + "\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            total = price * qty
            f.write(f"  {stock:<8}  ${price:>7}  {qty:>6}  ${total:>11,.2f}\n")
        f.write("=" * 50 + "\n")
        f.write(f"  TOTAL INVESTMENT  :  ${grand_total:,.2f}\n")
        f.write("=" * 50 + "\n")
    print(f"\n  ✓  Report saved to '{filename}'")

# ── SAVE TO CSV FILE ─────────────────────────────────────────
def save_to_csv(portfolio, grand_total):
    filename = "portfolio_report.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Price Per Share", "Quantity", "Total Value"])
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            total = price * qty
            writer.writerow([stock, price, qty, round(total, 2)])
        writer.writerow([])
        writer.writerow(["GRAND TOTAL", "", "", round(grand_total, 2)])
    print(f"  ✓  Report saved to '{filename}'")

# ── MAIN PROGRAM ─────────────────────────────────────────────
def main():
    print("\n" + "*" * 40)
    print("   STOCK PORTFOLIO TRACKER")
    print("*" * 40)

    # Step 1: Show available stocks
    show_available_stocks()

    # Step 2: Get user input
    portfolio = get_portfolio()

    if not portfolio:
        print("\n  No stocks entered. Exiting.")
        return

    # Step 3: Display results
    grand_total = display_results(portfolio)

    # Step 4: Optional file saving
    print("\n  Save your portfolio report?")
    print("  1. Save as TXT")
    print("  2. Save as CSV")
    print("  3. Save both")
    print("  4. Skip")

    choice = input("\n  Your choice (1/2/3/4): ").strip()

    if choice == "1":
        save_to_txt(portfolio, grand_total)
    elif choice == "2":
        save_to_csv(portfolio, grand_total)
    elif choice == "3":
        save_to_txt(portfolio, grand_total)
        save_to_csv(portfolio, grand_total)
    else:
        print("\n  Skipping file save.")

    print("\n  Thank you for using Stock Portfolio Tracker!\n")

# ── RUN ───────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
