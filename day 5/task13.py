class Notification:
    def send(self):
        print("Sending notification...")


class EmailNotification(Notification):
    def send(self):
        print("Email notification sent.")


class SMSNotification(Notification):
    def send(self):
        print("SMS notification sent.")


notifications = [
    Notification(),
    EmailNotification(),
    SMSNotification(),
    EmailNotification(),
    SMSNotification()
]

for notification in notifications:
    notification.send()