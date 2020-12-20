import pandas as pd
import time
SVPA_test_url = "https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=CRNW1&output=tabular"


GAGES = [
        ('SQUW1', 'USGS-38', '12144500','Snoqualmie River - Below the Falls', [15, 20, 31, 41], 'https://water.weather.gov/ahps2/hydrograph.php?wfo=sew&gage=squw1'),
        ('CRNW1', 'USGS-22', '12149000', 'Snoqualmie River near Carnation', [50.7, 54, 56, 58], 'https://water.weather.gov/ahps2/hydrograph.php?wfo=sew&gage=CRNW1'),
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
        self.gage_list = []
        print('GetUSGS initialized')

    def input_gages(self, gages):
        for gage_item in gages:
            name1, name2, GIN, desc, thresholds, url = gage_item
            new_gage = Gage(name1, name2, GIN, desc, thresholds, url)
            self.gage_list.append(new_gage)

    def run(self):
        for x in range(10):
            time.sleep(WAIT_TIME)
            self.print_stuff()

    def print_stuff(self):
        print('stuff')

WAIT_TIME = 5

if __name__ == '__main__':
    FAB = FloodAlertBot()
    FAB.input_gages(GAGES)
    FAB.run()