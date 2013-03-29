# -*- coding: utf-8 -*-

from kombu.transport import redis as kombu_redis
import redis


class Channel(kombu_redis.Channel):

    def _get_pool(self):
        parameters = self._connparams()
        parameters.update({
            'connection_class': redis.UnixDomainSocketConnection,
            'path': parameters.pop('host', None),
        })
        parameters.pop('port', None)
        return redis.ConnectionPool(**parameters)

    def _create_client(self):
        return self.Client(connection_pool=self.pool)


class Transport(kombu_redis.Transport):
    Channel = Channel
