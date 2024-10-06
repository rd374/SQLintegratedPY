import mysql.connector
from mysql.connector import Error
import importlib
import dbhelper 
class DB:
    def __init__(self):
        try:
            # Establishing the connection to the MySQL server
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                port='3306',
                password='12345',  # Your MySQL password
                auth_plugin='mysql_native_password',
                database='flightsx',
                connection_timeout=600
            )

            if self.conn.is_connected():
                self.mycursor = self.conn.cursor()
                print('Connection established')

                # SQL command to create a database
                # self.mycursor.execute("CREATE DATABASE flightsx")
                # print("Database 'flightsx' created successfully")

                # Optional: Use the new database
                self.mycursor.execute("USE flightsx")
                print("Switched to the 'flightsx' database")

        except Error as e:
            print(f"Error: {e}")

    def fetch_city_names(self):
        city = []
        self.mycursor.execute("""
            SELECT DISTINCT(Destination) FROM flightsx.flights
            UNION
            SELECT DISTINCT(Source) FROM flightsx.flights
        """)

        data = self.mycursor.fetchall()
        

        for item in data:
            city.append(item[0])

        return city
    def fetch_all_flights(self,source,destination):
        self.mycursor.execute("""
                              SELECT Airline,Route,Dep_time,Duration,Price FROM FLIGHTSX.FLIGHTS
                              WHERE SOURCE='{}' and Destination='{}'
                              """.format(source,destination))
        data= self.mycursor.fetchall()
        return data
    def fetch_airline_frequency(self):
        
        airline=[]
        frequency=[]
        
        self.mycursor.execute("""
                             select Airline,count(*) from flights
                             group by airline
                             """)
        data= self.mycursor.fetchall()
        
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
            
        return airline, frequency
    def busy_airport(self):

        city = []
        frequency = []

        self.mycursor.execute("""
        SELECT Source,COUNT(*) FROM (SELECT Source FROM flights
							UNION ALL
							SELECT Destination FROM flights) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency

    def daily_frequency(self):

        date = []
        frequency = []

        self.mycursor.execute("""
        SELECT Date_of_Journey,COUNT(*) FROM flights
        GROUP BY Date_of_Journey
        """)

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency

        

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
   
        
        




   
   

