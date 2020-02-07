
def main():
    import pandas as pd
    import numpy as np

    # This script extracts and computes the "6 metrics" (see file 6_desired_metrics_to_parse.txt)
    # for each address in unique_addresses for the 12 search queries. Assumes the unique_addresses dataset
    # contains a count of all entries for that address in all_data after the nan entries in all_data are dropped.
    # Assumes that all empty rows in unique_addresses are populated with zeroes and spelling mistakes for different
    # types of cuisines are corrected.

    # Set path to your datasets.
    all_data = pd.read_csv([YOUR PATH TO ALL_DATA], encoding="ISO-8859-1")
    unique_addresses = pd.read_csv([YOUR PATH TO UNIQUE ADDRESSES],encoding="ISO-8859-1")
    all_nan = pd.read_csv([YOUR PATH TO LIST OF ALL NAs],encoding="ISO-8859-1")

    # Remove nan, '#NAME?' and ' #VALUES?' entries and extraneous columns.
    all_data = all_data.drop(['Unnamed: 13'], axis=1)
    all_data = all_data.replace('#NAME?', np.nan)
    all_data = all_data.replace('#VALUE?', np.nan)
    all_data = all_data.replace('#VALUE!', np.nan)
    all_data = all_data.dropna()

    # Drop duplicate entries
    all_data = all_data.drop_duplicates(all_data)

    # Reset index value.
    all_data = all_data.reset_index()
    # unique_addresses = unique_addresses[0:50]

    # Parse all columns in data set as floating point numbers.
    unique_addresses['Vegan2'] = unique_addresses['Vegan2'].astype(float)
    unique_addresses['Vegan3'] = unique_addresses['Vegan3'].astype(float)
    unique_addresses['Vegan4'] = unique_addresses['Vegan4'].astype(float)
    unique_addresses['Vegan5'] = unique_addresses['Vegan5'].astype(float)
    unique_addresses['Vegan6'] = unique_addresses['Vegan6'].astype(float)
    unique_addresses['Vegan7'] = unique_addresses['Vegan7'].astype(float)

    unique_addresses['Soup2'] = unique_addresses['Soup2'].astype(float)
    unique_addresses['Soup3'] = unique_addresses['Soup3'].astype(float)
    unique_addresses['Soup4'] = unique_addresses['Soup4'].astype(float)
    unique_addresses['Soup5'] = unique_addresses['Soup5'].astype(float)
    unique_addresses['Soup6'] = unique_addresses['Soup6'].astype(float)
    unique_addresses['Soup7'] = unique_addresses['Soup7'].astype(float)

    unique_addresses['BBQ2'] = unique_addresses['BBQ2'].astype(float)
    unique_addresses['BBQ3'] = unique_addresses['BBQ3'].astype(float)
    unique_addresses['BBQ4'] = unique_addresses['BBQ4'].astype(float)
    unique_addresses['BBQ5'] = unique_addresses['BBQ5'].astype(float)
    unique_addresses['BBQ6'] = unique_addresses['BBQ6'].astype(float)
    unique_addresses['BBQ7'] = unique_addresses['BBQ7'].astype(float)

    unique_addresses['Chinese2'] = unique_addresses['Chinese2'].astype(float)
    unique_addresses['Chinese3'] = unique_addresses['Chinese3'].astype(float)
    unique_addresses['Chinese4'] = unique_addresses['Chinese4'].astype(float)
    unique_addresses['Chinese5'] = unique_addresses['Chinese5'].astype(float)
    unique_addresses['Chinese6'] = unique_addresses['Chinese6'].astype(float)
    unique_addresses['Chinese7'] = unique_addresses['Chinese7'].astype(float)

    unique_addresses['Italian2'] = unique_addresses['Italian2'].astype(float)
    unique_addresses['Italian3'] = unique_addresses['Italian3'].astype(float)
    unique_addresses['Italian4'] = unique_addresses['Italian4'].astype(float)
    unique_addresses['Italian5'] = unique_addresses['Italian5'].astype(float)
    unique_addresses['Italian6'] = unique_addresses['Italian6'].astype(float)
    unique_addresses['Italian7'] = unique_addresses['Italian7'].astype(float)

    unique_addresses['Mediterranean2'] = unique_addresses['Mediterranean2'].astype(float)
    unique_addresses['Mediterranean3'] = unique_addresses['Mediterranean3'].astype(float)
    unique_addresses['Mediterranean4'] = unique_addresses['Mediterranean4'].astype(float)
    unique_addresses['Mediterranean5'] = unique_addresses['Mediterranean5'].astype(float)
    unique_addresses['Mediterranean6'] = unique_addresses['Mediterranean6'].astype(float)
    unique_addresses['Mediterranean7'] = unique_addresses['Mediterranean7'].astype(float)

    unique_addresses['Mexican2'] = unique_addresses['Mexican2'].astype(float)
    unique_addresses['Mexican3'] = unique_addresses['Mexican3'].astype(float)
    unique_addresses['Mexican4'] = unique_addresses['Mexican4'].astype(float)
    unique_addresses['Mexican5'] = unique_addresses['Mexican5'].astype(float)
    unique_addresses['Mexican6'] = unique_addresses['Mexican6'].astype(float)
    unique_addresses['Mexican7'] = unique_addresses['Mexican7'].astype(float)

    unique_addresses['Poke2'] = unique_addresses['Poke2'].astype(float)
    unique_addresses['Poke3'] = unique_addresses['Poke3'].astype(float)
    unique_addresses['Poke4'] = unique_addresses['Poke4'].astype(float)
    unique_addresses['Poke5'] = unique_addresses['Poke5'].astype(float)
    unique_addresses['Poke6'] = unique_addresses['Poke6'].astype(float)
    unique_addresses['Poke7'] = unique_addresses['Poke7'].astype(float)

    unique_addresses['Ramen2'] = unique_addresses['Ramen2'].astype(float)
    unique_addresses['Ramen3'] = unique_addresses['Ramen3'].astype(float)
    unique_addresses['Ramen4'] = unique_addresses['Ramen4'].astype(float)
    unique_addresses['Ramen5'] = unique_addresses['Ramen5'].astype(float)
    unique_addresses['Ramen6'] = unique_addresses['Ramen6'].astype(float)
    unique_addresses['Ramen7'] = unique_addresses['Ramen7'].astype(float)

    unique_addresses['Thai2'] = unique_addresses['Thai2'].astype(float)
    unique_addresses['Thai3'] = unique_addresses['Thai3'].astype(float)
    unique_addresses['Thai4'] = unique_addresses['Thai4'].astype(float)
    unique_addresses['Thai5'] = unique_addresses['Thai5'].astype(float)
    unique_addresses['Thai6'] = unique_addresses['Thai6'].astype(float)
    unique_addresses['Thai7'] = unique_addresses['Thai7'].astype(float)

    unique_addresses['Vietnamese2'] = unique_addresses['Vietnamese2'].astype(float)
    unique_addresses['Vietnamese3'] = unique_addresses['Vietnamese3'].astype(float)
    unique_addresses['Vietnamese4'] = unique_addresses['Vietnamese4'].astype(float)
    unique_addresses['Vietnamese5'] = unique_addresses['Vietnamese5'].astype(float)
    unique_addresses['Vietnamese6'] = unique_addresses['Vietnamese6'].astype(float)
    unique_addresses['Vietnamese7'] = unique_addresses['Vietnamese7'].astype(float)

    # Loop over every unique address in unique_addresses file and calculate the metrics
    for i in range(0, len(unique_addresses)):
        for j in range(0, len(all_data)):
            if unique_addresses['Unique Address'][i] == all_data['SearchAddress'][j]:
                if all_data['SearchQuery'][j] == 'Vegan':
                    unique_addresses['Vegan1'][i] = all_data['NumRest'][j]
                    unique_addresses['Vegan2'][i] = float(unique_addresses['Vegan2'][i] + float(all_data['Rating'][j]))
                    unique_addresses['Vegan3'][i] = float(unique_addresses['Vegan3'][i] + float(all_data['Rating2'][j]))
                    unique_addresses['Vegan4'][i] = float(unique_addresses['Vegan4'][i] + float(all_data['NumRating'][j]))
                    unique_addresses['Vegan5'][i] = float(unique_addresses['Vegan5'][i] + float(all_data['NumRating2'][j]))
                    unique_addresses['Vegan6'][i] = float(unique_addresses['Vegan6'][i] + float(all_data['Rating Dif'][j]))
                    unique_addresses['Vegan7'][i] = float(unique_addresses['Vegan7'][i] + float(all_data['Volume weighted rating'][j]))

                if all_data['SearchQuery'][j] == 'Soup':
                    unique_addresses['Soup1'][i] = all_data['NumRest'][j]
                    unique_addresses['Soup2'][i] = float(unique_addresses['Soup2'][i] + float(all_data['Rating'][j]))
                    unique_addresses['Soup3'][i] = float(unique_addresses['Soup3'][i] + float(all_data['Rating2'][j]))
                    unique_addresses['Soup4'][i] = float(unique_addresses['Soup4'][i] + float(all_data['NumRating'][j]))
                    unique_addresses['Soup5'][i] = float(unique_addresses['Soup5'][i] + float(all_data['NumRating2'][j]))
                    unique_addresses['Soup6'][i] = float(unique_addresses['Soup6'][i] + float(all_data['Rating Dif'][j]))
                    unique_addresses['Soup7'][i] = float(unique_addresses['Soup7'][i] + float(all_data['Volume weighted rating'][j]))

                if all_data['SearchQuery'][j] == 'BBQ':
                    unique_addresses['BBQ1'][i] = all_data['NumRest'][j]
                    unique_addresses['BBQ2'][i] = float(unique_addresses['BBQ2'][i] + float(all_data['Rating'][j]))
                    unique_addresses['BBQ3'][i] = float(unique_addresses['BBQ3'][i] + float(all_data['Rating2'][j]))
                    unique_addresses['BBQ4'][i] = float(unique_addresses['BBQ4'][i] + float(all_data['NumRating'][j]))
                    unique_addresses['BBQ5'][i] = float(unique_addresses['BBQ5'][i] + float(all_data['NumRating2'][j]))
                    unique_addresses['BBQ6'][i] = float(unique_addresses['BBQ6'][i] + float(all_data['Rating Dif'][j]))
                    unique_addresses['BBQ7'][i] = float(unique_addresses['BBQ7'][i] + float(all_data['Volume weighted rating'][j]))

                if all_data['SearchQuery'][j] == 'Chinese':
                    unique_addresses['Chinese1'][i] = all_data['NumRest'][j]
                    unique_addresses['Chinese2'][i] = float(unique_addresses['Chinese2'][i] + float(all_data['Rating'][j]))
                    unique_addresses['Chinese3'][i] = float(unique_addresses['Chinese3'][i] + float(all_data['Rating2'][j]))
                    unique_addresses['Chinese4'][i] = float(unique_addresses['Chinese4'][i] + float(all_data['NumRating'][j]))
                    unique_addresses['Chinese5'][i] = float(unique_addresses['Chinese5'][i] + float(all_data['NumRating2'][j]))
                    unique_addresses['Chinese6'][i] = float(unique_addresses['Chinese6'][i] + float(all_data['Rating Dif'][j]))
                    unique_addresses['Chinese7'][i] = float(unique_addresses['Chinese7'][i] + float(all_data['Volume weighted rating'][j]))

                if all_data['SearchQuery'][j] == 'Italian':
                    unique_addresses['Italian1'][i] = all_data['NumRest'][j]
                    unique_addresses['Italian2'][i] = float(unique_addresses['Italian2'][i] + float(all_data['Rating'][j]))
                    unique_addresses['Italian3'][i] = float(unique_addresses['Italian3'][i] + float(all_data['Rating2'][j]))
                    unique_addresses['Italian4'][i] = float(unique_addresses['Italian4'][i] + float(all_data['NumRating'][j]))
                    unique_addresses['Italian5'][i] = float(unique_addresses['Italian5'][i] + float(all_data['NumRating2'][j]))
                    unique_addresses['Italian6'][i] = float(unique_addresses['Italian6'][i] + float(all_data['Rating Dif'][j]))
                    unique_addresses['Italian7'][i] = float(unique_addresses['Italian7'][i] + float(all_data['Volume weighted rating'][j]))

                if all_data['SearchQuery'][j] == 'Mediterranean':
                    unique_addresses['Mediterranean1'][i] = all_data['NumRest'][j]
                    unique_addresses['Mediterranean2'][i] = float(unique_addresses['Mediterranean2'][i] + float(all_data['Rating'][j]))
                    unique_addresses['Mediterranean3'][i] = float(unique_addresses['Mediterranean3'][i] + float(all_data['Rating2'][j]))
                    unique_addresses['Mediterranean4'][i] = float(unique_addresses['Mediterranean4'][i] + float(all_data['NumRating'][j]))
                    unique_addresses['Mediterranean5'][i] = float(unique_addresses['Mediterranean5'][i] + float(all_data['NumRating2'][j]))
                    unique_addresses['Mediterranean6'][i] = float(unique_addresses['Mediterranean6'][i] + float(all_data['Rating Dif'][j]))
                    unique_addresses['Mediterranean7'][i] = float(unique_addresses['Mediterranean7'][i] + float(all_data['Volume weighted rating'][j]))

                if all_data['SearchQuery'][j] == 'Mexican':
                    unique_addresses['Mexican1'][i] = all_data['NumRest'][j]
                    unique_addresses['Mexican2'][i] = float(unique_addresses['Mexican2'][i] + float(all_data['Rating'][j]))
                    unique_addresses['Mexican3'][i] = float(unique_addresses['Mexican3'][i] + float(all_data['Rating2'][j]))
                    unique_addresses['Mexican4'][i] = float(unique_addresses['Mexican4'][i] + float(all_data['NumRating'][j]))
                    unique_addresses['Mexican5'][i] = float(unique_addresses['Mexican5'][i] + float(all_data['NumRating2'][j]))
                    unique_addresses['Mexican6'][i] = float(unique_addresses['Mexican6'][i] + float(all_data['Rating Dif'][j]))
                    unique_addresses['Mexican7'][i] = float(unique_addresses['Mexican7'][i] + float(all_data['Volume weighted rating'][j]))

                if all_data['SearchQuery'][j] == 'Pho':
                    unique_addresses['Pho1'][i] = all_data['NumRest'][j]
                    unique_addresses['Pho2'][i] = float(unique_addresses['Pho2'][i] + float(all_data['Rating'][j]))
                    unique_addresses['Pho3'][i] = float(unique_addresses['Pho3'][i] + float(all_data['Rating2'][j]))
                    unique_addresses['Pho4'][i] = float(unique_addresses['Pho4'][i] + float(all_data['NumRating'][j]))
                    unique_addresses['Pho5'][i] = float(unique_addresses['Pho5'][i] + float(all_data['NumRating2'][j]))
                    unique_addresses['Pho6'][i] = float(unique_addresses['Pho6'][i] + float(all_data['Rating Dif'][j]))
                    unique_addresses['Pho7'][i] = float(unique_addresses['Pho7'][i] + float(all_data['Volume weighted rating'][j]))

                if all_data['SearchQuery'][j] == 'Poke':
                    unique_addresses['Poke1'][i] = all_data['NumRest'][j]
                    unique_addresses['Poke2'][i] = float(unique_addresses['Poke2'][i] + float(all_data['Rating'][j]))
                    unique_addresses['Poke3'][i] = float(unique_addresses['Poke3'][i] + float(all_data['Rating2'][j]))
                    unique_addresses['Poke4'][i] = float(unique_addresses['Poke4'][i] + float(all_data['NumRating'][j]))
                    unique_addresses['Poke5'][i] = float(unique_addresses['Poke5'][i] + float(all_data['NumRating2'][j]))
                    unique_addresses['Poke6'][i] = float(unique_addresses['Poke6'][i] + float(all_data['Rating Dif'][j]))
                    unique_addresses['Poke7'][i] = float(unique_addresses['Poke7'][i] + float(all_data['Volume weighted rating'][j]))

                if all_data['SearchQuery'][j] == 'Ramen':
                    unique_addresses['Ramen1'][i] = all_data['NumRest'][j]
                    unique_addresses['Ramen2'][i] = float(unique_addresses['Ramen2'][i] + float(all_data['Rating'][j]))
                    unique_addresses['Ramen3'][i] = float(unique_addresses['Ramen3'][i] + float(all_data['Rating2'][j]))
                    unique_addresses['Ramen4'][i] = float(unique_addresses['Ramen4'][i] + float(all_data['NumRating'][j]))
                    unique_addresses['Ramen5'][i] = float(unique_addresses['Ramen5'][i] + float(all_data['NumRating2'][j]))
                    unique_addresses['Ramen6'][i] = float(unique_addresses['Ramen6'][i] + float(all_data['Rating Dif'][j]))
                    unique_addresses['Ramen7'][i] = float(unique_addresses['Ramen7'][i] + float(all_data['Volume weighted rating'][j]))

                if all_data['SearchQuery'][j] == 'Thai':
                    unique_addresses['Thai1'][i] = all_data['NumRest'][j]
                    unique_addresses['Thai2'][i] = float(unique_addresses['Thai2'][i] + float(all_data['Rating'][j]))
                    unique_addresses['Thai3'][i] = float(unique_addresses['Thai3'][i] + float(all_data['Rating2'][j]))
                    unique_addresses['Thai4'][i] = float(unique_addresses['Thai4'][i] + float(all_data['NumRating'][j]))
                    unique_addresses['Thai5'][i] = float(unique_addresses['Thai5'][i] + float(all_data['NumRating2'][j]))
                    unique_addresses['Thai6'][i] = float(unique_addresses['Thai6'][i] + float(all_data['Rating Dif'][j]))
                    unique_addresses['Thai7'][i] = float(unique_addresses['Thai7'][i] + float(all_data['Volume weighted rating'][j]))

                if all_data['SearchQuery'][j] == 'Vietnamese':
                    unique_addresses['Vietnamese1'][i] = all_data['NumRest'][j]
                    unique_addresses['Vietnamese2'][i] = float(unique_addresses['Vietnamese2'][i] + float(all_data['Rating'][j]))
                    unique_addresses['Vietnamese3'][i] = float(unique_addresses['Vietnamese3'][i] + float(all_data['Rating2'][j]))
                    unique_addresses['Vietnamese4'][i] = float(unique_addresses['Vietnamese4'][i] + float(all_data['NumRating'][j]))
                    unique_addresses['Vietnamese5'][i] = float(unique_addresses['Vietnamese5'][i] + float(all_data['NumRating2'][j]))
                    unique_addresses['Vietnamese6'][i] = float(unique_addresses['Vietnamese6'][i] + float(all_data['Rating Dif'][j]))
                    unique_addresses['Vietnamese7'][i] = float(unique_addresses['Vietnamese7'][i] + float(all_data['Volume weighted rating'][j]))

    # Normalize all of the summed metrics by the appropriate data counts based on the desired metrics outlined in
    # '6_desired_metrics_to_parse.txt'

        # Normalize the Vegan averages.
        unique_addresses['Vegan2'][i] = unique_addresses['Vegan2'][i] / float(unique_addresses['Vegan1'][i])
        unique_addresses['Vegan3'][i] = unique_addresses['Vegan3'][i] / float(unique_addresses['Vegan1'][i])
        unique_addresses['Vegan7'][i] = unique_addresses['Vegan7'][i] / float(unique_addresses['Vegan4'][i])
        unique_addresses['Vegan4'][i] = unique_addresses['Vegan4'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Vegan5'][i] = unique_addresses['Vegan5'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Vegan6'][i] = unique_addresses['Vegan6'][i] / float(unique_addresses['Count'][i])

        # Normalize the Soup averages.
        unique_addresses['Soup2'][i] = unique_addresses['Soup2'][i] / float(unique_addresses['Soup1'][i])
        unique_addresses['Soup3'][i] = unique_addresses['Soup3'][i] / float(unique_addresses['Soup1'][i])
        unique_addresses['Soup7'][i] = unique_addresses['Soup7'][i] / float(unique_addresses['Soup4'][i])
        unique_addresses['Soup4'][i] = unique_addresses['Soup4'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Soup5'][i] = unique_addresses['Soup5'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Soup6'][i] = unique_addresses['Soup6'][i] / float(unique_addresses['Count'][i])

        # Normalize the BBQ averages.
        unique_addresses['BBQ2'][i] = unique_addresses['BBQ2'][i] / float(unique_addresses['BBQ1'][i])
        unique_addresses['BBQ3'][i] = unique_addresses['BBQ3'][i] / float(unique_addresses['BBQ1'][i])
        unique_addresses['BBQ7'][i] = unique_addresses['BBQ7'][i] / float(unique_addresses['BBQ4'][i])
        unique_addresses['BBQ4'][i] = unique_addresses['BBQ4'][i] / float(unique_addresses['Count'][i])
        unique_addresses['BBQ5'][i] = unique_addresses['BBQ5'][i] / float(unique_addresses['Count'][i])
        unique_addresses['BBQ6'][i] = unique_addresses['BBQ6'][i] / float(unique_addresses['Count'][i])

        # Normalize the Chinese averages.
        unique_addresses['Chinese2'][i] = unique_addresses['Chinese2'][i] / float(unique_addresses['Chinese1'][i])
        unique_addresses['Chinese3'][i] = unique_addresses['Chinese3'][i] / float(unique_addresses['Chinese1'][i])
        unique_addresses['Chinese7'][i] = unique_addresses['Chinese7'][i] / float(unique_addresses['Chinese4'][i])
        unique_addresses['Chinese4'][i] = unique_addresses['Chinese4'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Chinese5'][i] = unique_addresses['Chinese5'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Chinese6'][i] = unique_addresses['Chinese6'][i] / float(unique_addresses['Count'][i])

        # Normalize the Italian averages.
        unique_addresses['Italian2'][i] = unique_addresses['Italian2'][i] / float(unique_addresses['Italian1'][i])
        unique_addresses['Italian3'][i] = unique_addresses['Italian3'][i] / float(unique_addresses['Italian1'][i])
        unique_addresses['Italian7'][i] = unique_addresses['Italian7'][i] / float(unique_addresses['Italian4'][i])
        unique_addresses['Italian4'][i] = unique_addresses['Italian4'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Italian5'][i] = unique_addresses['Italian5'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Italian6'][i] = unique_addresses['Italian6'][i] / float(unique_addresses['Count'][i])

        # Normalize the Mediterranean averages.
        unique_addresses['Mediterranean2'][i] = unique_addresses['Mediterranean2'][i] / float(
            unique_addresses['Mediterranean1'][i])
        unique_addresses['Mediterranean3'][i] = unique_addresses['Mediterranean3'][i] / float(
            unique_addresses['Mediterranean1'][i])
        unique_addresses['Mediterranean7'][i] = unique_addresses['Mediterranean7'][i] / float(
            unique_addresses['Mediterranean4'][i])
        unique_addresses['Mediterranean4'][i] = unique_addresses['Mediterranean4'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Mediterranean5'][i] = unique_addresses['Mediterranean5'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Mediterranean6'][i] = unique_addresses['Mediterranean6'][i] / float(unique_addresses['Count'][i])

        # Normalize the Mexican averages.
        unique_addresses['Mexican2'][i] = unique_addresses['Mexican2'][i] / float(unique_addresses['Mexican1'][i])
        unique_addresses['Mexican3'][i] = unique_addresses['Mexican3'][i] / float(unique_addresses['Mexican1'][i])
        unique_addresses['Mexican7'][i] = unique_addresses['Mexican7'][i] / float(unique_addresses['Mexican4'][i])
        unique_addresses['Mexican4'][i] = unique_addresses['Mexican4'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Mexican5'][i] = unique_addresses['Mexican5'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Mexican6'][i] = unique_addresses['Mexican6'][i] / float(unique_addresses['Count'][i])

        # Normalize the Pho averages.
        unique_addresses['Pho2'][i] = unique_addresses['Pho2'][i] / float(unique_addresses['Pho1'][i])
        unique_addresses['Pho3'][i] = unique_addresses['Pho3'][i] / float(unique_addresses['Pho1'][i])
        unique_addresses['Pho7'][i] = unique_addresses['Pho7'][i] / float(unique_addresses['Pho4'][i])
        unique_addresses['Pho4'][i] = unique_addresses['Pho4'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Pho5'][i] = unique_addresses['Pho5'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Pho6'][i] = unique_addresses['Pho6'][i] / float(unique_addresses['Count'][i])

        # Normalize the Poke averages.
        unique_addresses['Poke2'][i] = unique_addresses['Poke2'][i] / float(unique_addresses['Poke1'][i])
        unique_addresses['Poke3'][i] = unique_addresses['Poke3'][i] / float(unique_addresses['Poke1'][i])
        unique_addresses['Poke7'][i] = unique_addresses['Poke7'][i] / float(unique_addresses['Poke4'][i])
        unique_addresses['Poke4'][i] = unique_addresses['Poke4'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Poke5'][i] = unique_addresses['Poke5'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Poke6'][i] = unique_addresses['Poke6'][i] / float(unique_addresses['Count'][i])

        # Normalize the Ramen averages.
        unique_addresses['Ramen2'][i] = unique_addresses['Ramen2'][i] / float(unique_addresses['Ramen1'][i])
        unique_addresses['Ramen3'][i] = unique_addresses['Ramen3'][i] / float(unique_addresses['Ramen1'][i])
        unique_addresses['Ramen7'][i] = unique_addresses['Ramen7'][i] / float(unique_addresses['Ramen4'][i])
        unique_addresses['Ramen4'][i] = unique_addresses['Ramen4'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Ramen5'][i] = unique_addresses['Ramen5'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Ramen6'][i] = unique_addresses['Ramen6'][i] / float(unique_addresses['Count'][i])

        # Normalize the Thai averages.
        unique_addresses['Thai2'][i] = unique_addresses['Thai2'][i] / float(unique_addresses['Thai1'][i])
        unique_addresses['Thai3'][i] = unique_addresses['Thai3'][i] / float(unique_addresses['Thai1'][i])
        unique_addresses['Thai7'][i] = unique_addresses['Thai7'][i] / float(unique_addresses['Thai4'][i])
        unique_addresses['Thai4'][i] = unique_addresses['Thai4'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Thai5'][i] = unique_addresses['Thai5'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Thai6'][i] = unique_addresses['Thai6'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Thai7'][i] = unique_addresses['Thai7'][i] / float(unique_addresses['Count'][i])

        # Normalize the Vietnamese averages.
        unique_addresses['Vietnamese2'][i] = unique_addresses['Vietnamese2'][i] / float(unique_addresses['Vietnamese1'][i])
        unique_addresses['Vietnamese3'][i] = unique_addresses['Vietnamese3'][i] / float(unique_addresses['Vietnamese1'][i])
        unique_addresses['Vietnamese7'][i] = unique_addresses['Vietnamese7'][i] / float(unique_addresses['Vietnamese4'][i])
        unique_addresses['Vietnamese4'][i] = unique_addresses['Vietnamese4'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Vietnamese5'][i] = unique_addresses['Vietnamese5'][i] / float(unique_addresses['Count'][i])
        unique_addresses['Vietnamese6'][i] = unique_addresses['Vietnamese6'][i] / float(unique_addresses['Count'][i])

    print('All Done')

    # Print a header for the output file to confirm and save file to disk.
    print(unique_addresses.head())
    unique_addresses.to_csv('6_metric_parsed_data_01_09_20.csv', float_format="%.3f")

if __name__=="__main__":
    main()