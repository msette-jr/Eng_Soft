"""Implemente as modificações necessárias para que a classe siga as boas práticas de design, garantindo maior coesão, ocultamento de informações e uma estrutura de código mais robusta e de fácil manutenção."""

class Aluno:
    def __init__(self, nome):
        self.__nome = nome
        self.__notas = []

    def adicionar_nota(self, nota):

        if not isinstance(nota, (int, float)):
            raise ValueError("A nota deve ser um número.")
        self.__notas.append(nota)

    def obter_nome(self):

        return self.__nome

    def obter_notas(self):

        return self.__notas

    def media_notas(self):

        return sum(self.__notas) / len(self.__notas) if self.__notas else 0


class Turma:
    def __init__(self):
        self.__alunos = []

    def adicionar_aluno(self, aluno):

        if not isinstance(aluno, Aluno):
            raise TypeError("Deve ser um objeto da classe Aluno.")
        self.__alunos.append(aluno)

    def obter_nota(self, nome):

        aluno = self.__encontrar_aluno_por_nome(nome)
        return aluno.obter_notas() if aluno else None

    def media_notas(self):

        total_notas = sum(aluno.media_notas() for aluno in self.__alunos)
        return total_notas / len(self.__alunos) if self.__alunos else 0

    def alunos_acima_da_media(self):

        media_turma = self.media_notas()
        return [aluno.obter_nome() for aluno in self.__alunos if aluno.media_notas() > media_turma]

    def __encontrar_aluno_por_nome(self, nome):

        for aluno in self.__alunos:
            if aluno.obter_nome() == nome:
                return aluno
        return None

# Exemplo de uso:

# para criar a turma
turma = Turma()

# Para criar os alunos
aluno1 = Aluno("Alberto")
aluno1.adicionar_nota(7.0)
aluno1.adicionar_nota(8.5)
aluno1.adicionar_nota(9.0)

aluno2 = Aluno("Beto")
aluno2.adicionar_nota(6.0)
aluno2.adicionar_nota(7.0)
aluno2.adicionar_nota(8.0)

# Para adicionar os alunos à turma
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)

# Para obter informações
nome = aluno1.obter_nome()
notas = aluno1.obter_notas()
media = aluno1.media_notas()

print(f"Nome: {nome}")
print(f"Notas: {notas}")
print(f"Média: {media}")

# média da turma
media_turma = turma.media_notas()
print(f"Média da turma: {media_turma}")

# Alunos acima da média
alunos_acima_da_media = turma.alunos_acima_da_media()
print(f"Alunos acima da média: {alunos_acima_da_media}")

"""Modificações relevantes:

1 - Agora, os atributos privados, como __nome e __notas, estão sendo utilizados corretamente para ocultar a implementação interna da classe Aluno, garantindo o encapsulamento.

2 - O método __encontrar_aluno_por_nome na classe Turma foi definido como privado, impedindo que o código externo acesse diretamente essa funcionalidade, o que também segue o princípio de encapsulamento.

3 - A coesão do código foi aprimorada, pois agora cada classe tem uma responsabilidade mais bem definida: a classe Aluno cuida dos dados relacionados ao aluno e a classe Turma gerencia a turma como um todo.

4 -  manutenção do código ficou mais fácil, pois os métodos estão mais claros e com responsabilidades bem separadas. Isso significa que alterações no cálculo das notas dos alunos, por exemplo, podem ser feitas sem impactar diretamente a classe Turma e vice-versa, tornando o código mais flexível e modular."""