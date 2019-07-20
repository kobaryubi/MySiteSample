from urllib.parse import urlparse, parse_qs

class RequestOperator(object):
    def __init__(self):
        pass

    @staticmethod
    def get_redirect_to(request):
        http_referer = request.META.get("HTTP_REFERER", None)
        if http_referer is None: return None
        parsed_url = urlparse(http_referer)
        query = parsed_url.query
        if len(query) == "": return None
        redirect_to_list = parse_qs(query).get("redirect_to", None)
        if redirect_to_list is None: return None
        return redirect_to_list[0]

