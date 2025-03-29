#Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
#Требования:
#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
#2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
#3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы)

class User:
    def __init__(self, user_id: int, name: str):
        self.__user_id = user_id  # Приватный атрибут ID
        self.__name = name  # Приватный атрибут имени
        self.__access_level = "user"  # Приватный уровень доступа
    # Методы доступа к атрибутам
    def get_user_id(self) -> int:
        return self.__user_id

    def get_name(self) -> str:
        return self.__name

    def get_access_level(self) -> str:
        return self.__access_level

    def set_name(self, new_name: str):
        if isinstance(new_name, str) and len(new_name) > 0:
            self.__name = new_name
        else:
            raise ValueError("Некорректное имя пользователя")

    def __str__(self):
        return f"User(ID: {self.__user_id}, Name: {self.__name}, Access: {self.__access_level})"


class Admin(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        self.__access_level = "admin"  # Переопределение уровня доступа
        self.__users_list = []  # Приватный список пользователей

    # Методы для работы с пользователями
    def get_users_list(self) -> list:
        return self.__users_list.copy()  # Возвращаем копию списка

    def add_user(self, user: User) -> bool:
        if not isinstance(user, User):
            print("Ошибка: можно добавлять только объекты User")
            return False

        # Проверка уникальности ID
        if any(u.get_user_id() == user.get_user_id() for u in self.__users_list):
            print(f"Ошибка: ID {user.get_user_id()} уже существует")
            return False

        self.__users_list.append(user)
        print(f"Добавлен: {user.get_name()}")
        return True

    def remove_user(self, user_id: int) -> bool:
        for i, user in enumerate(self.__users_list):
            if user.get_user_id() == user_id:
                removed_user = self.__users_list.pop(i)
                print(f"Удален: {removed_user.get_name()}")
                return True
        print(f"Ошибка: пользователь с ID {user_id} не найден")
        return False

    # Переопределение метода доступа к уровню
    def get_access_level(self) -> str:
        return self.__access_level

    def list_users(self):
        print("\nТекущие пользователи:")
        for user in self.__users_list:
            print(f"ID: {user.get_user_id()}, Name: {user.get_name()}")
        print()


# Пример использования
if __name__ == "__main__":
    # Создаем администратора
    admin = Admin(1, "Администратор Системы")

    # Создаем обычных пользователей
    user1 = User(2, "Иван Рабочий")
    user2 = User(3, "Мария Бухгалтер")

    # Добавляем пользователей
    admin.add_user(user1)
    admin.add_user(user2)

    # Пытаемся добавить дубликат
    admin.add_user(User(2, "Дубликат"))  # Должна быть ошибка

    # Выводим список
    admin.list_users()

    # Изменяем имя пользователя
    try:
        user1.set_name("Иван Обновленный")
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Удаляем пользователя
    admin.remove_user(2)
    admin.remove_user(999)  # Несуществующий

    # Проверяем список после удаления
    admin.list_users()

    # Проверка инкапсуляции
    try:
        print(user1.__access_level)  # Вызовет ошибку
    except AttributeError as e:
        print(f"\nЗащита данных: {e}")