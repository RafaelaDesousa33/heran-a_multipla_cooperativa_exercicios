class ContaBancaria:
    def __init__(self,saldo):
        self.saldo = saldo
      

class ContaCorrente(ContaBancaria):
    def __init__(self, limite, **kwargs):
        self.limite = limite
        super().__init__(**kwargs)

class ContaInvestimento(ContaBancaria):
    def __init__(self,rendimento, **kwargs):
        self.rendimento = rendimento
        super().__init__(**kwargs)


class ContaPremium(ContaCorrente,ContaInvestimento):
    def exibir_dados(self):
        return (
            f"Saldo:{self.saldo:.2f}\n"
            f"limite:{self.limite:.2f}\n"
            f"rendimento:{self.rendimento:.2f}\n"
        )

conta_premium = ContaPremium(
    saldo=1000,
    limite=5000,
    rendimento=0.12
)

print(conta_premium.exibir_dados())

print("---------------------------------------")

class Curso:
    def __init__(self,nome):
        self.nome = nome

class CursoPresencial(Curso):
    def __init__(self,sala, **kwargs):
        super().__init__(**kwargs)
        self.sala =  sala

class CursoOnline(Curso):
    def __init__(self,plataforma,**kwargs):
        super().__init__(**kwargs)
        self.plataforma = plataforma

class CursoHibrido(CursoPresencial,CursoOnline):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def imprimir_dados(self):
        return(
            f"Curso Hibrido\n"
            f"nome:{self.nome}\n"
            f"sala:{self.sala}\n"
            f"plataforma:{self.plataforma}\n"
        )
    
curso_hibrido = CursoHibrido(
    nome="Matematica",
    sala="Sala 02",
    plataforma="ead.curso",
 
)
print(curso_hibrido.imprimir_dados())

print("--------------------------")

class Funcionario:
    def __init__(self,nome,salario,funcao):
        self.nome = nome
        self.salario = salario
        self.funcao = funcao

    
class Tecnico(Funcionario):
    def __init__(self,especialidade, **kwargs):
        super().__init__(**kwargs)
        self.especialidade = especialidade

class Gestor(Funcionario):
    def __init__(self,equipe, **kwargs):
        self.equipe = equipe
        super().__init__(**kwargs)

class TechLead(Tecnico,Gestor):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def exibir_dados(self):
        return (
            f"nome:{self.nome}\n"
            f"salario:{self.salario}\n"
            f"funcao:{self.funcao}\n"
            f"especialidade:{self.especialidade}\n"
            f"equipe:{self.equipe}\n"
        )
    


tech_lead1 = TechLead(
    nome="Marcos",
    salario=2000,
    funcao="Tech lead",
    especialidade="Sistemas embarcados",
    equipe="Equipe 364",
)

print(tech_lead1.exibir_dados())