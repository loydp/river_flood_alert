import pandas as pd
SVPA_test_url = "https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=CRNW1&output=tabular"
USGS_test_url = "https://readingsvc.azurewebsites.net/api/GetGageReadingsUTC?regionId=1&id=SVPA-17&fromDateTime=2020-01-06T16:00:07-08:00&toDateTime=2020-01-10T16:00:07-08:00&showDeletedReadings=false"

class Gage:

    def __init__(self, name, url):
        self.name = name
        self.url = url
        print(name, 'gage is now initialized')


class FloodAlertBot:

    def __init__(self):
        print('GetUSGS initialized')


if __name__ == '__main__':
    data_get = FloodAlertBot()

    # svpa = data_get.get_SVPA_reading(USGS_test_url)
    # usgs = data_get.get_USGS_reading(SVPA_test_url)
    
    # print(usgs[1])
    # print(svpa['readings'][2])
    

'''
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
'''