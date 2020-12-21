import pandas as pd
import time


GAGES = [
        ('SQUW1', 'USGS-38', '12144500','Snoqualmie River - Below the Falls', [15, 20, 31, 41], 'https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=squw1&output=tabular'),
        ('CRNW1', 'USGS-22', '12149000', 'Snoqualmie River near Carnation', [50.7, 54, 56, 58], 'https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=CRNW1&output=tabular'),
        ('CRNZ1', 'USGS-9', '12150400', 'Snoqualmie River at Duvall', None, 'https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=CRNZ1&output=tabular')
        ]


class Gage:

    def __init__(self, name, name2, desc, gage_num, thresholds, url):
        self.name = name
        self.name2 = name2
        self.gage_num = gage_num
        self.thresholds = thresholds
        self.description = desc
        self.url = url
        self.records = self.read_USGS_gage()


    def update(self):
        if self.name2[:4] == 'USGS':
            self.records = self.read_USGS_gage()
            print(self.records[1].head())

    def read_USGS_gage(self):
        try:
            return pd.read_html(self.url)
        except Exception as e:
            print("Error in GetUSGS, get_USGS:\n", e)
            return None


class FloodAlertBot:

    def __init__(self):
        self.gage_list = []


    def input_gages(self, gages):
        for gage_item in gages:
            name1, name2, gage_USGS_ID, desc, thresholds, url = gage_item
            new_gage = Gage(name1, name2, gage_USGS_ID, desc, thresholds, url)
            self.gage_list.append(new_gage)


    def run(self):
        for x in range(1):
            self.update_USGS_gages()
            time.sleep(WAIT_TIME)


    def update_USGS_gages(self):
        for gage in self.gage_list:
            gage.update()



WAIT_TIME = 5

if __name__ == '__main__':
    FAB = FloodAlertBot()
    FAB.input_gages(GAGES)
    FAB.run()