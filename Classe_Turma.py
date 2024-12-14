class Aluno:
    def __init__(self, nome):
        self.__nome = nome
        self.__notas = []

    def adicionar_nota(self, nota):
        if isinstance(nota, (int, float)):
            self.__notas.append(nota)
        else:
            raise ValueError("A nota deve ser um número.")

    def obter_nome(self):
        return self.__nome

    def obter_notas(self):
        return self.__notas

    def media_notas(self):
        if self.__notas:
            return sum(self.__notas) / len(self.__notas)
        return 0


class Turma:
    def __init__(self):
        self.__alunos = []

    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.__alunos.append(aluno)
        else:
            raise TypeError("Deve ser um objeto da classe Aluno.")

    def obter_nota(self, nome):
        for aluno in self.__alunos:
            if aluno.obter_nome() == nome:
                return aluno.obter_notas()
        return None

    def media_notas(self):
        total_notas = sum(aluno.media_notas() for aluno in self.__alunos)
        return total_notas / len(self.__alunos) if self.__alunos else 0

    def alunos_acima_da_media(self):
        media = self.media_notas()
        return [aluno.obter_nome() for aluno in self.__alunos if aluno.media_notas() > media]



