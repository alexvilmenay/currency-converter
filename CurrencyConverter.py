import requests

# Currecncies URL
url= f"https://data.fixer.io/api/latest?access_key=7be6ab38aca7dd8a558f81ffc7aeaaa8"
response = requests.get(url)
data = response.json()
rates = data["rates"]

def getDict(country): # enter string country 
     url5 = "https://restcountries.com/v3.1/name/" + country # gets url link for country inputed 
     dict = requests.get(url5).json()[0] # saves county url info to a variable
     return dict # returns dict of imputed country

def EuroToUsd(x):
  euro = x
  usd = euro * rates["USD"]
  return usd

def getCode(country):
   nation = getDict(country)
   currencies = nation["currencies"]
   code = list(currencies.keys())[0]
   return code

def getCurrency(amount,country):
   nationCode = getCode(country)
   usCon = amount/ rates["USD"]
   currency = usCon * rates[nationCode]
   return round(currency,2)


  

def main():
 print(EuroToUsd(15))
 print(getCode("japan"))
 print(getCurrency(15,"united kingdom"))

while True:
 choice = input("Press 1 to Begin Conversion 2 to quit: ")
 if choice == "1":
    amount = int(input("Enter amount: "))
    country = input("Enter Country to Convert: ")
    if country == "england" or country == "uk"  or  country == "scotland"   or country == "wales":
       country = "united kingdom"
    code = getCode(country)
    conversion = getCurrency(amount,country)
    print(amount, "USD is", conversion, code, "in", country  )
 elif choice == "2":
    break 
 else:
    print("Invalid Input. Try Again") 


 

if __name__ == "__main__":
  main()
