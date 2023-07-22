import pandas as pd
from sqlalchemy import create_engine

# Sample Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Occupation': ['Engineer', 'Doctor', 'Teacher']
}
df = pd.DataFrame(data)

# SQLite database file path
database_path = 'example.db'

# Function to write DataFrame to SQLite database
def write_dataframe_to_sqlite(df, table_name, database_path):
    # Create a SQLAlchemy engine to connect to the database
    engine = create_engine(f'sqlite:///{database_path}')

    # Write DataFrame to the database table
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Function to read DataFrame from SQLite database
def read_dataframe_from_sqlite(table_name, database_path):
    # Create a SQLAlchemy engine to connect to the database
    engine = create_engine(f'sqlite:///{database_path}')

    # Read data from the database table into a DataFrame
    query = f'SELECT * FROM {table_name}'
    df = pd.read_sql(query, con=engine)

    return df

if __name__ == '__main__':
    # Define the table name in the SQLite database
    table_name = 'employees'

    # Write DataFrame to SQLite database
    write_dataframe_to_sqlite(df, table_name, database_path)

    # Read DataFrame from SQLite database
    df_from_db = read_dataframe_from_sqlite(table_name, database_path)

    print("Original DataFrame:")
    print(df)
    print("\nDataFrame from SQLite:")
    print(df_from_db)
