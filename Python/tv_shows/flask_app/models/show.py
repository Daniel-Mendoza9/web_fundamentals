from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, session

DATABASE = "shows"


class Show:

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shows LEFT JOIN users ON users.id = shows.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_shows = []
        for show in results:
            all_shows.append(cls(show))
        return all_shows

    @classmethod
    def save(cls, data):
        query = "INSERT INTO shows (title, network, release_date, description, user_id) VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        show_id = connectToMySQL(DATABASE).query_db(query, data)
        return show_id


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM shows LEFT JOIN users ON users.id = shows.user_id WHERE shows.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        show = Show(result[0])
        return show

    @classmethod
    def update(cls,data):
        query = "UPDATE shows SET title = %(title)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result


    @staticmethod
    def validate_show(show):
        is_valid = True
        # test whether a field matches the pattern
        print('this is it',show)
        if len(show['title']) < 3:
            flash("Title must be at least 3 characters.")
            is_valid = False
        if len(show['network']) < 3:
            flash("Network must be at least 3 characters.")
            is_valid = False
        if len(show['description']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        if show['release_date'] == '':
            flash("Date must not be blank.")
            is_valid = False
        return is_valid