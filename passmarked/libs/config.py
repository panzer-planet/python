from requests import get
from platform import platform, release, system


def get_ip():
    return get('https://api.ipify.org').text


def get_platform():
    return platform()


def get_release():
    return release()


def get_system():
    return system()


def get_application_meta(user_config):
    meta = {'appname': user_config['appname'],
            'source': str(get_ip()),
            'device': user_config['device'],
            'version': '2' if user_config['version'] is None else
                       user_config['version'],
            'platform': str(get_system()),
            'release': str(get_release()),
            'token': user_config['token']}
    return meta
