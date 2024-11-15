exchange_rates = {
    'usd_to_eur': 0.85,  # 1 USD = 0.85 EUR
    'usd_to_gbp': 0.75,  # 1 USD = 0.75 GBP
    'usd_to_inr': 74.0,  # 1 USD = 74.0 INR
    'usd_to_jpy': 110.0, # 1 USD = 110.0 JPY
}

def convert_currency(amount, conversion_rate):
    return amount * conversion_rate

while True:
    # Ask the user to enter the amount in USD
    try:
        amount_in_usd = float(input("Enter amount in USD (or type '0' to quit): "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue
# Exit the loop if the user wants to quit
    if amount_in_usd == 0:
        print("Thank you for using the Currency Converter! Goodbye.")
        break
    # Ask the user for the target currency
    print("Choose a target currency: EUR, GBP, INR, JPY")
    target_currency = input("Enter target currency: ").lower()
    # Check if the chosen currency is valid
    if target_currency == 'eur':
        converted_amount = convert_currency(amount_in_usd, exchange_rates['usd_to_eur'])
        print(f"{amount_in_usd} USD is equal to {converted_amount:.2f} EUR")
    elif target_currency == 'gbp':
        converted_amount = convert_currency(amount_in_usd, exchange_rates['usd_to_gbp'])
        print(f"{amount_in_usd} USD is equal to {converted_amount:.2f} GBP")
    elif target_currency == 'inr':
        converted_amount = convert_currency(amount_in_usd, exchange_rates['usd_to_inr'])
        print(f"{amount_in_usd} USD is equal to {converted_amount:.2f} INR")
    elif target_currency == 'jpy':
        converted_amount = convert_currency(amount_in_usd, exchange_rates['usd_to_jpy'])
        print(f"{amount_in_usd} USD is equal to {converted_amount:.2f} JPY")
    else:
        print("Invalid currency. Please choose from EUR, GBP, INR, JPY.")

