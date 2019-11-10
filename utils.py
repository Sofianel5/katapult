from users.models import DemographicProfile as dp 
from demographics import lookupAddy

def createDemographicProfile(address, city, state, zip):
    raw_data = lookupAddy(address, city, state, zip)
    age_data = {}
    age_data["PercentUnder5"] = raw_data['AgeDistribution']['PercentUnder5']
    age_data["AgePercent5To9"] = raw_data['AgeDistribution']['Percent5To9']
    age_data["AgePercent10To14"] = raw_data['AgeDistribution']['Percent10To14']
    age_data["AgePercent15To19"] = raw_data['AgeDistribution']['Percent15To19']
    age_data["AgePercent20To24"] = raw_data['AgeDistribution']['Percent20To24']
    age_data["AgePercent25To34"] = raw_data['AgeDistribution']['Percent25To34']
    age_data["AgePercent35To44"] = raw_data['AgeDistribution']['Percent35To44']
    age_data["AgePercent45To54"] = raw_data['AgeDistribution']['Percent45To54']
    age_data["AgePercent55To59"] = raw_data['AgeDistribution']['Percent55To59']
    age_data["AgePercent60To64"] = raw_data['AgeDistribution']['Percent60To64']
    age_data["AgePercent65To74"] = raw_data['AgeDistribution']['Percent65To74']
    age_data["AgePercent75To84"] = raw_data['AgeDistribution']['Percent75To84']
    age_data["AgePercent85AndOver"] = raw_data['AgeDistribution']['Percent85AndOver']
    age_data['medianAge'] = raw_data['AgeDistribution']['MedianAge']
    income_keys = ["PercentUnder10000", "Percent10000To14999", "Percent15000To24999", "Percent25000To34999", "Percent35000To49999", "Percent50000To74999", "Percent75000To99999", "Percent100000To149999", "Percent150000To199999", "Percent200000OrMore", "MedianHouseholdIncome"]
    income_data = {}
    for key in income_keys:
        income_data[key] = raw_data["IncomeDistribution"][key]
    ethnic_keys = ['PercentWhite', 'PercentBlack', 'PercentAmericanIndian', 'PercentAsian', 'PercentAsian', 'PercentPacificIslander', 'PercentOtherRace']
    ethnic_data = {}
    for key in ethnic_keys:
        ethnic_data[key] = raw_data["RaceDistribution"][key]
    ethnic_data["PercentHispanicOrLatinoOfAnyRace"] = raw_data["EthnicDistribution"]["PercentHispanicOrLatinoOfAnyRace"]
    ethnic_data["PercentNotHispanicOrLatino"] = raw_data["EthnicDistribution"]["PercentNotHispanicOrLatino"]
    population_density = raw_data["OtherInformation"]["PeoplePerSquareKilometer"]
    gender_distribution = {}
    gender_distribution["PercentFemale"] = raw_data["OtherInformation"]["PercentFemale"]
    gender_distribution["PercentMale"] = raw_data["OtherInformation"]["PercentMale"]
    education_distribution = {}
    education_keys = ['AreaGradDegree', 'AreaBachDegree', 'AreaAssocDegree', 'AreaSomeCollege', 'AreaHighSchoolGrad', 'AreaBelowHighSchoolGrad']
    for key in education_keys:
        education_distribution[key] = raw_data['CensusElements'][key]
    employement_keys = ['AreaWhiteCollar', 'AreaBlueCollar', 'AreaUnemploymentRate']
    employment_data = {}
    for key in employement_keys:
        employment_data[key] = raw_data['CensusElements'][key]
    household_size = raw_data['CensusElements']["AreaAvgHouseholdSize"]
    demographicProfile = dp()
    demographicProfile.AgePercentUnder5 = age_data["PercentUnder5"]
    demographicProfile.AgePercent5To9 = age_data["AgePercent5To9"]
    demographicProfile.AgePercent10To14 = age_data["AgePercent10To14"]
    demographicProfile.AgePercent15To19 = age_data["AgePercent15To19"]
    demographicProfile.AgePercent20To24 = age_data["AgePercent20To24"]
    demographicProfile.AgePercent25To34 = age_data["AgePercent25To34"]
    demographicProfile.AgePercent35To44 = age_data["AgePercent35To44"]
    demographicProfile.AgePercent45To54 = age_data["AgePercent45To54"]
    demographicProfile.AgePercent55To59 = age_data["AgePercent55To59"]
    demographicProfile.AgePercent60To64 = age_data["AgePercent60To64"]
    demographicProfile.AgePercent65To74 = age_data["AgePercent65To74"]
    demographicProfile.AgePercent75To84 = age_data["AgePercent75To84"]
    demographicProfile.AgePercent85AndOver = age_data["AgePercent85AndOver"]
    demographicProfile.medianAge = age_data['medianAge']
    demographicProfile.IncomePercentUnder10000 = income_data['PercentUnder10000']
    demographicProfile.IncomePercent10000To14999 = income_data['Percent10000To14999']
    demographicProfile.IncomePercent15000To24999 = income_data['Percent15000To24999']
    demographicProfile.IncomePercent25000To34999 = income_data['Percent25000To34999']
    demographicProfile.IncomePercent35000To49999 = income_data['Percent35000To49999']
    demographicProfile.IncomePercent50000To74999 = income_data['Percent50000To74999']
    demographicProfile.IncomePercent75000To99999 = income_data['Percent75000To99999']
    demographicProfile.IncomePercent100000To149999 = income_data['Percent100000To149999']
    demographicProfile.IncomePercent150000To199999 = income_data['Percent150000To199999']
    demographicProfile.IncomePercent200000OrMore = income_data['Percent200000OrMore']
    demographicProfile.medianIncome = income_data["MedianHouseholdIncome"]
    demographicProfile.PercentWhite = ethnic_data["PercentWhite"]
    demographicProfile.PercentBlack = ethnic_data["PercentBlack"]
    demographicProfile.PercentAmericanIndian = ethnic_data["PercentAmericanIndian"]
    demographicProfile.PercentAsian = ethnic_data["PercentAsian"]
    demographicProfile.PercentPacificIslander = ethnic_data["PercentPacificIslander"]
    demographicProfile.PercentOtherRace = ethnic_data["PercentOtherRace"]
    demographicProfile.PercentHispanicOrLatinoOfAnyRace = ethnic_data["PercentHispanicOrLatinoOfAnyRace"]
    demographicProfile.PercentNotHispanicOrLatino = ethnic_data["PercentNotHispanicOrLatino"]
    demographicProfile.populationDensity = population_density
    demographicProfile.PercentMale = gender_distribution["PercentMale"]
    demographicProfile.PercentFemale = gender_distribution["PercentFemale"]
    demographicProfile.BachDegree = education_distribution["AreaBachDegree"]
    demographicProfile.GradDegree = education_distribution["AreaGradDegree"]
    demographicProfile.AssocDegree = education_distribution["AreaAssocDegree"]
    demographicProfile.SomeCollege = education_distribution["AreaSomeCollege"]
    demographicProfile.HighSchool = education_distribution["AreaHighSchoolGrad"]
    demographicProfile.BelowHighSchool = education_distribution["AreaBelowHighSchoolGrad"]
    demographicProfile.WhiteCollar = employment_data['AreaWhiteCollar']
    demographicProfile.BlueCollar = employment_data['AreaBlueCollar']
    demographicProfile.Unemployed = employment_data['AreaUnemploymentRate']
    demographicProfile.avgHouseholdSize = household_size
    demographicProfile.save()
    return demographicProfile