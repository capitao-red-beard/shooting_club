# shooting_club

This project is software for a shooting club in The Netherlands. It is a user application which can manage the running of the club, including; housing users in an sqlite3 database, their scores, their purchases and can also be used as a monitoring tool for the club to analyse breakdown of sales and scores of users so at the end of the year they can be given a new class.

The app is contained within a GUI but can also export it's data to excel.

## Dependancies

Please see requirements.txt

However, the main technologies of this project are:

- sqlite3
- tkinter
- pandas
- matplotlib

## Functionality

This app allows for the storage of members of the shooting club. From here they can submit scores to the database at a maximum rate of 1x per week, per discipline. Once a user has submitted scores they will also be e-mailed to them. 

This app also allows users to purchase products from the shooting club, namely scorecards and ammunition. This again will be emailed to the user as a receipt once they have made payment.

The app also has the ability to act as a monitoring tool for an admin user, they will be able to have an overview of purchases made between custom dates they choose. They may be as granular as they want within their search. The same applies for monitoring a user's score. These scores can also be downloaded from the database onto a spreadsheet, which in turn may be printed from the application as a PDF.

## Key points

The app stores encrypted versions of users passwords, this is for security reasons, even though this app does not run online it is an important part of storing user credentials on a database.

The app has a whole file dedicated to input validation, this being a GUI app it is important that we do not clutter the database with rubbish. There are checks built into the code to ensure the same user is not entered twice into the system. 

I decided to add all the GUI code into one file, which on reflection was not the best idea but, it works for now and most code has been commented enough for my needs, I will break-up this GUI file into a more structured way in the future.

Admin user's can add sales items or remove them, or change the stock and price per item as and when needed. A warning will be presented to the user along with an email being sent to all other admins when the stock is running low!

## TO-DO

1. Make the app. into an exe file using pyinstaller == `DONE`
2. Finish off the presenting of data to a user when logged in.
3. Write a function to calculate average score of a user so when new classes are made at the end of the year, the users will know their class automatically, this will be e-mailed to them as and when needed.
4. Add a competition mode to the software so that user's may use the software whom are not native to the club.

## How to

1. Pull this repo using `git clone https://github.com/capitao-red-beard/shooting_club.git`
2. Navigate the the project folder and create a venv using `python3 -m venv venv`
3. Install the dependancies using `pip install -r requirements.txt`
4. Run the code either using `python3 gui.py` or navigate to the `dist` filder and run the `gui` executable
5. Enjoy!
