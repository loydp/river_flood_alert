import pandas as pd
url = "https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=CRNW1&output=tabular"
url2 = "https://readingsvc.azurewebsites.net/api/GetGageReadingsUTC?regionId=1&id=SVPA-17&fromDateTime=2020-01-06T16:00:07-08:00&toDateTime=2020-01-10T16:00:07-08:00&showDeletedReadings=false"
'''
SQUW1
CRNW1
CRNZ1
'''

"""
Every few minutes a class activates a retrieval routine.
At a time based on past data it retrieves information from the gages.
It sends a message to each gage and then stores that information in a class
associated with that gage, deleting old data.
Then:
It looks through the predicted flood level data, and if it exceeds a certain level
(stored in class) and unless told otherwise will send an alert.
The always on class also responds to requests from the bot source.

"""

class DataRetriever:

    def __init__(self):
        print('GetUSGS initialized')

    def get_USGS_reading(self, url):
        try:
            df_list = pd.read_html(url)
            return df_list
        except Exception as e:
            print("Error in GetUSGS, get_USGS:\n", e)
            return None

    def get_SVPA_reading(self, url):
        try:
            df_list = pd.read_json(url)
            return df_list
        except Exception as e:
            print("Error in GetSVPA, get_SVPA:\n", e)
            return None




if __name__ == '__main__':
    data_get = DataRetriever()
    svpa = data_get.get_SVPA_reading(url2)
    usgs = data_get.get_USGS_reading(url)
    
    print(usgs[1])
    print(svpa['readings'][2])
    