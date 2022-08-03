import random
import string

from aiogram.dispatcher.filters import Filter
from aiogram.types import InlineKeyboardButton, KeyboardButton, Message
from aiogram.utils.callback_data import CallbackData


class KeyboardButtonClickedFilter(Filter):
    key = "keyboardButtonClicked"
    text: str

    def __init__(self, button: KeyboardButton):
        self.text = button.text

    async def check(self, message: Message) -> bool:
        return self.text == message.text


class NavInlineButton(InlineKeyboardButton):
    """Only for syntax sugar purposes. Has its own filter that returns CallbackDataFilter"""

    def __init__(self, text: str = None, url: str = None):
        super().__init__(text=text, url=url)
        self.callback_data = "".join(
            [random.choice(string.digits + string.ascii_letters) for i in range(0, 8)])

    def filter(self):
        return CallbackData(self.callback_data).filter()


class NavKeyboardButton(KeyboardButton):
    """Only for syntax sugar purposes. Has its own filter that returns aiogram dispatcher's filter """

    def filter(self):
        return KeyboardButtonClickedFilter(button=self)
