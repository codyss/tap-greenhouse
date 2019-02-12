from tap_kit import TapExecutor, BaseClient, main_method

from .streams import STREAMS

REQUIRED_CONFIG_KEYS = ["start_date", 'api_key']


class GreenhouseTap(TapExecutor):
    url = 'https://harvest.greenhouse.io/v1/'
    pagination_type = 'next'
    replication_key_format = 'iso8061'
    auth_type = 'basic_key'


def main():
    main_method(
        REQUIRED_CONFIG_KEYS,
        GreenhouseTap,
        BaseClient,
        STREAMS
    )


if __name__ == '__main__':
    main()
