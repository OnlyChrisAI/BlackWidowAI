# BlackWidow v37 FREE VOICE EDITION
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform
import os, threading, asyncio

if platform == 'android':
    try:
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.INTERNET, Permission.RECORD_AUDIO])
    except: pass

import pygame
try: pygame.mixer.init()
except: pass

VOICE_DIR = "/storage/emulated/0/blackwidow_logs/voice_pack"

def ensure_voice_dir():
    try: os.makedirs(VOICE_DIR, exist_ok=True)
    except: pass

def play_wav(filename="greeting.wav"):
    ensure_voice_dir()
    path = os.path.join(VOICE_DIR, filename)
    if not os.path.exists(path):
        return f"File not found: {path}"
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        return f"Playing: {filename}"
    except Exception as e: return f"Error: {e}"

async def _gen_sa_voice(text):
    ensure_voice_dir()
    out_path = os.path.join(VOICE_DIR, "sa_voice.mp3")
    try:
        import edge_tts
        communicate = edge_tts.Communicate(text, "en-ZA-LeahNeural")
        await communicate.save(out_path)
        pygame.mixer.music.load(out_path)
        pygame.mixer.music.play()
        return f"SA Voice: {text}"
    except Exception as e: return f"Error: {e}"

def speak_sa_free(text):
    def run():
        try: asyncio.run(_gen_sa_voice(text))
        except:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(_gen_sa_voice(text))
    threading.Thread(target=run, daemon=True).start()
    return "Generating free SA voice..."

class BlackWidowLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        self.status = Label(text="BlackWidow v37 FREE\\nPut WAVs in:\\nblackwidow_logs/voice_pack/", size_hint_y=0.3)
        self.add_widget(self.status)
        btn1 = Button(text="TEST REAL VOICE PACK (Your WAV)", background_color=(0.2,0.8,0.2,1))
        btn1.bind(on_press=lambda x: self.update_status(play_wav("greeting.wav")))
        self.add_widget(btn1)
        btn2 = Button(text="TEST FREE SA FEMALE AI", background_color=(0.2,0.5,1,1))
        btn2.bind(on_press=lambda x: self.update_status(speak_sa_free("Hello Father Chris, BlackWidow is online, free forever")))
        self.add_widget(btn2)
        btn3 = Button(text="LIST VOICE FILES")
        btn3.bind(on_press=lambda x: self.list_files())
        self.add_widget(btn3)
        ensure_voice_dir()
    def update_status(self, msg): self.status.text = str(msg)
    def list_files(self):
        ensure_voice_dir()
        try:
            files = os.listdir(VOICE_DIR)
            self.status.text = "Found:\n" + "\n".join(files) if files else f"Folder empty:\n{VOICE_DIR}"
        except Exception as e: self.status.text = f"Error: {e}"

class BlackWidowApp(App):
    def build(self): return BlackWidowLayout()

if __name__ == "__main__": BlackWidowApp().run()