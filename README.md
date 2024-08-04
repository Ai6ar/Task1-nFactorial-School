# Task1-nFactorial-School
# Шаг 1: Инициализация UserManager

class UserManager:
    def __init__(self):
        self.users = {}
        self.next_id = 1

Словарь для хранения данных о пользователях и переменную для отслеживания следующего уникального идентификатора

# Шаг 2: Добавление пользователей

def add_user(self, name):
    user_id = self.next_id
    self.users[user_id] = name
    self.next_id += 1
    return user_id

Этот метод добавляет нового пользователя, присваивает ему уникальный идентификатор и возвращает его.

# Шаг 3: Получение пользователей по идентификатору


def get_user(self, user_id):
    return self.users.get(user_id)

Этот метод получает имя пользователя по его идентификатору. Если идентификатор не найден, он возвращает None.

# Шаг 4: Удаление пользователей

def delete_user(self, user_id):
    if user_id in self.users:
        del self.users[user_id]
        return True
    return False

Этот метод удаляет пользователя по его идентификатору. Возвращает True, если пользователь успешно удален, и False, если идентификатор не найден.

# Шаг 5: Поиск пользователей по имени

def find_user_by_name(self, name):
    return [user_id for user_id, user_name in self.users.items() if user_name == name]

Этот метод находит все идентификаторы пользователей с заданным именем и возвращает их в виде списка.
