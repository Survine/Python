import pyautogui
import time

message = input('message:')
mentions = input('mentions (comma-separated): ')
duration = input('duration:')
repeats = input('repeats: ')

time.sleep(10)

mention_list = mentions.split(',')

for i in range(int(repeats)):
    message_with_mentions = message

    for mention in mention_list:
        mention_syntax = f"@{mention.strip()}"  # Corrected mention syntax
        message_with_mentions = message_with_mentions.replace(
            f"@{mention.strip()}", mention_syntax)

    pyautogui.write(message_with_mentions)
    pyautogui.press('enter')
    time.sleep(int(duration))
