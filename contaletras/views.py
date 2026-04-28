from django.shortcuts import render
def contar_letras(request):
    texto = ""
    resultado = None

    if request.method == "POST":
        texto = request.POST.get("texto", "")
        resultado = len(texto)

    return render(request, "contaletras/formulario.html", {
        "texto": texto,
        "resultado": resultado
    })