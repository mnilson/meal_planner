from repository_sqlite import Repository


class DirectionRepository(Repository):
    def __init__(self, name: str):
        super(DirectionRepository, self).__init__(name)
        self.__create_db__()

    def clear_tables(self):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('DELETE FROM direction;')

        conn.commit()
        conn.close()

    def drop_db(self):
        super(DirectionRepository, self).drop_db()
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('DROP TABLE IF EXISTS direction;')

        conn.commit()
        c.close()

    def save_direction(self, direction_id, recipe_id, direction, step_number):
        conn = self.__conn__()
        c = conn.cursor()
        if direction_id is None:
            query = f"INSERT INTO direction (recipe_id, direction, step_number) VALUES({recipe_id}, '{direction}', {step_number}) "
            direction_id = c.execute(query).lastrowid
        else:
            c.execute(
                f"UPDATE direction "
                f" SET "
                f"  recipe_id = {recipe_id}, "
                f"  direction = '{direction}', "
                f"  step_number = {step_number} "
                f" WHERE direction_id = {direction_id}")
        conn.commit()
        conn.close()
        return direction_id

    def retrieve_directions(self):
        conn = self.__conn__()
        c = conn.cursor()
        return c.execute("SELECT * FROM direction;")

    def retrieve_direction_by_name(self, name):
        conn = self.__conn__()
        c = conn.cursor()
        return c.execute("SELECT * FROM direction where recipe_id = ? order by step_number;", [name]).fetchone()

    def __conn__(self):
        return super(DirectionRepository, self).__conn__()

    def __create_db__(self):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS direction (direction_id integer PRIMARY KEY, recipe_id, direction, step_number);')
        conn.commit()
        conn.close()
