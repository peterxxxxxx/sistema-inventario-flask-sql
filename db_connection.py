import pyodbc

def get_db_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=nombre del server\\SQLEXPRESS;' 
            'DATABASE=InventarioDB;'
            'Trusted_Connection=yes;'
        )
        return conn
    except Exception as e:
        print(f"Error conectando a BD: {e}")
        return None