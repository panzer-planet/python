from passmarked.models.model import Model
from passmarked.models.model_collection import ModelCollection
from passmarked.models.error import Error
from passmarked.libs.process_request import ProcessRequest
import passmarked.libs.config
import passmarked.libs.constants


class Core(object):

    def __init__(self, user_config):
        self.params_data = \
            passmarked.libs.config.get_application_meta(user_config)
        self.api_url = passmarked.libs.constants.API_URL

    def websites(self, options):
        url = self.api_url + '/v2/websites'
        params = self.params_data
        params['limit'] = options['limit']
        params['offset'] = options['offset']
        params['active'] = options['active']

        process = ProcessRequest()
        data = process.get(url, params)

        if isinstance(data, Error):
            return data

        if data['status'] == 'ok':
            return ModelCollection(data)

    def website(self, id):
        url = self.api_url + '/v2/websites/' + str(id)
        params = self.params_data

        process = ProcessRequest()
        data = process.get(url, params)

        if isinstance(data, Error):
            return data

        if data['status'] == 'ok':
            return Model(data)

    def report(self, key):
        url = self.api_url + '/v2/reports/' + str(key)
        params = self.params_data

        process = ProcessRequest()
        data = process.get(url, params)

        if isinstance(data, Error):
            return data

        if data['status'] == 'ok':
            return Model(data)

    def balance(self):
        url = self.api_url + '/v2/balance'
        params = self.params_data

        process = ProcessRequest()
        data = process.get(url, params)

        if isinstance(data, Error):
            return data

        if data['status'] == 'ok':
            return Model(data)

    def user(self):
        url = self.api_url + '/v2/user'
        params = self.params_data

        process = ProcessRequest()
        data = process.get(url, params)

        if isinstance(data, Error):
            return data

        if data['status'] == 'ok':
            return Model(data)

    def credits(self, options):
        url = self.api_url + '/v2/credits'
        params = self.params_data
        params['limit'] = options['limit']
        params['offset'] = options['offset']
        params['active'] = options['active']

        process = ProcessRequest()
        data = process.get(url, params)

        if isinstance(data, Error):
            return data

        if data['status'] == 'ok':
            return ModelCollection(data)

    def create_report(self, options):
        url = self.api_url + '/v2/reports'
        post_data = self.params_data
        post_data['url'] = options['url']
        post_data['recursive'] = options['recursive']
        post_data['bail'] = options['bail']
        post_data['level'] = options['level']
        post_data['limit'] = options['limit']
        post_data['patterns'] = options['patterns']
        post_data['filters'] = options['filters']

        process = ProcessRequest()
        data = process.post(url, post_data)

        if isinstance(data, Error):
            return data

        if data['status'] == 'ok':
            return Model(data)

    def reports(self, website_url):
        url = self.api_url + '/v2/reports/'
        post_data = self.params_data
        post_data['url'] = website_url

        process = ProcessRequest()
        data = process.post(url, post_data)

        if isinstance(data, Error):
            return data

        if data['status'] == 'ok':
            return Model(data)
