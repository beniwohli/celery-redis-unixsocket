# -*- coding: utf-8 -*-

from celery.backends.redis import RedisBackend
from celery.utils import cached_property


class RedisUnixSocketBackend(RedisBackend):

    @cached_property
    def client(self):
        if self.host.startswith('/'):
            pool = self.redis.ConnectionPool(
                connection_class=self.redis.UnixDomainSocketConnection,
                path=self.host,
                db=self.db,
            )
            return self.redis.Redis(connection_pool=pool)
        else:
            return super(RedisUnixSocketBackend, self).client
