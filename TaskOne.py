from abc import ABC, abstractmethod


'''Задание: Создать систему оповещений для различных
устройств, которые поддерживают разные интерфейсы.
Условия задачи:
1. Интерфейс IAlert — описывает метод send_alert(message:
str), который используется для отправки уведомлений.
Этот интерфейс должен поддерживаться всеми
устройствами.
2. Устройства для оповещений:
◦ Телефон — поддерживает метод send_sms(text: str),
который отправляет текстовое сообщение.
◦ Электронная почта — поддерживает метод
send_email(subject: str, body: str), где subject — тема
письма, а body — текст письма.
◦ Система громкой связи — поддерживает метод
broadcast(message: str), который озвучивает
сообщение через громкоговоритель.
3. Адаптеры — для каждого устройства (Телефон,
Электронная почта, Система громкой связи) создать
отдельный адаптер, который реализует интерфейс IAlert
и приводит методы этих устройств к единому виду
send_alert.
4. Клиентский код — написать функцию, которая
принимает список устройств с интерфейсом IAlert и
отправляет оповещение всем устройствам через метод
send_alert.'''


class Iphone:
    def send_sms(self, text: str) -> str:
        print(f"Отправлено SMS: {text}")


class Email:
    def send_email(self, subject: str, body: str) -> str:
        print(f"Отправлено письмо: {subject} - {body}")


class HandsFreeCS:
    def broadcast(self, message) -> str:
        print(f"Озвучено сообщение: {message}")


class IAlert(ABC):
    @abstractmethod
    def send_alert(self, message: str):
        pass


class IphoneAdapter(IAlert):
    def __init__(self, iphone: Iphone):
        self.adapter = iphone

    def send_alert(self, message: str):
        self.adapter.send_sms(message)


class EmailAdapter(IAlert):
    def __init__(self, email: Email):
        self.adapter = email

    def send_alert(self, message: str):
        self.adapter.send_email('Оповешание', message)


class HandsFreeCSAdapter(IAlert):
    def __init__(self, adapt: HandsFreeCS):
        self.adapter = adapt

    def send_alert(self, message: str):
        self.adapter.broadcast(message)


# cliend code
def main(devises: list[IAlert], message: str):
    for devise in devises:
        if isinstance(devise, IAlert):
            devise.send_alert(message)
        else:
            raise ValueError('not a specific device has been transferred')


if __name__ == '__main__':
    iphone = Iphone()
    email = Email()
    hand_freeCs = HandsFreeCS()

    iphone_adapter = IphoneAdapter(iphone)
    email_adapter = EmailAdapter(email)
    hand_freeCs_adapter = HandsFreeCSAdapter(hand_freeCs)

# test client code

    devises = [iphone_adapter, email_adapter, hand_freeCs_adapter]
    main(devises, 'Оповещание')










