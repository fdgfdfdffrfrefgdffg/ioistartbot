import aiohttp
from aiogram.types import Message
import re
import html  

async def send_task_details(message: Message):
    task_num = message.text[7:]
    task_num = task_num.zfill(4)
    url = f"https://robocontest.uz/api/tasks/{task_num}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                data = data["data"]

                html_text = f"{data['number']}-masala {data['title']}\n\n{data['description']}\n{data['input_info']}\n\n{data['output_info']}"
                
                img_urls = re.findall(r'<img[^>]+src="([^"]+)"', html_text)
                img_url = img_urls[0] if img_urls else None
                html_text = re.sub(r'<img[^>]+>', '', html_text)
                
                plain_text = re.sub(r'<[^>]*>', '', html_text)  
                telegram_text = html.unescape(plain_text)  

                telegram_text = re.sub(r'\\\((.*?)\\\)', r'\1', telegram_text)

                if img_url:
                    await message.answer(
                        photo=img_url,
                        caption=telegram_text
                    )
                else:
                    await message.answer(
                        text=telegram_text
                    )
