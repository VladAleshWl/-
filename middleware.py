import re


MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)


def mobile(request):

    if MOBILE_AGENT_RE.match(request.META.get('HTTP_USER_AGENT', '')):
        return True

    return False


class DomainMiddleware(object):

    def process_request(self, request):

        setattr(request, 'mobile', mobile(request))

