from django.shortcuts import render

def calcular_imc(request):
     resultado = None
     classificacao = ""
    
     if request.method == 'POST':
        # Captura o que foi digitado no formulário HTML
        peso = float(request.POST.get('peso'))
        altura = float(request.POST.get('altura'))
        
        try:
            imc = peso / (altura ** 2)

        except ZeroDivisionError:
            return render(request, 'calculadora/index.html',
                          {
                              'resultado: "Erro!!!',
                              'classificacao: "A altura não pode ser Zero!!!'
                          }
                      )


        resultado = round(imc, 2)

     if imc < 18.5:
            classificacao = "Abaixo do peso"
     elif imc >= 18.5 and imc < 24.9:
            classificacao = "Peso normal"
     elif imc >= 25.0 and imc < 29.9:
            classificacao = "Sobrepeso"
     elif imc >= 30.0 and imc < 34.9:
            classificacao = "Obesidade Grau I"
     elif imc >= 35.0 and imc < 39.9:
        classificacao = "Obesidade Grau II"
     else:
        classificacao = "Obesidade Grau III (Mórbida)"
    
     return render(request, 'calculadora/index.html', 
	    {
        'resultado': resultado, 
        'classificacao': classificacao
	    }
    )

    