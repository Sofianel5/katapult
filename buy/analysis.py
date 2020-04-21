from .models import MarketSegment
from users.models import DemographicProfile, Adspace
import requests 
import json

GOOGLE_KEY = "AIzaSyDWPqLxyV5wfu5STwy70HY0Dx9cL4KXV7I"
def distance(demographic1, demographic2):
    sse = 0
    sse += (demographic1.AgePercentUnder5 - demographic2.AgePercentUnder5)**2
    sse += (demographic1.AgePercent5To9 - demographic2.AgePercent5To9)**2
    sse += (demographic1.AgePercent10To14 - demographic2.AgePercent10To14)**2
    sse += (demographic1.AgePercent15To19 - demographic2.AgePercent15To19)**2
    sse += (demographic1.AgePercent20To24 - demographic2.AgePercent20To24)**2
    sse += (demographic1.AgePercent25To34 - demographic2.AgePercent25To34)**2
    sse += (demographic1.AgePercent35To44 - demographic2.AgePercent35To44)**2
    sse += (demographic1.AgePercent45To54 - demographic2.AgePercent45To54)**2
    sse += (demographic1.AgePercent55To59 - demographic2.AgePercent55To59)**2
    sse += (demographic1.AgePercent60To64 - demographic2.AgePercent60To64)**2
    sse += (demographic1.AgePercent65To74 - demographic2.AgePercent65To74)**2
    sse += (demographic1.AgePercent75To84 - demographic2.AgePercent75To84)**2
    sse += (demographic1.AgePercent85AndOver - demographic2.AgePercent85AndOver)**2
    sse += (demographic1.medianAge - demographic2.medianAge)**2
    sse += (demographic1.IncomePercentUnder10000 - demographic2.IncomePercentUnder10000)**2
    sse += (demographic1.IncomePercent10000To14999 - demographic2.IncomePercent10000To14999)**2
    sse += (demographic1.IncomePercent15000To24999 - demographic2.IncomePercent15000To24999)**2
    sse += (demographic1.IncomePercent25000To34999 - demographic2.IncomePercent25000To34999)**2
    sse += (demographic1.IncomePercent35000To49999 - demographic2.IncomePercent35000To49999)**2
    sse += (demographic1.IncomePercent50000To74999 - demographic2.IncomePercent50000To74999)**2
    sse += (demographic1.IncomePercent75000To99999 - demographic2.IncomePercent75000To99999)**2
    sse += (demographic1.IncomePercent100000To149999 - demographic2.IncomePercent100000To149999)**2
    sse += (demographic1.IncomePercent150000To199999 - demographic2.IncomePercent150000To199999)**2
    sse += (demographic1.IncomePercent200000OrMore - demographic2.IncomePercent200000OrMore)**2
    sse += (demographic1.PercentWhite - demographic2.PercentWhite)**2
    sse += (demographic1.PercentBlack - demographic2.PercentBlack)**2
    sse += (demographic1.PercentAmericanIndian - demographic2.PercentAmericanIndian)**2
    sse += (demographic1.PercentAsian - demographic2.PercentAsian)**2
    sse += (demographic1.PercentPacificIslander - demographic2.PercentPacificIslander)**2
    sse += (demographic1.PercentOtherRace - demographic2.PercentOtherRace)**2
    sse += (demographic1.PercentHispanicOrLatinoOfAnyRace - demographic2.PercentHispanicOrLatinoOfAnyRace)**2
    sse += (demographic1.PercentMale - demographic2.PercentMale)**2
    sse += (demographic1.BachDegree - demographic2.BachDegree)**2
    sse += (demographic1.GradDegree - demographic2.GradDegree)**2
    sse += (demographic1.AssocDegree - demographic2.AssocDegree)**2
    sse += (demographic1.SomeCollege - demographic2.SomeCollege)**2
    sse += (demographic1.HighSchool - demographic2.HighSchool)**2
    sse += (demographic1.BelowHighSchool - demographic2.BelowHighSchool)**2
    sse += (demographic1.WhiteCollar - demographic2.WhiteCollar)**2
    sse += (demographic1.Unemployed - demographic2.Unemployed)**2
    sse += (demographic1.BlueCollar - demographic2.BlueCollar)**2
    sse += ((demographic1.avgHouseholdSize - demographic2.avgHouseholdSize)*50)**2
    return sse**(0.5)
def sortMatchingSegments(segment, budget):
    available = list(Adspace.objects.all())
    available.sort(key=lambda x: distance(x.demographics, segment.demographics))
    available.reverse()
    i = 0
    pricesum = 0
    while (i < len(available)) and (pricesum < budget):
        pricesum += available[i].direct_price
        i += 1
    return available[:i]
def getCoordinates(matches):
    coordinates = []
    for match in matches:
        request = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={match.address}&key={GOOGLE_KEY}")
        response = dict(request.json())
        print(response)
        coordinates.append({"coordinates": response['results'][0]['geometry']['location'], "match": match.pk})
    return coordinates


