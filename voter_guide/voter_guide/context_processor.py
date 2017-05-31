# -*- coding: utf-8 -*-
from django.conf import settings


def current_url(request):
    return {'current_url': settings.SITE_DOMAIN + request.get_full_path()}

def site_domain(request):
    return {'site_domain': settings.SITE_DOMAIN}
