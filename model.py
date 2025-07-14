import sqlite3
import utils_json
from sqlite3 import Error

# TODO NOTE: You need to rewrite by yourself all code base 


def create_connection(db_file):
    """Create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite version {sqlite3.version}")
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    
    return conn

def create_tables(conn):
    """Create the users and addresses table DDL"""
    try:
        cursor = conn.cursor()
                    
        # Create users table 
        # TODO: Read about table constraints, SQLite data types, their differences from PostgreSQL, and add to the README.
        users_table = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        """
        
        # Create addresses table - ON DELETE CASCADE AND ON UPDATE NO ACTION = constraints 
        addresses_table = """
            CREATE TABLE IF NOT EXISTS addresses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                street TEXT NOT NULL,
                number TEXT NOT NULL,
                zip_code TEXT NOT NULL,
                latitude TEXT,
                longitude TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id)
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION
            );
        """
        
        # Execute the SQL commands
        cursor.execute(users_table)
        cursor.execute(addresses_table)
        
        conn.commit() # Save the operation 
        print("Tables created successfully")
    except Error as e:
        print(f"Error creating tables: {e}")

def insert_user(conn, user):
    """Insert a new user into the users table"""
    
    # DML to insert a user to the user table
    sql = """
        INSERT INTO users(first_name, last_name, email)
        VALUES(?, ?, ?)
    """
    try:
        cursor = conn.cursor() # to open the connection with database 
        cursor.execute(sql, user) # to execute the operation
        conn.commit() # to save the operation
        return cursor.lastrowid # the return of the operation
    except Error as e:
        print(f"Error inserting user: {e}")
        return None

def insert_address(conn, address):
    """Insert a new address into the addresses table"""
    sql = """
        INSERT INTO addresses(user_id, street, number, zip_code, latitude, longitude)
        VALUES(?, ?, ?, ?, ?, ?)
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, address)
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error inserting address: {e}")
        return None

def get_user_with_addresses(conn, user_id):
    """Get a user and their addresses"""
    try:
        cursor = conn.cursor()
        
        # Get user information
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone() # fetchone get just one row from a table
        
        if user is None:
            return None
        
        # Get user's addresses
        cursor.execute("SELECT * FROM addresses WHERE user_id = ?", (user_id,))
        addresses = cursor.fetchall() # fetchall get all rows from a table
        
        # Format the result in a dict 
        user_data = {
            "id": user[0],
            "first_name": user[1],
            "last_name": user[2],
            "email": user[3],
            "addresses": [] # list of one or more than one address
        }
        
        for addr in addresses:
            address_data = {
                "id": addr[0],
                "street": addr[2],
                "number": addr[3],
                "zip_code": addr[4],
                "latitude": addr[5],
                "longitude": addr[6]
            }
            user_data["addresses"].append(address_data)
        
        return user_data
    except Error as e:
        print(f"Error retrieving user data: {e}")
        return None

def main():
    """
      To execute all operations 
    """
    # TODO - James change the data base name and remove this commment
    database = "james_usuarios_db.sqlite"
    
    # Create a database connection
    conn = create_connection(database)
    
    if conn is not None:
        # Create tables
        create_tables(conn)
        
        # Insert users 
        # TODO - James Add more two users 
        user1 = ("Jack", "Chan", "jack.chan@example.com")
        user2=("james","tzung cheng guo","jamestzungcheng11@gmail.com")
        user3=("priscila","piazza","piazzapriscila@gmail.com")

        user1_id = insert_user(conn, user1)
        user2_id=insert_user(conn,user2)
        user3_id=insert_user(conn,user3)

        print(f"Inserted user with ID: {user1_id} ,{user2_id},{user3_id}")
       
        
        # Insert addresses
        # TODO James add addresses for the users you created with Curitiba and CDE 
        address1 = (user1_id, "Main Street", "123", "10001", 40.7128, -74.0060)  # New York
        address2 = (user1_id, "Broadway", "456", "10002", 40.7580, -73.9855)     # Another NY address
        address3= (user2_id,"Rua das flores","789","80020-060",-25.4284,-49.2733)
        address4=(user3_id,"Avenida San Blas","321","7000",-25.5162,-54.6114)
        addr1_id = insert_address(conn, address1)
        addr2_id = insert_address(conn, address2)
        addr3_id=insert_address(conn,address3)
        addr4_id=insert_address(conn,address4)
        print(f"Inserted addresses with IDs: {addr1_id}, {addr2_id} ,{addr3_id},{addr4_id}")
        
       
        # Retrieve and display user data with addresses
        # TODO create a function to save the result in a json file. 

        user_data = get_user_with_addresses(conn, user1_id)
        if user_data:
            print("\nUser Information:")
            print(f"Name: {user_data['first_name']} {user_data['last_name']}")
            print(f"Email: {user_data['email']}")
            print("\nAddresses:")
            for addr in user_data['addresses']:
                print(f"  {addr['street']} {addr['number']}, ZIP: {addr['zip_code']}")
                print(f"  Coordinates: ({addr['latitude']}, {addr['longitude']})")
        
        # Close the connection
        conn.close()
        print("\nDatabase connection closed")

if __name__ == '__main__':
    main()

