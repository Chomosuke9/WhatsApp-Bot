from datetime import datetime, timezone, timedelta
import re
import threading
from emoji_changer import replace_emoji_with_symbol
from Cek_khodam_function import cek_khodam, arti
from Ai_Function import gpt
import time
import function_list as Wa
import Configs
from time_counter import get_remaining_seconds
import Database

start_time = time.time()
now = datetime.now()
Wa.start(Configs.is_headless)
Wa.unread()
mode = 0
lock = threading.Lock()

time_zone = Configs.time_zone
developer = Configs.developer
Model = Configs.Model
system_prompt = Configs.system_prompt
Temperature = Configs.Temperature
Max_token = Configs.Max_token
Top_P = Configs.Top_P

messages = [{"role": "system", "content": system_prompt}]

day_dict = {
    0: 'Senin',
    1: 'Selasa',
    2: 'Rabu',
    3: 'Kamis',
    4: 'Jumat',
    5: 'Sabtu',
    6: 'Minggu'
}


def start():
    last_chat = ""
    sender = ""
    while True:
        try:
            result = Wa.lastchat()
            last_chat = result[0]
            sender = result[1]
        except:
            pass
        if last_chat.lower() == "start":
            if sender[:(len(developer))] == developer:
                global mode
                Wa.send("Service start")
                mode = 1
                break
            else:
                Wa.send("This command can only used by Developer")
        else:
            time.sleep(0.2)

