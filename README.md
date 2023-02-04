# Guess-The-Temperature coding challenge

A web application built using flask framework that lets a user guess the temperature and provide feedback to go higher or lower until there is a match.

A really good tutorial about flask with examples: https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3


To run the code: 

 flask run (or) flask -p 5000


Q1: What framework/libraries did you use for the front-end and why?

Ans: Python was used to create this programme, together with the Flask framework and SQLite database. To read and process a temperature, it also makes use  of the Werkzeug, Pandas, and csv packages. csv document With the help of this code, a web application that lets users predict the temperature on a      randomly chosen date and stores the results in a SQLite database will be created. The render template method in Flask will be used to compare the user's estimate and the real temperature and show the results on the front end.


Q2:What framework/libraries did you use for the back-end and why?
Ans: This code makes use of the Flask back-end framework. Sqlite3, Pandas, CSV, and Random are the libraries that were utilised in this project. The web framework is Flask, the database connection and user guesses are stored in sqlite3, the temperature data is read from a csv file using pandas, and a random date is selected at random from the temperature data to display on the index page using random.


Q3: If you had more time, what further improvements or new features would you add?
Ans: If I had more time, I would incorporate the following upgrades and additions: 
      1. Access to specific sites or functions is restricted by user authentication and authorisation. 
      2. Keep track of the user's gaming history and offer a scoreboard with the best results. 
      3. Increase the amount of information in the temperature.csv file and provide users the choice to filter it by time, place, or temperature range. 
      4. Visualize the temperature data using a more user-friendly interface that includes graphs and charts. 
      5. Implement a feature that lets the user select the game's level of difficulty (e.g., easier or harder). 
      6. Include a help section with thorough directions and game rules. 
      7. Improve the website's general look and feel, as well as the performance of the code.


Q4: What steps did you take to future proof the application for possible expansions?
Ans: The programme was not future-proofed in the code to accommodate potential additions. In order to store the user's estimate, the application reads information from a CSV file and stores it in a SQLite database. The CSV file cannot be expanded to accommodate more data, nor can the database be made larger. The application should be future-proofed by taking steps like dynamic data loading, deploying a more scalable database solution, and using the right data management and storage approaches.


Q5:Which part of the challenge are you most proud of and why?
Ans: The implementation of the "compareTemperatures" function is the aspect of the challenge that I am most proud of. This function compares the user-specified temperature to the recorded temperature in the CSV file. It then records both the user's guess and the actual temperature in a database and notifies the user if their guess was accurate, incorrect, or excessively high. I am proud of this function because it combines a number of the project's elements, including reading from the CSV file, saving information to a database, and informing the user of a comparison between two temperatures.



Q6: Which parts did you spend the most time with? What did you find most difficult?
Ans: It could take a while and be difficult to read the CSV file, save the data in a pandas dataframe, and then choose a random row from it. The database storage of user estimate data and comparison of the user's guess with the actual temperature measurement may present further difficulties.
