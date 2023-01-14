# Tuttitalia Scrapping

## Website

Link:- `https://www.tuttitalia.it/`

Tuttitalia Is A Italia Website That Cantains The Public/Private Schools Information Of Italia. This Website Contains Many-more Information About Italia, But For Now We Only Collect The Information About The Schools In Italia Like Region, Provincia, City, Grade, Name Of School, Address, Type & Code. You Can Go Directly To Link(https://www.tuttitalia.it/scuole/) To Check The Regions Of The Italia School And Explore Some School.

## Description

- This Project Is A Web Scraping Tool That Uses The Python Programming Language And The Selenium Library To Extract Data From Websites Tuttitalia.
It Is Designed To Automate The Process Of Accessing And Navigating Through Web Pages In Order To Collect Specific Information. The Data Collected Can Be Used For A Variety Of Purposes Such As Data Analysis, Machine Learning, Or To Populate A Database.
- This Project Is Useful For Anyone Who Needs To Collect Data From A Large Number Of Web Pages Or For Anyone Who Wants To Automate A Tedious Data Collection Task. It Can Be Customized To Scrape Any Data That Is Visible On A Website And Can Be Scheduled To Run Automatically At A Specific Time Or Frequency.
- In This Project, First We Have To Collect The Link Of The Address/city Of Italia And Store That Link In Our Csv File. Now We Use This Csv To Collect The All Information About The School And Store The Information One By One In Our New Csv File And Save It. Now We Have The Few Information About The The Schools In Italia. 
- For This Project We Have To Be In Patience Because This Script Take Time To Collect Data In Two Steps. We Also Need Fast And Lots Of Internet Because We Going To Collect Data By Going Through Every Page.


## Installation

1. Use Python3
2. Clone the repository: `git clone https://github.com/parteekkamboj9/Scraping.git`
3. Install the required dependencies: `pip install -r requirement.txt`

## Usage

1. Run the 1st script: `getting_links.py`
2. This script well make csv file: `tuttitalia_links.csv`
3. This csv have all links of school area.
4. Run the 2nd script: `information.py`
5. This script well make csv file: `inform.csv`
6. The script will output the result of the scraping school's data.

- `Note:- you can read comments in the script to know about the flow.`


## Known issues and limitations

- The script only works with Python 3
- Some websites block scraping attempts and the script may not work on those sites.
- Need lot of internet with fast network speed.
- This will take time to complete because we hiting on every page and getting the info.

## Contribution/Acknowledgments

You are welcome to contribute to this project by submitting pull requests or reporting bugs.

It's my main goal to provide you with accurate and helpful information. If you have any other questions or need help with anything else, please don't hesitate to ask.

You can ask me anytime using my cantact/social media profile.



