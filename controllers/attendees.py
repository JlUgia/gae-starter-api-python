#!/usr/bin/env python

import os
import webapp2
import json
import re
import time

from google.appengine.ext import db
from google.appengine.ext.db import TransactionFailedError

from model.model import *

from util.json_serializer import JsonSerializer

class AttendeesController(webapp2.RequestHandler):
            
    def get(self):

        results = []

        # Retrieve attendees
        q = Attendee.all().order('-created_at')

        for attendee in q:
            results.append(attendee)

        self.response.status = 200
        self.outputBody = results
            
        if(self.response.status_int == 200):
            self.response.write(json.dumps(self.outputBody, cls = JsonSerializer, indent=4))


    def post(self):
        
        self.response.status = 422;

        if(self.request.body):

            inputBody = json.loads(self.request.body)
            attendee = Attendee(**inputBody)

            attendee.put()
            self.outputBody = attendee
            self.response.status = 201

        if(self.response.status_int == 201): 
            self.response.write(json.dumps(self.outputBody, cls = JsonSerializer, indent=4))
