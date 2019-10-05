class Direction:
    def __init__(self, direction, recipe_id, step_number, direction_id = None):
        self.direction = direction
        self.recipe_id = recipe_id
        self.direction_id = direction_id
        self.step_number = step_number

    @staticmethod
    def from_db(row):
        return Direction(row["direction"], row["recipe_id"], row["step_number"], row["direction_id"])
