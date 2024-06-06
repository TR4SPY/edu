import sqlite3

#   Connect to a SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('flights.db')

#   Create a cursor object to execute SQL commands
c = conn.cursor()

### SQL Queries in order to create the tables if those do not exist
#   Create the Aircraft table to store Aircrafts information
c.execute('''CREATE TABLE IF NOT EXISTS Aircraft (
                Aircraft_ID INT PRIMARY KEY,
                Type TEXT,
                Model TEXT,
                Capacity INT)''')

#   Create the Flight table to store Flights information
c.execute('''CREATE TABLE IF NOT EXISTS Flight (
                Flight_ID INT PRIMARY KEY,
                Aircraft_ID INT,
                Pilot_ID INT,
                Origin TEXT NOT NULL,
                Destination TEXT NOT NULL,
                Date DATE NOT NULL,
                FOREIGN KEY (Aircraft_ID) REFERENCES Aircraft(Aircraft_ID)
                ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (Pilot_ID) REFERENCES Pilot(Pilot_ID)
                ON UPDATE CASCADE ON DELETE CASCADE);''')

#   Create the Pilot create_table to store Pilots information
c.execute('''CREATE TABLE IF NOT EXISTS Pilot (
                Pilot_ID INT PRIMARY KEY,
                Name TEXT,
                License_Number INT,
                Phone_Number INT)''')

#   Create the Operate table to store the many-to-many relationship
c.execute('''CREATE TABLE IF NOT EXISTS Operate (
                Flight_ID INT,
                Pilot_ID INT,
                FOREIGN KEY (Flight_ID) REFERENCES Flight(Flight_ID)
                ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (Pilot_ID) REFERENCES Pilot(Pilot_ID)
                ON UPDATE CASCADE ON DELETE CASCADE);''')

#   Commit the changes and close the connection
conn.commit()
conn.close()


### Defining functions that are later called in the main function
### Functions such as: operations (add/delete/update/view) or custom functions that are eliminating repetition of the code
#   Define add_flight function
def add_flight(flight_id, origin, destination, date, aircraft_id, pilot_id):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  #   A while loop that prompts the user if wants to try again after an error occurs in this case same unique ID of the Pilot
  while True:
    # Check if the Pilot_ID exists in the Pilot table
    c.execute("SELECT * FROM Pilot WHERE Pilot_ID = ?", (pilot_id, ))
    result = c.fetchone()
    if result:
      break
    else:
      print("A Pilot with that ID does not exist. Please enter a valid ID.")
      pilot_id = input("Enter a valid Pilot ID: ")

#   A while loop that prompts the user if wants to try again after an error occurs in this case same unique ID of the Flight
  while True:
    try:
      c.execute(
        "INSERT INTO Flight (Flight_ID, Origin, Destination, Date, Aircraft_ID, Pilot_ID) VALUES (?,?,?,?,?,?)",
        (flight_id, origin, destination, date, aircraft_id, pilot_id))
      print("Flight added successfully!")
      break
    except sqlite3.IntegrityError:
      print(
        "A Flight with that ID already exists. Please enter a different ID.")
      flight_id = input("Enter a new ID for the Flight: ")

  conn.commit()
  conn.close()


#   Define delete_flight function
def delete_flight(flight_id):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  #   A while loop that prompts the user if wants to try again after an error occurs in this case the ID of the Flight does not exist
  while True:
    # Check if the flight_id exists in the Flight table
    c.execute("SELECT * FROM Flight WHERE Flight_ID = ?", (flight_id, ))
    result = c.fetchone()
    if result:
      c.execute("DELETE FROM Flight WHERE Flight_ID = ?", (flight_id, ))
      print("Flight deleted successfully!")
      break
    else:
      print("A Flight with that ID does not exist. Please enter a valid ID.")
      flight_id = input("Enter a valid Flight ID: ")

  conn.commit()
  conn.close()


#   Define add_aircraft function
def add_aircraft(aircraft_id, type, model, capacity):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  c.execute(
    "INSERT INTO Aircraft (Aircraft_ID, Type, Model, Capacity) VALUES (?,?,?,?)",
    (aircraft_id, type, model, capacity))

  conn.commit()
  conn.close()


