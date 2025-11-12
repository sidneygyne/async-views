import httpx
import asyncio
from time import sleep
from django.http import HttpResponse


async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)

def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)

""" Executa de forma assíncrona: dispara a tarefa e retorna sem bloquear """
""" async_view → dispara http_call_async() em paralelo, retorna a resposta imediatamente. """
async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")

""" Executa de forma síncrona: bloqueia até terminar todas as etapas """
""" sync_view → só retorna depois que http_call_sync() terminar (bloqueia o fluxo). """
def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")