class Aluno:
    def __init__(self, nome):
        self.__nome = nome
        self.__notas = []

    def adicionar_nota(self, nota):
        if isinstance(nota, (int, float)) and 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            raise ValueError("A nota deve ser um número entre 0 e 10.")

    def obter_nome(self) -> str:
        return self.__nome

    def obter_notas(self) -> list:
        return self.__notas

    def media_notas(self) -> float:
        if self.__notas:
            return sum(self.__notas) / len(self.__notas)
        return 0.0

    def limpar_notas(self):
        self.__notas = []

    def esta_aprovado(self) -> bool:
        return self.media_notas() >= 7

    def __str__(self):
        return f"Aluno: {self.__nome}, Notas: {self.__notas}, Média: {self.media_notas():.2f}"
