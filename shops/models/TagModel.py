from .NamedModel import NamedModel


class Tagmodel(NamedModel):

    class Meta :
        abstract = False
    
    def __str__(self) -> str:
        return self.name