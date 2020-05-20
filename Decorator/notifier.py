from abc import ABC, abstractmethod
from argparse import ArgumentParser
import BAT
def get_args():
    parser = ArgumentParser()
    parser.add_argument("--sms", type=bool, nargs='?', const=True, default=False)
    parser.add_argument("--email", type=bool, nargs='?', const=True, default=False)
    parser.add_argument("--batman", type=bool, nargs='?', const=True, default=False)
    return parser.parse_args()

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
        return f"""{BAT.bat}
    `                     ` \n\t {self._notifier.send()}"""


if __name__ == "__main__":
    cmd_args = get_args()


    print('\n')
    simple = ConcreteNotifier()
    print("our undecorated notify will do...")
    print(simple.send())

    print('\n\n')
    #DECORATORS
    """
    We 
    """

    stack: Notifier = simple
    if cmd_args.sms:
        stack = SMSAlertDecorator(stack, "347.767.0101")
    
    if cmd_args.email:
        stack = EMailAlertDecorator(stack, "denis@rcanalytics.com")

    if cmd_args.batman:
        stack = BatSignalAlertDecorator(stack)

    print("WITH FEATURE FLAGS... the decorated notifier will notify...\n")
    print(stack.send())