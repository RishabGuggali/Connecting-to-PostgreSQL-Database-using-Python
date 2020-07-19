import psycopg2

#connect to the db--------------------------------------------------------------------------------
con = psycopg2.connect(
            #host = " ",
            database="your_database_name",
            user = "your_database_username",
            password = "your_database_password")

#cursor-------------------------------------------------------------------------------------------
cur = con.cursor()



#execute query
#Insert query------------------------------------------------------------------------------------------

cur.execute("insert into Tabelname values('','') ")             #Enter the table name and pass the values you need to Insert into Database

#Delete query------------------------------------------------------------------------------------------

cur.execute("delete from Tablename where condition ")           #Enter the table name and condition to delete 

#Select query------------------------------------------------------------------------------------------------

cur.execute("select * from Tablename")                          #Enter the table name which you want to retrieve

#------------------------------------------------------------------------------------------------------------
rows = cur.fetchall()

for r in rows:
    print(r[0]+"  "+r[1])                                  #Iterate and print the retrieved data 

#commit the transcation---------------------------------------------------------------------------------------
con.commit()

#close the cursor---------------------------------------------------------------------------------------------
cur.close()

#close the connection-----------------------------------------------------------------------------------------
con.close()
