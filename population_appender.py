# This script uses the google maps API to extract population data from all of the relevant manhattan boroughs and adds
# that data in a new column in an excel sheet next to an address that is located in that particular borough.

# Import necessary libraries
import pandas as pd
import math
from math import radians, cos, sin, asin, sqrt

# Google Maps API Key
gmaps = googlemaps.Client(key='[your API key]')

# Set path to where your dataset is stored
# and use the updated unique_addresses_with_google_lat_longs file that was sent with this email)
unique_addresses = pd.read_csv(
    [YOUR PATH], encoding="ISO-8859-1")

############################## Borough Extraction #################################################

# This loops over the unique_addresses lat/longs and parses out the boroughs and appends them to
# unique_addresses. THIS CODE TAKES OVER 25 MINS TO RUN!
boroughs = []
for l in range(739, len(unique_addresses['Unique Address'])):
    try:
        x = pd.DataFrame(gmaps.reverse_geocode((unique_addresses['Latitude'][l],
                                                unique_addresses['Longitude'][l]), result_type='neighborhood'))[
            'formatted_address'][0]
    except:
        x = 'No borough found'
    boroughs.append(x)
unique_addresses['Boroughs'] = pd.DataFrame(boroughs)[0]
print(unique_addresses.head())

####################################################################################################
######################## Importing Borough Population Data into the Dataframe ######################
####################################################################################################

# REPLACE MY PATH WITH YOUR PATH FOR THE FILES IN QUESTION
unique_addresses_complete = pd.read_csv(
    [YOUR PATH])

popData = pd.DataFrame(pd.read_csv(
    [YOUR PATH]))

unique_addresses_complete['Population'] = 0

# For loop that iterates over all of the the data in unique_addresses_complete and appends the population data from
# popData.csv

for i in range(0, unique_addresses_complete['Boroughs'].count()):
    if "Manhattanville" in unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][4])
    if "Morningside Heights" in unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][5])
    if "Upper West Side" in unique_addresses_complete['Boroughs'][i] or "Bloomingdale" in \
            unique_addresses_complete['Boroughs'][i] or "Manhattan Valley" in unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][7])
    if "Chelsea" in unique_addresses_complete['Boroughs'][i] or "Flatiron District" in \
            unique_addresses_complete['Boroughs'][i] or "Union Square" in unique_addresses_complete['Boroughs'][
        i] or "Hudson Yards" in unique_addresses_complete['Boroughs'][i] or "NoMad" in \
            unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][5])
    if "Lincoln Square" in unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][9])
    if "Clinton" in unique_addresses_complete['Boroughs'][i] or "Hell's Kitchen" in \
            unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][10])
    if "Midtown South" in unique_addresses_complete['Boroughs'][i] or "Midtown" in \
            unique_addresses_complete['Boroughs'][i] or "Koreatown" in unique_addresses_complete['Boroughs'][
        i] or "Midtown Manhattan" in unique_addresses_complete['Boroughs'][i] or "Garment District" in \
            unique_addresses_complete['Boroughs'][i] or "Theater District" in unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][11])
    if "Midtown East" in unique_addresses_complete['Boroughs'][i] or "Turtle Bay" in \
            unique_addresses_complete['Boroughs'][i] or "Sutton Place" in unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][12])
    if "Murray Hill" in unique_addresses_complete['Boroughs'][i] or "Kips Bay" in unique_addresses_complete['Boroughs'][
        i] or "Rose Hill" in unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][13])
    if "Gramercy" in unique_addresses_complete['Boroughs'][i] or "Herald Square" in \
            unique_addresses_complete['Boroughs'][i] or "Gramercy Park" in unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][14])
    if "East Village" in unique_addresses_complete['Boroughs'][i] or "Bowery" in unique_addresses_complete['Boroughs'][
        i] or "Ukrainian Village" in unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][15])
    if "West Village" in unique_addresses_complete['Boroughs'][i] or "Meatpacking District" in \
            unique_addresses_complete['Boroughs'][i] or "NoHo" in unique_addresses_complete['Boroughs'][
        i] or "Greenwich Village" in unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][16])
    if "SoHo" in unique_addresses_complete['Boroughs'][i] or "Tribeca" in unique_addresses_complete['Boroughs'][
        i] or "Little Italy" in unique_addresses_complete['Boroughs'][i] or "Washington Square Village" in \
            unique_addresses_complete['Boroughs'][i] or "Hudson Square" in unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][17])
    if "Battery Park City" in unique_addresses_complete['Boroughs'][i] or "Financial District" in \
            unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][18])
    if "Lower East Side" in unique_addresses_complete['Boroughs'][i] or "Alphabet City" in \
            unique_addresses_complete['Boroughs'][i] or "Two Bridges" in unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][20])
    if "Lenox Hill" in unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][21])
    if "Yorkville" in unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][22])
    if "Upper East Side" in unique_addresses_complete['Boroughs'][i] or "Carnegie Hill" in \
            unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][22])
    if "Stuyvesant Town-Peter Cooper Village" in unique_addresses_complete['Boroughs'][i] or "Peter Cooper Village" in \
            unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][28])
    if "Chinatown" in unique_addresses_complete['Boroughs'][i] or "Civic Center" in \
            unique_addresses_complete['Boroughs'][i]:
        unique_addresses_complete['Population'][i] = int(popData['MealTime Avg'][19])

    # Parses out the csv with the updated population data.
