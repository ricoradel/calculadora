from calculadora import Calculadora

salario = float(input("Salário Bruto: R$ "))
outros = float(input("Outros descontos: R$ "))
salario = salario - outros

resultado = Calculadora.salario_real(salario)

print("\nSalário Líquido: R$ %.2f" %resultado[0])
print("\nDescontos: \nINSS: R$ %.2f" %resultado[1])
print("IR: R$ %.2f" %resultado[2])


bonus = float(input("\nBônus (PLR) Bruto: R$  "))
resultado_bonus = Calculadora.bonus_real(bonus)
print("\nBônus (PLR) Líquido: R$ %.2f" %resultado_bonus[0])
print("Descontos: IR: R$ %.2f" %resultado_bonus[1])
