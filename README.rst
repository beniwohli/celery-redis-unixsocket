celery-redis-unixsocket
=======================


This package provides a celery result backend and a kombu transport for Redis
using unix sockets instead of TCP.

Usage
-----

Add this to your settings::

    BROKER_TRANSPORT = 'celery_redis_unixsocket.broker.Transport'
    BROKER_HOST = '/path/to/redis.sock'
    BROKER_VHOST = 0

And if you want to store results::

    CELERY_RESULT_BACKEND = 'redisunixsocket'
    CELERY_REDIS_HOST = '/path/to/redis.sock'

    CELERY_IGNORE_RESULT = False

    import celery_redis_unixsocket

The ``import celery_redis_unixsocket`` is important because it registers
``redisunixsocket`` as a result backend.

.. note::

   This code has only been tested with Django.
