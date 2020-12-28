import pandas as pd
import time


GAGES = [
        ('SQUW1', 'USGS-38', '12144500','Snoqualmie River - Below the Falls', [15, 20, 31, 41], 'https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=squw1&output=tabular'),
]
'''('CRNW1', 'USGS-22', '12149000', 'Snoqualmie River near Carnation', [50.7, 54, 56, 58], 'https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=CRNW1&output=tabular'),
        ('CRNZ1', 'USGS-9', '12150400', 'Snoqualmie River at Duvall', None, 'https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=CRNZ1&output=tabular')
        ]
'''

class Gage:
    """
    Holds relevant gage information:
        ID
        Description
        Source URL
        Important information derived from the last reading
    On update, updates itself.
    Reports data.
    """

    def __init__(self, gage_ID, USGS_ID, USGS_num, desc, thresholds, url):
        # initial information
        self.gage_ID = gage_ID          # Gage ID
        self.USGS_ID = USGS_ID          # USGS ID
        self.USGS_num = USGS_num        # USGS number 2
        self.description = desc         # SVPA Description
        self.thresholds = thresholds    # action thresholds
        self.url = url                  # data url
        self.thresholds = []            # action thresholds

        # information from the data
        self.last_height = None
        self.last_time = None
        self.max_forecast_height = None
        self.max_forecast_time = None


    def update(self):
        """
        Updates member fields using outside information.
        #TODO
        Currently assumes USGS input
        """
        df_list = self.read_USGS_gage()
        self.last_time = df_list[1][0][2]
        self.last_height = df_list[1][2][2]
        self.max_forecast_height, self.max_forecast_time = self.__get_max(df_list[1])

    def __get_max(self, df):
        max_index = None 
        for i in range(len(df[2])):
            if i > 1:
                value_str = df[2][i]
                value = float(value_str[:-2])
                if max_index == None or value > max_index:
                    max_index = i
        print(df[2][max_index])
        return (df[2][max_index], df[0][max_index])


    def read_USGS_gage(self):
        """
        Returns a list of dataframes, corresponding to tables
        found at the gage URL.

        :returns: a list of dataframes.
        """
        try:
            return pd.read_html(self.url)
        except Exception as e:
            print("Error in GetUSGS, get_USGS:\n", e)
            return None

    def get_status(self):
        """
        From the gage records return relevant information.
        """
        status = ''
        status += '{}\n'.format(self.description)
        status += '{} -- {} -- {}\n'.format(self.gage_ID, self.USGS_ID, self.USGS_num)

        status += '\tCurrent Time: {}\n'.format(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(time.time())))
        status += '\tLatest Time: {}\n'.format(self.last_time)
        status += '\tLatest Level: {}\n'.format(self.last_height)
        status += '\tThe highest expected level is: {} at {}'.format(self.max_forecast_height, self.max_forecast_time)
        return status


class FloodAlertBot:

    def __init__(self):
        self.gage_list = []


    def input_gages(self, gages):
        """
        Converts a list of gage information into objects,
        and then appends those objects to a list of gage objects.

        :param gages: (list) Relevant gage information
        """
        for gage_item in gages:
            name1, USGS_ID, gage_USGS_ID, desc, thresholds, url = gage_item
            new_gage = Gage(name1, USGS_ID, gage_USGS_ID, desc, thresholds, url)
            self.gage_list.append(new_gage)


    def run(self):
        """
        The core loop. It waits a set amount of time, updates information,
        then waits again.
        #TODO
        Initiates a second thread that responds to RPCs
        """
        for x in range(1):
            self.update_USGS_gages()
            self.print_USGS_statuses()
            time.sleep(WAIT_TIME)

    def print_USGS_statuses(self):
        """
        Prints out the status of each gage.
        """
        for gage in self.gage_list:
            print(gage.get_status())

    def update_USGS_gages(self):
        """
        Takes the list of gages, and updates each.
        """
        for gage in self.gage_list:
            gage.update()


WAIT_TIME = 5

if __name__ == '__main__':
    FAB = FloodAlertBot()
    FAB.input_gages(GAGES)
    FAB.run()