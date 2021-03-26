import base64
import sqlite3
import webbrowser


def DB_connection(db_file):
    """ Create connection to any db """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        connection.row_factory = sqlite3.Row
    except Exception as e:
        print(e)

    return connection


def main_data():
    # Connect to Db and Update value
    connection = DB_connection("week10.db")  
    row = None
    while(row != "q"):
        # Get user input
        row = input("Please enter a row id (1-29): ")
        if row.lower() == "q":
            break
        elif int(row) > 29 or int(row) < 1:
            print("Invalid id! Select a new id between 1 and 29")
        else:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Lab10 WHERE id = ?", (row,))
            # Retrieve first row matching the id provided
            row1 = cursor.fetchone()
            # First decode from base64 then from utf-8 to ascii string
            url = base64.b64decode(row1['Link']).decode()
            # Open the url in a new tab (new = 2)
            webbrowser.open(url, new=2)

            # Request from  user for name of the city and country and Student name update the record
            city = input("Please enter the city name: ")
            country = input("Please enter the country name: ")
            student = input("Please enter your name: ")
            if not city or not country or not student:
                print("You must enter a valid city, country and name")
            else:
                try:
                    sql = '''UPDATE Lab10 SET City = ?, Country = ?, Student = ? WHERE id = ?'''
                    values = (city, country, student, row)
                    cursor.execute(sql, values)
                    connection.commit()
                    print("Row successfully updated!")

                except Exception as e:
                    print("Row updated fail")
                    print(e)


if __name__ == '__main__':
    main_data()