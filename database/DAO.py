from database.DB_connect import DBConnect


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
        cnx.xlose()
        return res


if __name__ == '__main__':
    print(DAO.getCodins())
