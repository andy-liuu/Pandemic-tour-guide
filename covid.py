import covidpy as cp

import countryinfo as ci

import pprint


#countries = cp.ListCountries()
#world = cp.WorldData()


'''
returns a dictionary with:

{'country': country['Country_Name'], 'cases': country["Active_Cases"], 'rating': rating}
'''

def getCovidStats(name):

    '''EXAMPLE RESULT IS DICTIONARY
{
    'Country_Name': 'BANGLADESH', 
    'Total_Cases': 777397, 
    'New_Cases': 0, 
    'Total_Deaths': 12045, 
    'New_Deaths': 0, 
    'Total_Recovered': 718249, 
    'New_Recovered': 0, 
    'Active_Cases': 47103, 
    'Serious_Cases': 1120, 
    'Total_Tests': 5677222
}
    '''


    country = cp.CountryData(name)
    population = ci.CountryInfo(name).population()

    percentage = country["Active_Cases"]/population

    #print(percentage)
    
    rating = 0

    if percentage < 0.02:
        rating = round(10 * (1-(percentage / 0.02)), 1)

    #print(rating)

    result = {'country': country['Country_Name'],
              'cases': country["Active_Cases"],
              'rating': rating}

    return result


#tester code
if __name__ == "__main__":
    
    pprint.pprint(getCovidStats("Canada"))

    pprint.pprint(countries)
