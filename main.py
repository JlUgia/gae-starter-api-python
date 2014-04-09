#!/usr/bin/env python

# Google's AppEngine modules:
import webapp2
from webapp2 import Route
from webapp2_extras import routes
from webapp2_extras.routes import DomainRoute

# Controllers and handlers
from controllers.attendees import *

# Requested URLs that are not listed here,
# will return 404

ROUTES = [
    DomainRoute('<:(moscow-2014\.appspot\.com|localhost)>', [ # Allowed domains

        # Attendees
        Route(r'/users', handler=AttendeesController, name='attendees')
    ])
]

app = webapp2.WSGIApplication(ROUTES, debug=False)