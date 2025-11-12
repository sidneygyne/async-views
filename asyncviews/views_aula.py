import httpx
import asyncio
from time import sleep
from django.http import HttpResponse


# Função assíncrona: conta de 1 a 5 com pausa de 1s e depois faz uma requisição HTTP sem bloquear
async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


# Função síncrona: conta de 1 a 5 com pausa de 1s e depois faz uma requisição HTTP bloqueante
def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)


# View assíncrona: dispara http_call_async() em paralelo e retorna imediatamente sem bloquear a resposta
async def async_view(request):
    asyncio.create_task(http_call_async())  # cria a tarefa assíncrona
    return HttpResponse("Non-blocking HTTP request")


# View síncrona: executa http_call_sync() de forma sequencial e só retorna após terminar (bloqueia o fluxo)
def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")
