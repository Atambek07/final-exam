class Notifier:
    def notify(self,user_name, message):
        raise NotImplementedError("Notifier subclasses must implement the notify method")
    
class EmailNotifier(Notifier):
    def __init__(self, email):
        self.email = email
        
    def notify(self, user_name, message):
        print(f"Sending email to {self.email} for {user_name}: {message}")
        
class TelegramNotifier(Notifier):
    def __init__(self, chat_id):
        self.chat_id = chat_id
        
    def notify(self, user_name, message):
        print(f"Sending Telegram message to {self.chat_id} for {user_name}: {message}")
        
class User:
    def __init__(self, name, preferred_notifier):
        self.name = name
        self.preferred_notifier = preferred_notifier
        
    def send_notification(users, message):
        for user in users:
            user.preferred_notifier.notify(user.name, message)
            
users = [
    User("Alice", EmailNotifier("alice@mail.com")),
    User("Bob", TelegramNotifier("@bob123"))
]

result = User.send_notification(users, "Добро пожаловать!")

