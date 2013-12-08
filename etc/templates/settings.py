#!/usr/bin/env python
# WARNING
# GENERATED AND OVERWRITTEN BY BUILDOUT
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '${parts.buildout.directory}/var/db.sqlite3',
    }
    #'default': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'OPTIONS':{
    #        'db': '${parts.v.mysql_database}',
    #        'host': 'localhost',
    #        'port': 3306,
    #        'user': '${parts.v['sys-user']}',
    #        'passwd': '${parts.v.mysqlpw}',
    #    }
    #}
}
WEBSITE_URL='http://${parts.v['reverse-proxy-host']}'
DEBUG = '${parts.v.debug}'.lower().strip() == 'true'
TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr-fr'
MEDIA_URL = WEBSITE_URL+'/media/'
ADMINS = (
     ('admin', '${parts.v.adminmail}'),
)
SECRET_KEY=s3cuR3

# vim:set et sts=4 ts=4 tw=80:
