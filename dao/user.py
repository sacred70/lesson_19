from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_user_id(self, uid):
        return self.session.query(User).get(uid)

    def get_user_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def create(self, user_data):
        user = User(**user_data)
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user_data):
        user = self.get_user_id(user_data.get("id"))
        user.username = user_data.get("username")
        user.password = user_data.get("password")
        user.role = user_data.get("role")

        self.session.add(user)
        self.session.commit()

    def delete(self, uid):
        user = self.get_user_id(uid)
        self.session.delete(uid)
        self.session.commit()

