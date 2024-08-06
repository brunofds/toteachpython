import logging

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
fh = logging.FileHandler('decorators.log')
ch.setLevel(logging.INFO)
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)


# Abordagem com o email sendo um atributo do método construtor
class CustomersAtribute:

    def __init__(self, first, last):
        self.name = first
        self.last = last
        self.email = '{}.{}'.format(self.name, self.last)

    def full_name(self):
        return '{} {}'.format(self.name, self.last)


# Abordagem com o email sendo retornado pelo método
class CustomersMethod:

    def __init__(self, first, last):
        self.name = first
        self.last = last

    def full_name(self):
        return '{} {}'.format(self.name, self.last)

    def email(self):
        return '{}.{}@gmail.com'.format(self.name, self.last)


# Abordagem com o email sendo o return de um método com decorator (@property). Deve ser chamado como se fosse atributo
class CustomersDecorator:

    def __init__(self, first, last):
        self.name = first
        self.last = last

    def full_name(self):
        return '{} {}'.format(self.name, self.last)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.name, self.last)


cust_1 = CustomersAtribute("Larissa", "Gutierrez")
logger.info(cust_1.email)

cust_2 = CustomersMethod("Bruno", "Silva")
logger.info(cust_2.email())

cust_3 = CustomersDecorator("Ed", "Lola")
logger.info(cust_3.email)