#   Define delete_aircraft function
def delete_aircraft(aircraft_id):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  #   A while loop that prompts the user if wants to try again after an error occurs in this case the ID of the Flight does not exist
  while True:
    # Check if the Pilot_ID exists in the Pilot table
    c.execute("SELECT * FROM Aircraft WHERE Aircraft_ID = ?", (aircraft_id, ))
    result = c.fetchone()
    if result:
      c.execute("DELETE FROM Aircraft WHERE Aircraft_ID = ?", (aircraft_id, ))
      print("Aircraft deleted successfully!")
      break
    else:
      print(
        "An Aircraft with that ID does not exist. Please enter a valid ID.")
      aircraft_id = input("Enter a valid Aircraft's ID: ")


#   Define update_aircraft function
def update_aircraft(aircraft_id, type, model, capacity):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  #   A while loop that prompts the user if wants to try again after an error occurs in this case the ID of the Aircraft does not exist
  while True:
    c.execute("SELECT * FROM Aircraft WHERE Aircraft_ID = ?", (aircraft_id, ))
    result = c.fetchone()
    if result:
      c.execute(
        "UPDATE Aircraft SET Type = ?, Model = ?, Capacity =? WHERE Aircraft_ID = ?",
        (type, model, capacity, aircraft_id))
      print("Aircraft updated successfully!")
      break
    else:
      print("A Aircraft with that ID does not exist. Please enter a valid ID.")
      pilot_id = input("Enter a valid Aircraft ID: ")

  conn.commit()
  conn.close()


#   Define add_pilot function
def add_pilot(pilot_id, name, license_number, phone_number):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  c.execute(
    "INSERT INTO Pilot (Pilot_ID, Name, License_Number, Phone_Number) VALUES (?,?,?,?)",
    (pilot_id, name, license_number, phone_number))

  conn.commit()
  conn.close()


#   Define delete_pilot function
def delete_pilot(pilot_id):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  #   A while loop that prompts the user if wants to try again after an error occurs in this case the ID of the Pilot does not exist
  while True:
    # Check if the Pilot_ID exists in the Pilot table
    c.execute("SELECT * FROM Pilot WHERE Pilot_ID = ?", (pilot_id, ))
    result = c.fetchone()
    if result:
      c.execute("DELETE FROM Pilot WHERE Pilot_ID = ?", (pilot_id, ))
      print("Pilot deleted successfully!")
      break
    else:
      print("A Pilot with that ID does not exist. Please enter a valid ID.")
      pilot_id = input("Enter a valid Pilot's ID: ")

  conn.commit()
  conn.close()


#   Define update_pilot function
def update_pilot(pilot_id, name, license_number, phone_number):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  #   A while loop that prompts the user if wants to try again after an error occurs in this case same the ID of the Pilot does not exist
  while True:
    c.execute("SELECT * FROM Pilot WHERE Pilot_ID = ?", (pilot_id, ))
    result = c.fetchone()
    if result:
      c.execute(
        "UPDATE Pilot SET Name = ?, License_number = ?, Phone_number = ? WHERE Pilot_ID = ?",
        (name, license_number, phone_number, pilot_id))
      print("Pilot updated successfully!")
      break
    else:
      print("A Pilot with that ID does not exist. Please enter a valid ID.")
      pilot_id = input("Enter a valid Pilot's ID: ")

  conn.commit()
  conn.close()


#   Define add_operate function
def add_operate(pilot_id, flight_id):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  c.execute("INSERT INTO Operate (Pilot_ID, Flight_ID) VALUES (?,?)",
            (pilot_id, flight_id))

  conn.commit()
  conn.close()


#   Define update_flight function
def update_flight(flight_id, origin, destination, date, aircraft_id, pilot_id):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  c.execute(
    "UPDATE Flight SET Origin =?, Destination = ?, Date = ?, Aircraft_ID = ?, Pilot_ID = ? WHERE Flight_ID = ?",
    (origin, destination, date, aircraft_id, pilot_id, flight_id))

  conn.commit()
  conn.close()


