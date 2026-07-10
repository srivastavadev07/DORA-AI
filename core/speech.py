import asyncio
import edge_tts
import pygame
import os

VOICE = "en-US-GuyNeural"


async def _speak_async(text):
    filename = "temp_voice.mp3"

    communicate = edge_tts.Communicate(text=text, voice=VOICE)
    await communicate.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()
    pygame.mixer.quit()

    os.remove(filename)


def speak(text):
    print(f"\n🤖 DORA: {text}")
    asyncio.run(_speak_async(text))