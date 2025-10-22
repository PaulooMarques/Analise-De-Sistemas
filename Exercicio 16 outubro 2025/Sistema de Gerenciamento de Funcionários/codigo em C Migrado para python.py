class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nome} - {self.cargo} - R$ {self.salario:.2f}"

class SistemaFuncionarios:
    def __init__(self, max_funcionarios=100):
        self.funcionarios = []
        self.max_funcionarios = max_funcionarios

    def adicionar_funcionario(self):
        if len(self.funcionarios) >= self.max_funcionarios:
            print("Limite de funcionários atingido!")
            return

        try:
            nome = input("Nome: ").strip()
            if not nome:
                print("Nome não pode ser vazio!")
                return

            cargo = input("Cargo: ").strip()
            if not cargo:
                print("Cargo não pode ser vazio!")
                return

            salario = float(input("Salário: "))
            if salario < 0:
                print("Salário não pode ser negativo!")
                return

            funcionario = Funcionario(nome, cargo, salario)
            self.funcionarios.append(funcionario)
            print("Funcionário cadastrado com sucesso!")

        except ValueError:
            print("Erro: Valor inválido para salário!")
        except KeyboardInterrupt:
            print("\nOperação cancelada.")

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
            return

        print("\nLista de funcionários:")
        for i, func in enumerate(self.funcionarios, 1):
            print(f"{i}) {func}")

    def buscar_funcionario(self):
        nome_busca = input("Nome do funcionário: ").strip()

        for func in self.funcionarios:
            if func.nome.lower() == nome_busca.lower():
                print(f"Cargo: {func.cargo} | Salário: R$ {func.salario:.2f}")
                return

        print("Funcionário não encontrado.")

    def executar(self):
        while True:
            print("\n=== SISTEMA DE FUNCIONÁRIOS ===")
            print("1 - Adicionar funcionário")
            print("2 - Listar funcionários")
            print("3 - Buscar funcionário")
            print("0 - Sair")

            try:
                opcao = input("Escolha uma opção: ").strip()

                if opcao == "1":
                    self.adicionar_funcionario()
                elif opcao == "2":
                    self.listar_funcionarios()
                elif opcao == "3":
                    self.buscar_funcionario()
                elif opcao == "0":
                    print("Encerrando...")
                    break
                else:
                    print("Opção inválida!")

            except KeyboardInterrupt:
                print("\n\nEncerrando...")
                break
            except Exception as e:
                print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    sistema = SistemaFuncionarios()
    sistema.executar()