unique_addresses_complete.to_csv('unique_addresses_with_population_incomplete.csv')


####################################################################################################
############################### Locating addresses within a distance ###############################
####################################################################################################
def within_distance(lat1, lon1, lat2, lon2, distance_min):
    '''This function checks if a given address (defined by lat1, lon1) is within blocks city 
    blocks of another address (given by lat2, lon2).
    int, int, int, int, int -> boolean
    '''

    # Haversine function to compute distance between the two points
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 3956  # Radius of earth in kilometers. Use 3956 for miles
    distance = c * r

    # Compare haversine distance to min_distance
    return distance < distance_min


def locate_addresses(address, blocks, path):
    '''This function takes in one of the unique addresses(must be spelled exactly the way they are
     in the file) and outputs a dataframe of the cooresponding addresses and their lat/longs that 
     are within blocks radius of that particular address. path contains the file that has the 
     unique addresses, latitude, longitude and borough. string, int, string -> pandas DataFrame 
     object
    '''
    old_addresses = pd.read_csv(path)
    # First, determine the combination of integer values that will form the a and b side of the 
    # right triangle. a and b 
    # must add up to blocks.
    # Calculate a, b, and c for triangles that can be made with {blocks} city blocks
    a = list(range(0, int(blocks / 2) + 1, 1))
    b = list(range(blocks, int(blocks / 2) - 1, -1))
    c = []
    for i in range(0, len(a)):
        c.append(sqrt(a[i] ** 2 + b[i] ** 2))
    c[:] = [x / 20 for x in c]
    c_in_miles = c
    # These are the haversine radii corresponding to all of the combinations of city blocks one
    # would have to walk to be
    # able to deliver at the boundaries of the 20 block radius. 
    print(c_in_miles)

    # For now, take the minimum of this distance to use in comparison.
    distance_min = min(c_in_miles)

    # Pull Latitude and Longitude of the address in question.
    for i in range(0, old_addresses['Latitude'].count()):
        if old_addresses['Unique Address'][i] == address:
            lat = old_addresses['Latitude'][i]
            long = old_addresses['Longitude'][i]
            break
        else:
            continue

    # Implement haversine distance function comparing the distance from Lat/Long of the 
    # given address to the Lat/Long
    # of the other addresses in the unique_addresses_complete file.
    in_range_addresses = pd.DataFrame()
    for i in range(0, max(old_addresses.count())):
        if within_distance(lat, long, old_addresses['Latitude'][i], old_addresses['Longitude'][i],
                           distance_min):
            in_range_addresses = in_range_addresses.append(old_addresses[i:i + 1],
                                                           ignore_index=True)
        else:
            pass
    return in_range_addresses


# Example: [REPLACE MY PATH WITH YOUR PATH FOR THE UNIQUE_ADDRESSES FILE]
# check number of addresses in 20 block radius
# matrix to store whether other addresses are in the radius
locate_addresses('6 E 36th St', 5,
                 'C:/Users/Drew Daniels/Desktop/Daniels Kitchen Group/CodeTestNotes/Final URLs')
