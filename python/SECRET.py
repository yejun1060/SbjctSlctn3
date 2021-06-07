import json
from django.core.exceptions import ImproperlyConfigured

with open("../secret.json") as f:
    secrets = json.load(f.read())


def get(setting, secrets=secrets):
    try:
        return secrets[setting]
    except BaseException:
        msg = f"set the {setting} variable"
        raise ImproperlyConfigured(msg)


SECRET_KEY = get("SECRET_KEY")
