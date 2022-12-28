import sqlite3


def tableCreator(dbName, SQL):
    with sqlite3.connect(dbName) as db:
        cursor = db.cursor()
        cursor.execute(SQL)
        db.commit()


dbName = "myDB.db"
createTblPdt = """ CREATE TABLE IF NOT EXISTS tblProduct
                    (ProductID INTEGER, 
                    Name TEXT,
                    Price REAL,
                    PRIMARY KEY(ProductID)
                    )
                """
tableCreator(dbName, createTblPdt)


def insertData(values):
    with sqlite3.connect("myDB.db") as db:
        cursor = db.cursor()
        sql = """INSERT INTO tblProduct(Name,Price) VALUES(?,?)"""
        cursor.execute(sql, values)
        db.commit()


products = ("Espresso2", 1.6)

insertData(products)


def selectProducts():
    with sqlite3.connect("myDB.db") as db:
        cursor = db.cursor()
        cursor.execute("""SELECT * FROM tblProduct""")
        products = cursor.fetchall()
        return products


print(selectProducts())


def selectProduct(id):
    with sqlite3.connect("myDB.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT Name, Price FROM tblProduct WHERE ProductID=?", (id,))
        product = cursor.fetchone()
        return product


print(selectProduct(4))


def updateProduct(data):
    with sqlite3.connect("myDB.db") as db:
        cursor = db.cursor()
        sql = "UPDATE tblProduct SET Name=?, Price =? WHERE PRODUCTID=?"
        cursor.execute(sql, data)
        db.commit()


dataToUpdate = ("Espresso44", 3.6, 4)

updateProduct(dataToUpdate)


def deleteProduct(data):
    with sqlite3.connect("myDB.db") as db:
        cursor = db.cursor()
        sql = "DELETE FROM tblProduct WHERE Name=?"
        cursor.execute(sql, data)
        db.commit()


dataToDelete = ("Espresso44",)

deleteProduct(dataToDelete)
