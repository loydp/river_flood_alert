Project description, for dev use:
Every few minutes a class activates a retrieval routine.
At a time based on past data it retrieves information from the gages.
It sends a message to each gage and then stores that information in a class
associated with that gage, deleting old data.
Then:
It looks through the predicted flood level data, and if it exceeds a certain level
(stored in class) and unless told otherwise will send an alert.
The always on class also responds to requests from the bot source.


https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=CRNW1&output=tabular
https://readingsvc.azurewebsites.net/api/GetGageReadingsUTC?regionId=1&id=SVPA-17&fromDateTime=2020-01-06T16:00:07-08:00&toDateTime=2020-01-10T16:00:07-08:00&showDeletedReadings=false

SQUW1
CRNW1
CRNZ1
