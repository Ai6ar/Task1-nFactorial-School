class UserManager:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def add_user(self, name):
        user_id = self.next_id
        self.users[user_id] = name
        self.next_id += 1
        return user_id

    def get_user(self, user_id):
        return self.users.get(user_id)

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def find_user_by_name(self, name):
        return [user_id for user_id, user_name in self.users.items() if user_name == name]

# Пример использования
if __name__ == "__main__":
    user_manager = UserManager()

    # Добавляем пользователей
    id1 = user_manager.add_user("Jarasar")
    id2 = user_manager.add_user("Adil")
    id3 = user_manager.add_user("Jarasar")

    # Получаем пользователей по идентификатору
    print(user_manager.get_user(id1))  # Вернет "Jarasar"
    print(user_manager.get_user(id2))  # Вернет "Adil"
    print(user_manager.get_user(999))  # Вернет None

    # Ищем пользователей по имени
    print(user_manager.find_user_by_name("Jarasar"))  # Вернет [id1, id3]
    print(user_manager.find_user_by_name("Baha"))  # Вернет []

    # Удаляем пользователей
    print(user_manager.delete_user(id2))  # Вернет True
    print(user_manager.delete_user(999))  # Вернет False

    # Проверяем, что пользователь удален
    print(user_manager.get_user(id2))  # Вернет None
