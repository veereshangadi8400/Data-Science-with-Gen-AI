# #constants
import csv

countries = []
allUnivs = {}

def readFiles(UniFileName, capitalsFileName):
    try:
        with open(capitalsFileName) as c:
            capitals_reader = csv.reader(c)
            next(capitals_reader)
            for row in capitals_reader:
                # country, capital, latitude, longitude, countryCode, continent = row
                countries.append(row)
        with open(UniFileName) as u:
            universities_reader = csv.reader(u)
            next(universities_reader)
            for row in universities_reader:
                allUnivs[row[0]] = row[1:]
    except IOError :
        return False 
    return allUnivs

allUniv =  readFiles(r'C:\Users\Veeresh\OneDrive\Documents\flm_documents\weekly_test\week4_Test\universities.csv',
          r'C:\Users\Veeresh\OneDrive\Documents\flm_documents\weekly_test\week4_Test\capitals.csv')
# print(allUniv)

def findCountryByName(countryName, countries):
    for country in countries:
        if country[0].lower() == countryName.lower():
            return (country[0], country[1], country[5])
    return False

countryByName = findCountryByName('France', countries)
# print(countryByName)

def getAllCodes(allUnivs):
    codes =set()
    for key in allUnivs:
        codes.add(key)
    return codes
    #or
    #dict_keys([])
    
# print(getAllCodes(allUnivs))


def getDistinctCountries(allUnivs):
    distinctCountries = set()
    for code in allUnivs:
        distinctCountries.add(allUnivs[code][2])
    return distinctCountries
 
# print(getDistinctCountries(allUnivs))

def getDistinctContinents(allUnivs):
    distinctContinents = set()
    for code in allUnivs:
        countryInUniv = allUnivs[code][2]
        for country in countries:
            if country[0] == countryInUniv:
                distinctContinents.add(country[5])
    return distinctContinents

# print(getDistinctContinents(allUnivs))

def getTopIntRank(countryName, allUnivs):
    countryName = countryName.upper()
    bestRank, bestUniv = None, None
    for code in allUnivs:
        if allUnivs[code][2].upper() == countryName:
            if bestRank is None:
                bestRank = int(allUnivs[code][0])
                bestUniv = allUnivs[code][1]
            else:
                if bestRank > int(allUnivs[code][0]):
                    bestRank = int(allUnivs[code][0])
                    bestUniv  = allUnivs[code][1]
    if bestRank is None:
        return f'No university in {countryName}'
    return(str(bestRank), bestUniv)

# print(getTopIntRank('Usa', allUnivs))

def getTopNatRank(countryName, allUnivs):
    countryName = countryName.upper()
    bestRank, bestUniv = None, None
    for code in allUnivs:
        if allUnivs[code][2].upper() == countryName:
            if bestRank is None:
                bestRank = allUnivs[code][3]
                bestUniv = allUnivs[code][1]
            else:
                if int(bestRank) > int(allUnivs[code][3]):
                    bestRank = allUnivs[code][3]
                    bestUniv = allUnivs[code][1]
    if bestRank is None:
        return f'No University in {countryName}'
    return (bestRank, bestUniv)

# print(getTopNatRank('Japan', allUnivs))

def getAvgScore(countryName, allUnivs):
    countryName = countryName.upper()
    scores = []
    for code in allUnivs:
        if allUnivs[code][2].upper() == countryName:
            scores.append(float(allUnivs[code][6]))
    if not scores:
        return f'{countryName} not found'
    return round(sum(scores)/len(scores),2) 

print(getAvgScore('denmark', allUnivs))

# def getRelativeScoreContinent(countryName, allUnivs):
#     countryName = countryName.upper()
#     # your code is here
#     return round(100*avg/max,2)


# def getUnivWithCapital(countryName, allUnivs):
#     univsWithCapital=set()
#     countryName = countryName.upper()
#     # your code is here
#     return univsWithCapital


# def studyInOnePlace(countryName, degrees, budget,allUnivs):
#     countryName = countryName.upper()
#     codes=set()
#     degrees = set( [d.upper() for d in degrees])
#     # your code is here
#     # return codes
#     # or
#     # return [codes]


# def studyInTwoPlaces(firstCode, firstDegree,secondCode , secondDegree, budget,allUnivs):
#     firstDegree = firstDegree.upper()
#     secondDegree = secondDegree.upper()
#     firstCode = firstCode.upper()
#     secondCode = secondCode.upper()
#     # your code is here
    
#     #     return True
#     # or
#     #     return False
#     # or
#     #     raise ValueError("Something went wrong!")