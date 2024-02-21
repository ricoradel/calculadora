# Calculadora
# Calcular Salário Real
# Calcular Bonus (PLR) Real
# Calcular Imposto de Renda
# Calcular Juros Compostos (Simular investimentos)

class Calculadora:
  # -- Descontos salário
    
  def inss_discount(salario):
    if salario < 1412:
      return salario * (7.5 / 100)
    elif salario > 1412 and salario < 2666.68:
      return salario * (9 / 100) - 21.18
    elif salario > 2666.68 and salario < 4000.03:
      return salario * (12 / 100) - 101.18
    elif salario > 4000.03:
      return salario * (14 / 100) - 181.18
    
  def ir_discount(salario):
    if salario < 2112:
      return 0
    elif salario > 2112 and salario < 2826.65:
      return salario * 7.5 / 100 - 158.4
    elif salario > 2826.65 and salario < 3751.05:
      return salario * 15 / 100 - 370.4
    elif salario > 3751.05 and salario < 4664.68:
      return salario * 22.5 / 100 - 651.73
    elif salario > 4664.68:
      return salario * 27.5 / 100 - 884.96 
    
  def ir_bonus(bonus):
    if bonus < 6677.55:
      return 0
    elif bonus > 6677.55 and bonus < 9922.28:
      return bonus * 7.5 / 100 - 500.82
    elif bonus > 9922.28 and bonus < 13167:
      return bonus * 15 / 100 - 1244.99
    elif bonus > 13167 and bonus < 16380.38:
      return bonus * 22.5 / 100 - 2232.51
    elif bonus > 16380.38:
      return bonus * 27.5 / 100 - 3051.53

  # -- Calculadora de Sálario Real

  def salario_real(salario):  
    inss = Calculadora.inss_discount(salario)
    salario_inss = salario - inss
    ir = Calculadora.ir_discount(salario_inss)
    salario_liquido = salario_inss - ir
    return salario_liquido, inss, ir

 # -- Calculadora Bônus (PLR)
  
  def bonus_real(bonus):
    ir = Calculadora.ir_bonus(bonus)
    bonus_liquido = bonus - ir
    return bonus_liquido, ir
