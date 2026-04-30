from django.shortcuts import render

def calcular_imc(request):
     resultado = None
     classificacao = ""

     if request.method == 'POST':
        try:
            # .get() com valor padrão 0 evita erros se o campo estiver vazio
            peso = float(request.POST.get('peso', 0))
            altura = float(request.POST.get('altura', 0))
            
            imc = peso / (altura ** 2)
            resultado = round(imc, 2)
            
            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif imc < 24.9:
                classificacao = "Peso normal"
            elif imc < 29.9:
                classificacao = "Sobrepeso"
            elif imc < 34.9:
                classificacao = "Obesidade Grau I"
            elif imc < 39.9:
                classificacao = "Obesidade Grau II"
            else:
                classificacao = "Obesidade Grau III (Mórbida)"
                
        except (ZeroDivisionError, ValueError):
            classificacao = "Erro: Insira valores válidos para peso e altura."


     return render(request, 'calculadora/index.html', {
        'resultado': resultado, 
        'classificacao': classificacao
    })


def pagina1(x = None):
    return render(x, 'calculadora/index2.html')

def pagina2(x = None):
    return render(x, 'calculadora/index3.html')

def torradeira(x = None):
    return render(x, 'calculadora/index4.html')

def sistema_solar(x = None):
    return render(x, 'calculadora/index5.html')