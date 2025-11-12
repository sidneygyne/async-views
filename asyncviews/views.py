import httpx
import asyncio

from django.http import HttpResponse



async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


async def api_view(request):
    await http_call_async()
    return HttpResponse("Chamada HTTP assíncrona concluída!")