import requests
import xmltodict

def lookupAddy(addy, city, state, zip):
    response = requests.get(f"https://trial.serviceobjects.com/dgp/DemographicsPlus.asmx/GetDemographicsByAddress?Address={addy}&City={city}&State={state}&PostalCode={zip}&LicenseKey=WS53-OJB1-WNC1")
    res = dict(xmltodict.parse(response.content)['DemographicResult'])
    return res

