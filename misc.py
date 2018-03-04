import collections
import json


class PythonObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, collections.Set):
            return dict(_set_object=sorted(list(obj)))
        else:
            return json.JSONEncoder.default(self, obj)

def as_python_object(dct):
    if '_set_object' in dct:
        return set(dct['_set_object'])
    return dct
