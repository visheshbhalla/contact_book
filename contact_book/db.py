from urlparse import urlparse
import pymongo

def includeme(config):
    settings = config.registry.settings

    # Store DB connection in registry
    db_url = urlparse(settings['mongo_uri'])
    conn = pymongo.MongoClient(host=db_url.hostname, port=db_url.port)
    settings['db_conn'] = conn

    # Make DB connection accessible as a request property
    def _get_db(request):
        settings = request.registry.settings
        try:
            db = settings['db_conn'][db_url.path[1:]]
        except pymongo.errors.ConnectionFailure, e:
             print "Could not connect to server: %s" % e
        if db_url.username and db_url.password:
            db.authenticate(db_url.username, db_url.password)
        return db

    config.set_request_property(_get_db, 'db', reify=True)
