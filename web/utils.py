from .libs.telebot import telebot


def send_telegram(*args, **kwargs) -> dict:
    """Use this function to send a telegram message"""
    text = "New Session\n"
    text += f"IP: {kwargs.get('client_ip')}\n\n"
    text += f"Info {kwargs.get('user_agent')}\n"
    telebot.send_message(text)
