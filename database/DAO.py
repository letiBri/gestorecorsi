from database.DB_connect import DBConnect
from model.corso import Corso


class DAO():

    @staticmethod
    def getCodins():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select c.codins
                    from corso c"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["codins"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from corso"""
        cursor.execute(query)

        res = []
        for row in cursor:
            #res.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
            res.append(Corso(**row)) #modo più veloce per prendere tutti i campi del dizionario

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiPD(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from corso c where c.pd=%s"""

        cursor.execute(query, (pd, ))

        res = []
        for row in cursor:
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res


if __name__ == "__main__":
    print(DAO.getCodins())
    for c in DAO.getAllCorsi():
        print(c)
