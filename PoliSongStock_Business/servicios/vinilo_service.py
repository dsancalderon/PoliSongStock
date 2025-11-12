from entidades.comic import Comic  # Asegúrate de tener esta clase definida similar a Vinilo

class ComicService:
    def __init__(self):
        self.comics = {}  # id -> Comic

    def registrar_comic(self, id:int, titulo:str, autor:str, anio:int, precio:float, stock:int):
        """Registra un nuevo cómic en el sistema"""
        if id in self.comics:
            raise ValueError("Cómic ya existe")
        c = Comic(id, titulo, autor, anio, precio, stock)
        self.comics[id] = c
        return c

    def asociar_personaje(self, comic_id:int, personaje):
        """Asocia un personaje al cómic"""
        if comic_id not in self.comics:
            raise ValueError("Cómic no encontrado")
        c = self.comics[comic_id]
        c.asociar_personaje(personaje)
        return c

    def consultar_disponibles(self):
        """Devuelve todos los cómics con stock > 0"""
        return [c for c in self.comics.values() if c.consultar_disponibilidad()]
