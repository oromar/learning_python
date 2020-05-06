from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, name, age):
    return HttpResponse(
        '<h1>Hello {name} de {age} anos!</h1>'
            .format(name=name, age=age)
    )
def sum(request, numA, numB):
    return HttpResponse(
        f'''
            <h1>{numA + numB}</h1>
        '''
    )
def sub(request, numA, numB):
    return HttpResponse(
        f'''
            <h1>{numA - numB}</h1>
        '''
    )
def mul(request, numA, numB):
    return HttpResponse(
        f'''
            <h1>{numA * numB}</h1>
        '''
    )
def div(request, numA, numB):
    return HttpResponse(
        f'''
            <h1>{numA / numB}</h1>
        '''
    )