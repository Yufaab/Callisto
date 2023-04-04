# Data Scrapper for Josaa couselling site

### Steps to generate csv file for any year ###

* Clone the project
* Visit this JOSAA site 
* Download the page after loading data
* Save it as JoSAA.html
* Install the python modules with the command `pip install -r requirements.txt`
* In the scrapper.py file, find this line `dataframe.to_csv('./data/2022/round6.csv', index=False)` and change the values `20xx` and `roundx.csv` accordingly
* Run the python file with the command `python scapper.py`
