
from suit.apps import DjangoSuitConfig

class C130Config(DjangoSuitConfig):
    layout = 'horizontal'
    name = 'c130'

    def ready(self):
        import c130.signals