"""
Exemplo 1
Exemplificação o nível/level do log default
"""
import logging.config
import config

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)  # Corresponds to the name of the module wich this method is called
# log_format = '%(asctime)s:%(name)s:%(levelname)s:%(filename)s:%(message)s'
# logging.basicConfig(filename='exemplo2.log',
#                     level=logging.WARNING,
#                     format=log_format)


def soma(x: int, y: int) -> int:
    """
    Função que efetua a soma de dois números inteiros
    """
    if isinstance(x, int) and isinstance(y, int):
        logger.warning(f'x: {x} + y: {y}')
        return x + y
    else:
        logger.info(f'x: {x} type: {type(x)} - y: {y} type: {type(y)}')


def money_save(count, hours):
    money = count * hours
    logger.info('name1')
    return money


config.subtrai(7, 8)
soma(8, 9)
money_save(2, 5)

