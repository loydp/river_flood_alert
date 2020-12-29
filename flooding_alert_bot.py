import pandas as pd
import time
import threading


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
    On update(), updates itself.
    Reports data on get_status().
    """

    def __init__(self, gage_ID, USGS_ID, USGS_num, desc, thresholds, url):
        # initial information
        self.gage_ID = gage_ID          # Gage ID
        self.USGS_ID = USGS_ID          # USGS ID
        self.USGS_num = USGS_num        # USGS number 2
        self.description = desc         # SVPA Description
        self.thresholds = thresholds    # action thresholds
        self.url = url                  # data url
        self.thresholds = thresholds    # action thresholds

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
        self.max_forecast_height, self.max_forecast_time = self.__get_max(df_list[2])

    def __get_max(self, df):
        max_index = None 
        for i in range(len(df[2])):
            if i > 1:
                value_str = df[2][i]
                value = float(value_str[:-2])
                if max_index == None or value > max_index:
                    max_index = i
        return (float(df[2][max_index][:2]), df[0][max_index])


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
        # TODO throw an excption: must load gages first
        if self.max_forecast_height > self.thresholds[0]:
            return "Uh oh!"
        status = ''
        status += '{}\n'.format(self.description)
        status += '{} -- {} -- {}\n'.format(self.gage_ID, self.USGS_ID, self.USGS_num)

        status += '\tCurrent Time: {}\n'.format(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(time.time())))
        status += '\tLatest Time: {}\n'.format(self.last_time)
        status += '\tLatest Level: {}\n'.format(self.last_height)
        # TODO something
        '''
        Latest Time: 12/29 06:30
        Latest Level: 5.40ft
        The highest expected level is: 5.0 at 12.0
        '''
        status += '\tThe highest expected level is: {} at {}\n'.format(self.max_forecast_height, self.max_forecast_time)
        status += '\tWhere the thresholds are: {}'.format(self.thresholds)
        return status


class FloodAlertBot:

    def __init__(self):
        self.gage_list = []

    def run(self):
        """
        The core loop. It waits a set amount of time, updates information,
        then waits again.
        #TODO
        Initiates a second thread that responds to RPCs
        """
        server = threading.Thread(target=self.__remote_event)
        server.start()
        self.__timed_event()


    def __timed_event(self):
        # while true
        for x in range(1):
            self.update_USGS_gages()
            statuses = self.get_USGS_statuses()
            self.send_to_discord(statuses)
            time.sleep(WAIT_TIME)


    def send_to_discord(self, statuses):
        #FIXME
        print(statuses)


    def __remote_event(self):
        #while true
        #accept incoming requests
        print('remote event')
        while True:
            time.sleep(3)
            self.send_to_discord('Hello')

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


    def get_USGS_statuses(self):
        """
        Accesses and returns gage status information.
        """
        status = ''
        for gage in self.gage_list:
            status += gage.get_status()
        return status


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
