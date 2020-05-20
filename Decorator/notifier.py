from abc import ABC, abstractmethod

class Notifier(ABC):
    def __init__(self):
        pass
        # self.email_list = email_list

    def send(self) -> None:
        pass

class ConcreteNotifier(Notifier):
    def send(self) -> None:
        return "Default Alert sent to the Default Place"

class BaseAlertDecorator(Notifier):
    _notifier: Notifier = None

    def __init__(self, notifier: Notifier) -> None:
        self._notifier = notifier

    def send(self) -> None:
        return self._notifier.send()

class SMSAlertDecorator(BaseAlertDecorator):
    def __init__(self, notifier: Notifier, phone_number: str):
        super().__init__(notifier)
        self.phone_number = phone_number

    def send(self) -> None:
        return f"SMS -> {self.phone_number} \n\t {self._notifier.send()}"

class EMailAlertDecorator(BaseAlertDecorator):
    def __init__(self, notifier: Notifier, email: str):
        super().__init__(notifier)
        self.email = email

    def send(self) -> None:
        return f"EMAIL -> {self.email} \n\t {self._notifier.send()}"

class BatSignalAlertDecorator(BaseAlertDecorator):
    def send(self) -> None:
        return f"BATMAN HELP! \n\t {self._notifier.send()}"


if __name__ == "__main__":
    print('\n')
    simple = ConcreteNotifier()
    print(simple.send())

    print('\n\n')
    #DECORATORS
    sms_alerter = SMSAlertDecorator(simple, "347.767.0101")
    email_alerter = EMailAlertDecorator(sms_alerter, "denis@rcanalytics.com")
    bat_signal_alerter = BatSignalAlertDecorator(email_alerter)

    print(bat_signal_alerter.send())