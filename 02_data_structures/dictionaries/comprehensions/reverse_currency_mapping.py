codes = {"USD": "US Dollar", "EUR": "Euro", "GBP": "British Pound", "JPY": "Japanese Yen"}

codes_reversed = {code: country for country, code in codes.items()}
print(codes_reversed)