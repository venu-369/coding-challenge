import sqlite3
import csv
import random
from flask import Flask, render_template, request, flash

# initialize flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Q#qwe121dvj)sndh'

# csv file for reading
london_temp = 'london_temp.csv'

# function to get db connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# route to show index page
@app.route('/')
def index():
    # read from csv and choose a random row
    with open(london_temp) as f:
      reader = csv.reader(f)
      chosen_row = random.choice(list(reader))
      # print the chosen row
      print(chosen_row)
    # render index.html with the chosen row
    return render_template('index.html', randomDate=chosen_row)

# function to save user guess to database
def save_user_guess(guessed_temp, actual_temp, dt):
    # get db connection
    conn = get_db_connection()
    # insert user guess into database
    conn.execute('INSERT INTO user_guesses (guessed_temp, actual_temp, dt) VALUES (?, ?, ?)',
              (guessed_temp, actual_temp, dt))
    # commit changes to database
    conn.commit()
    # close database connection
    conn.close()

# route to compare temperatures
@app.route('/result', methods=('GET', 'POST'))
def compareTemperatures():
    # read from csv file
    with open(london_temp, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # find the row with the chosen date
        foundRowInCsv = [row for row in reader if row['dt'] == request.form['date']]

        # print the found row
        print("foundRowInCsv", foundRowInCsv)

        # convert the found row to an array
        foundRowInCsvAsArray = [foundRowInCsv[0]['dt'], foundRowInCsv[0]['dt_iso'], foundRowInCsv[0]['temp'] ]

        # save user guess to database
        save_user_guess(request.form['guess-temperature'], foundRowInCsvAsArray[2], foundRowInCsv[0]['dt'])

        # convert the guessed and actual temperatures to float
        guessedTemp = float(request.form['guess-temperature'])
        actualTemp = float(foundRowInCsvAsArray[2])

        # print the guessed and actual temperatures
        print("guessedTemp", guessedTemp, "actualTemp:", actualTemp)

        # compare the temperatures
        if guessedTemp == actualTemp:
            flash('You guessed it correctly, Congratulations. You won!')
        elif guessedTemp < actualTemp:
            flash('You guessed lower value, increase value')
        else:
            flash('You guessed higher value, decrease value')



    return render_template('index.html', randomDate=foundRowInCsvAsArray)
