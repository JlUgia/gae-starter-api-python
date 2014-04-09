#!/usr/bin/env python

from google.appengine.ext import db

# These classes define the data objects
# that you will be able to store in
# AppEngine's data store.

class Attendee(db.Model):
  name = db.StringProperty()
  email = db.StringProperty(required=True)
  created_at = db.DateTimeProperty(auto_now_add=True)

  def to_dict(self):
    return {'id':str(self.key().id()), 'name':self.name, 'email':self.email, 'created_at':self.created_at}

  def __hash__(self):
    return self.key().id()

  def __eq__(self, other):
    return self.key().id() == other.key().id()