#   Define search_flight function
def search_flight(flight_id):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  c.execute("SELECT * FROM Flight WHERE Flight_ID = ?", (flight_id, ))
  #   Fetches a single record. None is returned if there is no record to fetch
  flight_info = c.fetchone()

  #   If single record is returned, print the result and align to the left with the width specified (default 15)
  if flight_info:
    print("Flight ID".ljust(15) + "|" + "Aircraft ID".ljust(15) + "|" +
          "Pilot ID".ljust(15) + "|" + "Origin".ljust(15) + "|" +
          "Destination".ljust(15) + "|" + "Date".ljust(15))
    flight_id, aircraft_id, pilot_id, origin, destination, date = flight_info
    print(f"{flight_id}".ljust(15) + "|" + f"{aircraft_id}".ljust(15) + "|" +
          f"{pilot_id}".ljust(15) + "|" + f"{origin}".ljust(15) + "|" +
          f"{destination}".ljust(15) + "|" + f"{date}".ljust(15))
    return flight_info

  else:
    print("No flights found.")
    return None

  c.close()
  conn.close()


#   Define search_flight_by_destination_and_date function
def search_flight_by_destination_and_date(destination, date):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  c.execute("SELECT * FROM Flight WHERE Destination = ? AND Date = ?",
            (destination, date))
  #   Fetches all the rows of a query result. Returns all the rows as a list of tuples. An empty list is returned if there is no record to fetch
  flight_info = c.fetchall()

  #   If list of tuples returned, print the results align to the left with the width specified (default 15)
  if flight_info:
    print("Flight ID".ljust(15) + "|" + "Aircraft ID".ljust(15) + "|" +
          "Pilot ID".ljust(15) + "|" + "Origin".ljust(15) + "|" +
          "Destination".ljust(15) + "|" + "Date".ljust(15))
    for row in flight_info:
      flight_id, aircraft_id, pilot_id, origin, destination, date = row
      print(f"{flight_id}".ljust(15) + "|" + f"{aircraft_id}".ljust(15) + "|" +
            f"{pilot_id}".ljust(15) + "|" + f"{origin}".ljust(15) + "|" +
            f"{destination}".ljust(15) + "|" + f"{date}".ljust(15))
    return flight_info

  else:
    print("No flights found.")
    return None

  c.close()
  conn.close()


#   Define view_flights function
def view_flights():
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  c.execute("SELECT * FROM Flight")
  #   Fetches all the rows of a query result. Returns all the rows as a list of tuples. An empty list is returned if there is no record to fetch
  flight_info = c.fetchall()

  #   If list of tuples returned, print the results align to the left with the width specified (default 15)
  if flight_info:
    print("Flight ID".ljust(15) + "|" + "Aircraft ID".ljust(15) + "|" +
          "Pilot ID".ljust(15) + "|" + "Origin".ljust(15) + "|" +
          "Destination".ljust(15) + "|" + "Date".ljust(15))
    for row in flight_info:
      flight_id, aircraft_id, pilot_id, origin, destination, date = row
      print(f"{flight_id}".ljust(15) + "|" + f"{aircraft_id}".ljust(15) + "|" +
            f"{pilot_id}".ljust(15) + "|" + f"{origin}".ljust(15) + "|" +
            f"{destination}".ljust(15) + "|" + f"{date}".ljust(15))
    return flight_info
  else:
    print("No flights found.")
    return None

  c.close()
  conn.close()


#   Define flights_per_week function
def flights_per_week(week):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  #   Indicate how many flights are in the database in the certain week
  c.execute("SELECT COUNT(*) FROM Flight WHERE strftime('%W', Date) = ?",
            (week, ))
  flights_count = c.fetchone()[0]

  conn.commit()
  conn.close()

  return flights_count


#   Define flights_per_destination function
def flights_per_destination(destination):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  #   Indicate how many flights are in the database as per certain destination
  c.execute("SELECT COUNT(*) FROM Flight WHERE Destination = ?",
            (destination, ))
  flights_count = c.fetchone()[0]

  conn.commit()
  conn.close()

  return flights_count


