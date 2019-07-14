import json
from django.core.serializers.json import DjangoJSONEncoder

class JsonEncoder():
    def __init__(self):
        pass

    @classmethod
    def dumps(cls, data, encoder_cls=DjangoJSONEncoder):
        encoded = json.dumps(data, cls=encoder_cls)
        return encoded