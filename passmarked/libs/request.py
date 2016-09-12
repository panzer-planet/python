import requests
import passmarked.libs.constants


class Request(object):

    def get(self, url, params):
        headers = {'user-agent': passmarked.libs.constants.USER_AGENT}
        return requests.get(url, headers=headers, params=params)

    def post(self, url, data):
        headers = {'user-agent': passmarked.libs.constants.USER_AGENT}
        return requests.post(url, headers=headers, data=data)
