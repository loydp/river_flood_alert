import numpy as p
import pandas as pd
SVPA_test_url = "https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=CRNW1&output=tabular"


GAGES = [
        ('SQUW1', 'USGS-38', '12144500','Snoqualmie River - Below the Falls', [15, 20, 31, 41], 'https://water.weather.gov/ahps2/hydrograph.php?wfo=sew&gage=squw1'),
        ('CRNW1', 'USGS-22', '12149000' 'Snoqualmie River near Carnation', [50.7, 54, 56, 58], 'https://water.weather.gov/ahps2/hydrograph.php?wfo=sew&gage=CRNW1'),
        ('CRNZ1', 'USGS-9', '12150400', 'Snoqualmie River at Duvall', None, 'https://water.weather.gov/ahps2/hydrograph.php?wfo=sew&gage=CRNZ1')
        ]

class Gage:

    def __init__(self, name, name2, desc, GIN, thresholds, url):
        self.name = name
        self.name2 = name2
        self.gin = GIN
        self.thresholds = thresholds
        self.description = desc
        self.url = url
        print(name, 'gage is now initialized')


class FloodAlertBot:

    def __init__(self):
        gage_list = []
        print('GetUSGS initialized')

    def input_gages(self, gage_list):
        for gage in gage_list:
            name1, name2, GIN, desc, thresholds, url = gage
            new_gage = Gage(name1, name2, GIN, desc, thresholds, url)
            gage_list.append(new_gage)


if __name__ == '__main__':
    FAB = FloodAlertBot()
    FAB.input_gages(GAGES)



    # svpa = data_get.get_SVPA_reading(USGS_test_url)
    # usgs = data_get.get_USGS_reading(SVPA_test_url)
    
    # print(usgs[1])
    # print(svpa['readings'][2])
    
'''

USGS_test_url = "https://readingsvc.azurewebsites.net/api/GetGageReadingsUTC?regionId=1&id=SVPA-17&fromDateTime=2020-01-06T16:00:07-08:00&toDateTime=2020-01-10T16:00:07-08:00&showDeletedReadings=false"

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