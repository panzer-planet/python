from passmarked.models.error import Error
from passmarked.libs.request import Request


class ProcessRequest(object):

    def get(self, url, params):
        request = Request()
        try:
            data = request.get(url, params).json()
        except:
            data = {'code': 'CONNECTION_FAILED',
                    'message': 'The connection failed',
                    'status': 'error'}
            return Error(data)

        if data['status'] == 'error':
            return Error(data)
        else:
            return data

    def post(self, url, post_data):
        request = Request()
        try:
            data = request.post(url, post_data).json()
        except:
            data = {'code': 'CONNECTION_FAILED',
                    'message': 'The connection failed',
                    'status': 'error'}
            return Error(data)

        if data['status'] == 'error':
            return Error(data)
        else:
            return data
