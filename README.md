Snowqualmie Valley Preservation Alliance Flood Alert Bot
========================================================

### GENERAL NOTES:
The flood alert bot gathers data from water gages, digests that data and moves it to the people who need to know it.<br>
The program should also be fairly portable/abstract/OO, to allow for it to be adapted to new systems.<br>
The current iteration should interact with a Discord bot to communicate with people using discord or email.<br>
<br>**2020-12-19**


### DEPENDENCIES:
* tested on python 3.9
* pandas
* lxml
* will need discord.py


Currently uses pandas to read tabular tables.  
May be used for series processing later.  
The latest version of windows has a bug that interacts poorly with numpy. So as of now if installing on a windows machine install pandas 1.1.3, which should install numpy 1.19.3.  
In terminal:  
pip install pandas==1.1.3
<br>**2020-12-19**