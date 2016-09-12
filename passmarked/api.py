from passmarked.core import Core


class API(object):

    def __init__(self, user_config):
        self.api = Core(user_config)

    def websites(self, active=True, limit=50, offset=10):
        options = {'active': active, 'limit': limit, 'offset': offset}
        return self.api.websites(options)

    def website(self, id):
        return self.api.website(id)

    def get(self, key):
        return self.api.report(key)

    def balance(self):
        return self.api.balance()

    def user(self):
        return self.api.user()

    def credits(self, active=True, limit=50, offset=10):
        options = {'active': active, 'limit': limit, 'offset': offset}
        return self.api.credits(options)

    # critical / error / warning / notice
    def create(self, url, bail=True, level='notice', limit=None,
               patterns=[], filters=[]):
        options = {'url': url, 'recursive': True, 'bail': bail, 'level': level,
                   'limit': limit, 'patterns': patterns, 'filters': filters}
        return self.api.create_report(options)

    def submit(self, url):
        return self.api.reports(url)