#   Define flights_per_month function
def flights_per_month(month):
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  #   Indicate how many flights are in the database in the certain month
  c.execute("SELECT COUNT(*) FROM Flight WHERE strftime('%m', Date) = ?",
            (month, ))
  flights_count = c.fetchone()[0]

  conn.commit()
  conn.close()

  return flights_count


#   Define list_pilots function
def list_pilots():
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  c.execute("SELECT * FROM Pilot")
  #   Fetches all the rows of a query result. Returns all the rows as a list of tuples. An empty list is returned if there is no record to fetch
  pilot_info = c.fetchall()

  #   If list of tuples returned, print the results align to the left with the width specified (default 15)
  if pilot_info:
    print("Pilot ID".ljust(15) + "|" + "Name".ljust(15) + "|" +
          "License_number".ljust(15) + "|" + "Phone_number".ljust(15))
    for row in pilot_info:
      pilot_id, name, license_number, phone_number = row
      print(f"{pilot_id}".ljust(15) + "|" + f"{name}".ljust(15) + "|" +
            f"{license_number}".ljust(15) + "|" + f"{phone_number}".ljust(15))
    return pilot_info
  else:
    print("No pilots found.")
    return None

  c.close()
  conn.close()


#   Define list_aicrafts function
def list_aircrafts():
  conn = sqlite3.connect('flights.db')
  c = conn.cursor()

  c.execute("SELECT * FROM Aircraft")
  #   Fetches all the rows of a query result. Returns all the rows as a list of tuples. An empty list is returned if there is no record to fetch
  aircraft_info = c.fetchall()

  #   If list of tuples returned, print the results align to the left with the width specified (default 15)
  if aircraft_info:
    print("Aircraft ID".ljust(15) + "|" + "Type".ljust(15) + "|" +
          "Model".ljust(15) + "|" + "Capacity".ljust(15))
    for row in aircraft_info:
      aircraft_id, type, model, capacity = row
      print(f"{aircraft_id}".ljust(15) + "|" + f"{type}".ljust(15) + "|" +
            f"{model}".ljust(15) + "|" + f"{capacity}".ljust(15))
    return aircraft_info
  else:
    print("No aircrafts found.")
    return None

  c.close()
  conn.close()


#   Define clear function where first command moves the cursor to the top left corner of the screen
#   Second command clears the screen from the cursor to the end of the screen.
#   Optional parameter end="" avoids printing newline character after executing these commands, so >>> stays in the topmost row.
def clear():
  print("\033[H\033[J", end="")


#   Define what_next function with while loop in order to continue asking user until correct input is given
def what_next():
  while True:
    response = input("Do you want to do anything else? (yes/no) ")
    if response.lower() == "yes":
      clear()
      break
    elif response.lower() == "no":
      print("Exiting program")
      exit()
    else:
      print("Invalid response. Please enter 'yes' or 'no'")


#   Define logo function that prints out a logo of the Airline Database Management System on each page
def logo():
  print("  █████╗    ██████╗    ███╗   ███╗   ███████╗   ")
  print(" ██╔══██╗   ██╔══██╗   ████╗ ████║   ██╔════╝   ")
  print(" ███████║   ██║  ██║   ██╔████╔██║   ███████╗   ")
  print(" ██╔══██║   ██║  ██║   ██║╚██╔╝██║   ╚════██║   ")
  print(" ██║  ██║██╗██████╔╝██╗██║ ╚═╝ ██║██╗███████║██╗")
  print(" ╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝╚═╝     ╚═╝╚═╝╚══════╝╚═╝")
  print("\tAirline Database Management System\n")


#   Define main function
def main():
  conn = sqlite3.connect('flights.db')
  create_tables()


