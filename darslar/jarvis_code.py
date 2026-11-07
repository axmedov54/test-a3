import sqlite3

# Define the database filename
DB_FILE = 'example.db'

def create_cars_table():
    """
    Creates the 'cars' table in the SQLite database if it does not exist.
    """
    # SQL command to create the table with appropriate data types and constraints
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique, self-incrementing ID
        make TEXT NOT NULL,                  -- Manufacturer (e.g., Toyota)
        model TEXT NOT NULL,                 -- Specific model (e.g., Corolla)
        year INTEGER NOT NULL,               -- Manufacturing year
        price REAL                           -- Price (float)
    );
    """
    
    try:
        # Connect to the database (creates it if it doesn't exist)
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Execute the create table command
            cursor.execute(create_table_sql)
            # Commit connection is implicit when using 'with' for connection
            print("Table 'cars' created successfully or already exists.")
            
    except sqlite3.Error as e:
        # Print error details if database operation fails
        print(f"Error creating table: {e}")

if __name__ == "__main__":
    # Execute the function to create the table
    create_cars_table()