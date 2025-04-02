from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class DAO():

    @staticmethod
    def getCodins():
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select c.codins
                        from corso c"""
            cursor.execute(query)

            for row in cursor:
                res.append(row["codins"])

            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * from corso"""
            cursor.execute(query)
            for row in cursor:
                #res.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
                res.append(Corso(**row)) #modo più veloce per prendere tutti i campi del dizionario

            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def getCorsiPD(pd):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * from corso c where c.pd=%s"""

            cursor.execute(query, (pd, ))

            for row in cursor:
                res.append(Corso(**row))

            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def getCorsiPDwithIscritti(pd):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select c.codins, c.crediti, c.nome, c.pd, count(*) as n
                        from corso c, iscrizione i
                        where c.codins=i.codins and c.pd=%s
                        group by c.codins, c.crediti, c.nome, c.pd"""

            cursor.execute(query, (pd,))

            for row in cursor:
                res.append((Corso(row["codins"], row["crediti"], row["nome"], row["pd"]), row["n"])) #restituisco una tupla dove il primo elemento è il corso mentre il secondo elemento è il contatore

            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def getStudentiCorso(codins):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select s.*
                        from studente s, iscrizione i
                        where s.matricola=i.matricola and i.codins=%s"""

            cursor.execute(query, (codins,))

            for row in cursor:
                res.append(Studente(**row))

            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def getCDSofCorso(codins):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select s.CDS, count(*) as n
                        from studente s, iscrizione i
                        where s.matricola = i.matricola and i.codins=%s and s.CDS != ""
                        group by s.CDS"""

            cursor.execute(query, (codins,))

            for row in cursor:
                res.append((row["CDS"], row["n"]))

            cursor.close()
            cnx.close()
            return res


if __name__ == "__main__":
    print(DAO.getCodins())
    for c in DAO.getAllCorsi():
        print(c)
    for c in DAO.getCorsiPDwithIscritti(1):
        print(c)
