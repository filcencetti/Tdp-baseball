from database.DB_connect import DBConnect
from model.team import Team


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getYears():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """
                   select distinct t.year 
                    from teams t
                    where t.year > 1980
                   """
        cursor.execute(query)

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getTeams(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                select distinct * 
                from teams 
                where year = %s
                """
        cursor.execute(query,(year,))

        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getEdges(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                select t1.ID as teamID1, t2.ID as teamID2, sum(s1.salary + s2.salary) as sum_salary
                from teams t1, teams t2, salaries s1, salaries s2, appearances a1, appearances a2
                where t1.ID  = s1.teamID
                and t2.ID = s2.teamID
                and a1.playerID = s1.playerID
                and a2.playerID = s2.playerID
                and a1.teamID = t1.ID
                and a2.teamID = t2.ID
                and t1.year = a1.`year` 
                and a2.year = %s
                and a1.year = a2.`year`
                and t1.year = t2.`year`
                and s1.year = s2.`year`
                and s1.year = a2.year
                group by t1.ID, t2.ID
                """
        cursor.execute(query,(year,))

        for row in cursor:
            result.append((row["teamID1"],row["teamID2"],row["sum_salary"]))

        cursor.close()
        conn.close()
        return result
