import json
from lib.gson import json_util


def dumps(itens):
    return json.dumps(itens, default=json_util.default)
