#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'

from pyramid.renderers import render_to_response
from pyramid import renderers
get_template = renderers.get_renderer


def index_view(context, request):
    main = get_template('templates/main_template.pt').implementation()
    return render_to_response(
        'templates/index.pt',
        {'main': main,
         'errors': {}},
        request=request,)
# vim:set et sts=4 ts=4 tw=80:
