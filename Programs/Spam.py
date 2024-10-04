import pyautogui
import time

message = input('message: ')
mentions = input('mentions (comma-separated): ')
duration = input('duration (seconds): ')
repeats = input('repeats: ')

time.sleep(10)  # Time delay to switch to the desired window

mention_list = mentions.split(',')

for i in range(1, int(repeats) + 1):
    message_with_mentions = f"{message} {i}"  # Add the iteration number to the message

    for mention in mention_list:
        mention_syntax = f"@{mention.strip()}"  # Ensure proper mention syntax
        message_with_mentions = message_with_mentions.replace(
            f"@{mention.strip()}", mention_syntax)

    pyautogui.write(message_with_mentions)
    pyautogui.press('enter')
    time.sleep(int(duration))

