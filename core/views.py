from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome):
    return HttpResponse('<h1>Hello {}!</h1>' .format(nome))

def hello2(request):
    return HttpResponse('<h1>Hello World!</h1>' )

def conta(request, operacao, num1, num2):
    if operacao == "Soma":
        return HttpResponse('<h1>A soma é: {}</h1>'.format(int(num1)+int(num2)))
    elif operacao == "Subtracao":
        return HttpResponse('<h1>A subtração é: {}</h1>'.format(int(num1)-int(num2)))
    elif operacao == "Divisao":
        return HttpResponse('<h1>A divisao é: {}</h1>'.format(int(num1)/int(num2)))
    elif operacao == "Multiplicacao":
        return HttpResponse('<h1>A multiplicação é: {}</h1>'.format(int(num1)*int(num2)))