#   A while loop responsible for displaying the main menu
while True:
  logo()
  print("1. Flights Operations")
  print("2. Pilots Operations")
  print("3. Aircrafts Operations")
  print("4. Exit")

  choice = int(input("Enter your choice: "))

  #   1st option in main menu (1. Flights Operations) in default
  if choice == 1:
    clear()
    logo()
    print("Choose the operation: ")
    print("1. Add a Flight")
    print("2. Delete a Flight")
    print("3. Update a Flight")
    print("4. Search for a Flight")
    print("5. View All Flights")
    print("6. Summarize Flights")
    print("7. <-- Go Back to the Main Menu")

    second_choice = int(input("Enter your choice: "))

    ##   1st sub-menu (1. Add a Flight) in default
    if second_choice == 1:
      clear()
      logo()
      flight_id = int(input("Enter the Flight's ID: "))
      origin = input("Enter the origin: ")
      destination = input("Enter the destination: ")
      date = input("Enter the date in format (yyyy-mm-dd): ")
      aircraft_id = int(input("Enter the Aircraft's ID: "))
      pilot_id = int(input("Enter the Pilot's ID: "))
      add_flight(flight_id, origin, destination, date, aircraft_id, pilot_id)
      #print("Flight added successfully!")
      what_next()

##   2nd sub-menu (2. Delete a Flight) in default
    elif second_choice == 2:
      flight_id = int(input("Enter the Flight's ID: "))
      delete_flight(flight_id)
      what_next()

##   3rd sub-menu (3. Update a Flight) in default
    elif second_choice == 3:
      clear()
      logo()
      flight_id = int(input("Enter the Flight's ID: "))
      origin = input("Enter the origin: ")
      destination = input("Enter the destination: ")
      date = input("Enter the date in format (yyyy-mm-dd): ")
      aircraft_id = int(input("Enter the Aircraft's ID: "))
      pilot_id = int(input("Enter the Pilot's ID: "))
      update_flight(flight_id, origin, destination, date, aircraft_id,
                    pilot_id)
      print("Flight updated successfully!")
      what_next()

##   4th sub-menu (4. Search for a Flight) in default
    elif second_choice == 4:
      clear()
      logo()
      print("1. Search for a Flight by ID")
      print("2. Search for a Flight by Destination and Date")
      print("3. <-- Go Back to the Main Menu")

      third_choice = int(input("Enter your choice: "))

      ### 1st sub-sub-menu (1. Search for a Flight by ID) in default
      if third_choice == 1:
        flight_id = int(input("Enter the flight ID: "))
        flight_info = search_flight(flight_id)
        #print(flight_info)
        what_next()

### 2nd sub-sub-menu (2. Search for a Flight by Destination and Date) in default
      elif third_choice == 2:
        destination = input("Enter the destination: ")
        date = input("Enter the date in format (yyyy-mm-dd): ")
        flight_info = search_flight_by_destination_and_date(destination, date)
        #print(flight_info)
        what_next()

### 3rd sub-sub-menu (3. <-- Go Back to the Main Menu) in default
      elif third_choice == 3:
        clear()
        continue
### Break if any other choice has been made
      elif third_choice == 4:
        break

##  5th sub-menu (5. View All Flights) in default
    elif second_choice == 5:
      clear()
      logo()
      flight_info = view_flights()
      #print(flight_info)
      what_next()

##  6th sub-menu (6. Summarize Flights) in default
    elif second_choice == 6:
      clear()
      logo()
      print("1. Summarize Flights by Specific Week")
      print("2. Summarize Flights by Specific Month")
      print("3. Summarize Flights by Destination")
      print("4. <-- Go Back to the Main Menu")

      third_choice = int(input("Enter your choice: "))

      ### 1st sub-sub-menu (1. Summarize Flights by Specific Week) in default
      if third_choice == 1:
        week = input("Enter the week in format (ww): ")
        flights_count = flights_per_week(week)
        print("Number of flights in week {}: {}".format(week, flights_count))
        what_next()

### 2nd sub-sub-menu (2. Summarize Flights by Specific Month) in default
      elif third_choice == 2:
        month = input("Enter the month in format (mm): ")
        flights_count = flights_per_month(month)
        print("Number of flights in month {}: {}".format(month, flights_count))
        what_next()

### 3rd sub-sub-menu (3. Summarize Flights by Destination) in default
      elif third_choice == 3:
        destination = input("Enter the destination: ")
        flights_count = flights_per_destination(destination)
        print("Number of flights to {}: {}".format(destination, flights_count))
        what_next()

### 4th sub-sub-menu (4. <-- Go Back to the Main Menu) in default
      elif third_choice == 4:
        clear()
        continue

