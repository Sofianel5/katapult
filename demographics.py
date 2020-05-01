import requests
import xmltodict

def lookupAddy(addy, city, state, zip):
    response = requests.get(f"https://trial.serviceobjects.com/dgp/DemographicsPlus.asmx/GetDemographicsByAddress?Address={addy}&City={city}&State={state}&PostalCode={zip}&LicenseKey=WS53-JRL1-NHG3")
    res = dict(xmltodict.parse(response.content)['DemographicResult'])
    print(res)
    return res

