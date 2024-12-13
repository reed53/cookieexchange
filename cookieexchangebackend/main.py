import logging


LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event, context) -> str:
    """
    Lambda handler
    :param event: Not used
    :param context: Not used
    :return:
    :raises
    """
    logging.info('here')
    return 'OK'


def main() -> None:
    """
    """
    pass


if __name__ == '__main__':
    main()