### Break if any other choice given
      elif third_choice == 5:
        break

##  7th sub-menu (7. <-- Go Back to the Main Menu)
    elif second_choice == 7:
      clear()
      continue

##  Break if any other choice given
    elif second_choice == 8:
      break

#   2nd option in main menu (2. Pilots Operations) in default
  elif choice == 2:
    clear()
    logo()
    print("Choose the operation: ")
    print("1. Add a Pilot")
    print("2. Delete a Pilot")
    print("3. Update Pilot's Data")
    print("4. View All the Pilots")
    print("5. <-- Go Back to the Main Menu")

    second_choice = int(input("Enter your choice: "))

    ##  1st sub-menu (1. Add a Pilot) in default
    if second_choice == 1:
      clear()
      logo()
      pilot_id = int(input("Enter the Pilot's ID: "))
      name = input("Enter the Pilot's Name: ")
      license_number = int(input("Enter the Pilot's License Number: "))
      phone_number = int(input("Enter the Pilot's Phone Number: "))
      add_pilot(pilot_id, name, license_number, phone_number)
      what_next()

##  2nd sub-menu (2. Delete a Pilot) in default
    elif second_choice == 2:
      clear()
      logo()
      pilot_id = int(input("Enter the Pilot's ID: "))
      delete_pilot(pilot_id)
      what_next()

##  3rd sub-menu (3. Update Pilot's Data) in default
    elif second_choice == 3:
      clear()
      logo()
      pilot_id = int(input("Enter the Pilot's ID: "))
      name = input("Enter the Name of the Pilot: ")
      license_number = int(input("Enter the License Number of the Pilot: "))
      phone_number = int(input("Enter the Phone Number of the Pilot "))
      update_pilot(pilot_id, name, license_number, phone_number)
      print("Pilot's profile updated successfully!")
      what_next()

##  4th sub-menu (4. View All the Pilots) in default
    elif second_choice == 4:
      clear()
      logo()
      pilot_info = list_pilots()
      what_next()

##  5th sub-menu (5. <-- Go Back to the Main Menu) in default
    elif second_choice == 5:
      clear()
      continue

    elif second_choice == 6:
      break

#   3rd option in main menu (3. Aircrafts Operations) in default
  elif choice == 3:
    clear()
    logo()
    print("1. Add Aircraft")
    print("2. Delete Aircraft")
    print("3. Update Aircraft")
    print("4. View All the Aircrafts")
    print("5. <-- Go Back to the Main Menu")

    second_choice = int(input("Enter your choice: "))

    ##  1st sub-menu (1. Add Aircraft) in default
    if second_choice == 1:
      aircraft_id = int(input("Enter the Aircraft's ID: "))
      type = input("Enter the Type of the Aircraft: ")
      model = input("Enter the Aircraft's Model: ")
      capacity = int(input("Enter the Capacity of the Aircraft: "))
      add_aircraft(aircraft_id, type, model, capacity)
      what_next()

## 2nd sub-menu (2. Delete Aircraft) in default
    elif second_choice == 2:
      aircraft_id = int(input("Enter the Aircraft's ID: "))
      delete_aircraft(aircraft_id)
      what_next()

##  3rd sub-menu (3. Update Aircraft) in default
    elif second_choice == 3:
      clear()
      logo()
      aircraft_id = int(input("Enter the Aircraft's ID: "))
      type = input("Enter the Type of the Aircraft: ")
      model = input("Enter the Model of the Aircraft: ")
      capacity = int(input("Enter the capacity of the Aircraft: "))
      update_aircraft(aircraft_id, type, model, capacity)
      print("Aircraft's information updated successfully!")
      what_next()

## 4th sub-menu (4. View All the Aircrafts) in default
    elif second_choice == 4:
      clear()
      logo()
      aircraft_info = list_aircrafts()
      what_next()

## 5th sub-menu (5. <-- Go Back to the Main Menu) in default
    elif second_choice == 5:
      clear()
      continue

##  Break in case of any other choice given
    elif second_choice == 6:
      break

#   4th option in the main menu (4. Exit) in default
  elif choice == 4:
    print("Exiting program")
    break

