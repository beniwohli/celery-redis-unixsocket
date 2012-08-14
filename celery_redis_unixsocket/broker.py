# -*- coding: utf-8 -*-

from kombu.transport import redis as kombu_redis
import redis


class Channel(kombu_redis.Channel):

    def _create_client(self):
        conninfo = self.connection.client
        database = conninfo.virtual_host
        if not isinstance(database, int):
            if not database or database == "/":
                database = kombu_redis.DEFAULT_DB
            elif database.startswith("/"):
                database = database[1:]
            try:
                database = int(database)
            except ValueError:
                raise ValueError(
                    "Database name must be int between 0 and limit - 1")
        if conninfo.hostname and conninfo.hostname.startswith('/'):
            pool = redis.ConnectionPool(
                connection_class=redis.UnixDomainSocketConnection,
                path=conninfo.hostname,
                db=database,
                password=conninfo.password,
            )
        else:
            pool = None

        return self.Client(
            host=conninfo.hostname,
            port=conninfo.port or kombu_redis.DEFAULT_PORT,
            db=database,
            password=conninfo.password,
            connection_pool=pool,
        )


class Transport(kombu_redis.Transport):
    Channel = Channel
