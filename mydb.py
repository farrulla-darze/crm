import pymysql

# Establish connection to the MySQL server
connection = pymysql.connect(
    host='localhost',      # Your MySQL host
    user='root',    # Your MySQL username
    password='11235813',  # Your MySQL password
    
)

try:
    # Create a cursor object
    with connection.cursor() as cursor:
        # SQL query to create a new database
        create_db_query = "CREATE DATABASE crm_database"
        
        # Execute the query
        cursor.execute(create_db_query)
        print(f"Database crm_database created successfully.")

finally:
    # Close the connection
    connection.close()
