# -*- coding: utf-8 -*-

__version__ = '0.1'

try:
    from celery.backends import BACKEND_ALIASES
    BACKEND_ALIASES['redisunixsocket'] = 'celery_redis_unixsocket.store.RedisUnixSocketBackend'
except ImportError:
    pass