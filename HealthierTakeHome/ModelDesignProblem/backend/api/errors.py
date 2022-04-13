from . import api


@api.app_errorhandler(405)
def unsported_method(e):
    return "Method Not Allowed", 405
