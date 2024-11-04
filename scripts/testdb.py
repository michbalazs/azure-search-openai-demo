import pyodbc

connection_string = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:aidataserver.database.windows.net,1433;Database=aidata;Uid=mich;Pwd=Tea#77!*;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=1000;"
try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    print(cursor.fetchone())
    conn.close()
except pyodbc.Error as ex:
    sqlstate = ex.args[1]
    print(sqlstate)
