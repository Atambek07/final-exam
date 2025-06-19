# Практическая задача 1

### Темы: Классы, наследование, интерфейсы, принцип единой ответственности (SRP)  
### Уровень: Легкий

#### Реализуй систему уведомлений с базовым классом Notifier и двумя реализациями:
- EmailNotifier → отправляет письма
- TelegramNotifier → отправляет сообщения в Telegram

** Создай функцию send_notifications(users, message), которая рассылает сообщение всем пользователям. У каждого пользователя есть поле preferred_notifier.

``` python
class User:
    def __init__(self, name, notifier):
        self.name = name
        self.notifier = notifier

users = [
    User("Alice", EmailNotifier("alice@mail.com")),
    User("Bob", TelegramNotifier("@bob123"))
]

send_notifications(users, "Добро пожаловать!")
```