def main():
    global Model, system_prompt, Temperature, Max_token, Top_P, last_chat, sender, messages
    while True:
        try:
            result = Wa.lastchat()
            last_chat = result[0]
            sender = result[1]
            time.sleep(0.2)
        except:
            print("Someone is typing...")
            last_chat = ""
            sender = ""
            time.sleep(0.2)
            break
        if last_chat.lower() == "stop":
            if sender[:(len(developer))] == developer:
                global mode
                mode = 0
                Wa.send("Service stopped")
                break
            else:
                Wa.send("Only Developer can stop the service")

        elif last_chat[:3].lower() == "gpt":
            messages.append({"role": "user", "content": last_chat[3:]})
            response = gpt(messages, Temperature, Model, Max_token, Top_P)
            response = replace_emoji_with_symbol(response)
            messages.append({"role": "assistant", "content": response})
            Wa.send_keys(response)
            Wa.send("")

        elif last_chat[:6].lower() == "khodam":
            Wa.send_keys("❏  INFO  KHODAM")
            Wa.send_keys("╭─────────────────┈")
            Wa.send_keys(f"│ ɴᴀᴍᴇ :{last_chat[6:]}")
            Wa.send_keys(f"│ ᴋʜᴏᴅᴀᴍ : {cek_khodam(last_chat[6:])}")
            Wa.send_keys(f"│ ᴀʀᴛɪ : {arti()}")
            Wa.send("╰─────────────────┈")

        elif last_chat.lower() == "system info":
            end_time = time.time()
            runtime_seconds = int(end_time - start_time)
            days = runtime_seconds // (24 * 3600)
            hours = runtime_seconds // 3600
            hours %= 24
            runtime_seconds %= 3600
            minutes = runtime_seconds // 60
            # Calculate whatever needed

            Wa.send_keys("❏ DATE  INFO ❏")
            Wa.send_keys("╭─────────────────┈")
            Wa.send_keys(f"│ ᴛɪᴍᴇ : {datetime.now(timezone(timedelta(hours=time_zone))).strftime("%H:%M:%S")}")
            Wa.send_keys(f"│ ʙᴜʟᴀɴ : {datetime.now().strftime("%B")}")
            Wa.send_keys(f"│ ᴅᴀᴛᴇ : {datetime.now().strftime("%d")}")
            Wa.send_keys(f"│ ʀᴜɴᴛɪᴍᴇ :  {days} Days {hours} Hours {minutes} Minutes")
            Wa.send("╰─────────────────┈")
            Wa.send_keys("❏ LLM  INFO ❏")
            Wa.send_keys("╭─────────────────┈")
            Wa.send_keys(f"│ᴍᴏᴅᴇʟ : {Model}")
            Wa.send_keys(f"│sʏsᴛᴇᴍ ᴘʀᴏᴍᴘᴛ : {system_prompt}")
            Wa.send_keys(f"│ᴛᴇᴍᴘᴇʀᴀᴛᴜʀᴇ : {Temperature}")
            Wa.send_keys(f"│ᴍᴀxɪᴍᴜᴍ ᴛᴏᴋᴇɴ : {Max_token} Token")
            Wa.send_keys(f"│ᴛᴏᴘ_ᴘ : {Top_P}")
            Wa.send("╰─────────────────┈")
        elif last_chat.lower() == "reset memory":
            messages = [{"role": "system", "content": system_prompt}]
            Wa.send("Memory has been reset")
        elif last_chat.lower() == "user info":
            if sender[:(len(developer))] == developer:
                sender = "Raja Iblis"
                role = "Developer"
            else:
                role = "Pengangguran"

            Status = "Alive"
            age = 0
            Wa.send_keys("❏ USER  INFO ❏")
            Wa.send_keys("╭─────────────────┈")
            Wa.send_keys(f"│ɴᴀᴍᴇ : {sender}")
            Wa.send_keys(f"│ꜱᴛᴀᴛᴜꜱ : {Status}")
            Wa.send_keys(f"│ʀᴏʟᴇ : {role}")
            Wa.send_keys(f"│ᴀɢᴇ : {age} Days")
            Wa.send("╰─────────────────┈")
        elif last_chat[:3].lower() == "set":

            if last_chat[:15].lower() == "set temperature":
                clean_value = re.sub(r'[^0-9.]', '', last_chat[16:])
                if clean_value == "":
                    Wa.send("Temperature cant be empty")
                else:
                    Temperature = float(clean_value)
                    Wa.send("Temperature updated to " + clean_value)

            elif last_chat[:10].lower() == "set prompt":
                system_prompt = last_chat[11:]
                messages = [{"role": "system", "content": system_prompt}]
                Wa.send("System prompt updated")

            elif last_chat[:9].lower() == "set model":
                if sender[:(len(developer))] == developer:
                    if last_chat[-1] == "1":
                        Model = "gemma2-9b-it"
                        Wa.send("Model changed to gemma2-9b-it")

                    elif last_chat[-1] == "2":
                        Model = "gemma-7b-it"
                        Wa.send("Model changed to gemma-7b-it")

                    elif last_chat[-1] == "3":
                        Model = "llama-3.1-70b-versatile"
                        Wa.send("Model changed to llama-3.1-70b-versatile")
                        Wa.send("Model with 70 Billion parameters will take longer time to response")

                    elif last_chat[-1] == "4":
                        Model = "llama-3.1-8b-instant"
                        Wa.send("Model changed to llama-3.1-8b-instant")

                    elif last_chat[-1] == "5":
                        Model = "llama3-70b-8192"
                        Wa.send("Model changed to llama3-70b-8192")
                        Wa.send("Model with 70 Billion parameters will take longer time to response")

                    elif last_chat[-1] == "6":
                        Model = "llama3-8b-8192"
                        Wa.send("Model changed to llama3-8b-8192")

                    elif last_chat[-1] == "7":
                        Model = "llama3-groq-70b-8192-tool-use-preview"
                        Wa.send("Model changed to llama3-groq-70b-8192")

                    elif last_chat[-1] == "8":
                        Model = "llama3-groq-8b-8192-tool-use-preview"
                        Wa.send("Model changed to llama3-groq-8b-8192")

                    elif last_chat[-1] == "9":
                        Model = "mixtral-8x7b-32768"
                        Wa.send("Model changed to mixtral-8x7b-32768")

                    else:
                        Wa.send_keys("❏ MODEL LIST ❏")
                        Wa.send_keys("╭─────────────────┈")
                        Wa.send_keys("│1. gemma2-9b-it")
                        Wa.send_keys("│2. gemma-7b-it")
                        Wa.send_keys("│3. llama-3.1-70b-versatile")
                        Wa.send_keys("│4. llama-3.1-8b-instant")
                        Wa.send_keys("│5. llama3-70b-8192")
                        Wa.send_keys("│6. llama3-8b-8192")
                        Wa.send_keys("│7. llama3-groq-70b-8192")
                        Wa.send_keys("│8. llama3-groq-8b-8192")
                        Wa.send_keys("│9. mixtral-8x7b-32768")
                        Wa.send("╰─────────────────┈")
                    messages = [{"role": "system", "content": system_prompt}]
                    Wa.send("Model changed to " + last_chat[-1])
                else:
                    Wa.send("Model only can changed by Developer")

            elif last_chat[:17].lower() == "set maximum token":
                if sender[:(len(developer))] == developer:
                    Max_token = int(last_chat[18:])
                    Wa.send(f"Maximum token are caped at {Max_token} tokens")
                else:
                    Wa.send("Maximum token can only be changed by Developer")
            else:
                pass

        else:
            pass
        Wa.click_2nd_row()
        time.sleep(1)
        break


def daily():
    global mode
    Wa.group()
    Wa.search_contact("Online Terrorist")
    now = datetime.now()
    day = now.weekday()
    day = day_dict[day]
    n = 1
    jadwal = Database.jadwal(day)
    Wa.send_keys(f"❏ MATA PELAJARAN HARI {day} ❏")
    Wa.send_keys("╭─────────────────┈")
    for j in jadwal[0]:
        Wa.send_keys(f"│• Jam {n} : {j}")
        n += 1
    Wa.send("╰─────────────────┈")
    mode = 1
    Wa.unread()


def main_thread():
    global mode
    while True:
        if mode == 1:
            main()
        elif mode == 0:
            start()
        elif mode == 2:
            daily()
        else:
            input("press enter to start")
            mode = 1


def mode_manager():
    while True:
        global mode
        time.sleep(get_remaining_seconds())
        with lock:
            mode = 2
        time.sleep(120)


# Create two threads
t1 = threading.Thread(target=mode_manager)
t2 = threading.Thread(target=main_thread)
# Start the threads


if __name__ == "__main__":
    t1.start()
    t2.start()
