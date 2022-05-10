import json
from providers import Provider

#@staticmethod
def import_providers():
    filename = "./provider.json"

    # Open file using utf8
    f = open(filename, "r", encoding="utf-8")

    # read file
    data = f.read()

    # load data as Json
    j = json.loads(data)

    # Create providers list
    providers = []
    for line in j:
        p = Provider(line)
        providers.append(p)

    return providers
