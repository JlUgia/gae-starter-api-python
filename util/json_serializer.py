import json
import datetime
from time import strftime
from time import mktime
from google.appengine.ext.db import GeoPt

from model.model import *

class JsonSerializer(json.JSONEncoder):

    def default(self, obj):
        
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        elif isinstance(obj, Attendee):
        	return obj.to_dict()

        return json.JSONEncoder.default(self, obj)