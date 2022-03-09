import requests
import json
from config import keys


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException("Одинаковые валюты")

        try:
            quote_ticket = keys[quote]
        except KeyError:
            raise APIException(f"Валюта {quote} не поддерживается")

        try:
            base_ticket = keys[base]
        except KeyError:
            raise APIException(f"Валюта {base} не поддерживается")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"не удалось обработать количество {amount}")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticket}&tsyms={base_ticket}')
        total_base = json.loads(r.content)[keys[base]]*amount

        return total_base