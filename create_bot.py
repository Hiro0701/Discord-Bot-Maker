# -*- coding: utf-8 -*-

bot_name = input("Your bot's name: ")

token_name = f'{bot_name}_token'
globals()[token_name] = input("Your bot's token: ")

bot_prefix = input("Your bot's prefix: ")

import os
import shutil

current_path = os.path.dirname(__file__)
source_folder = os.path.join(current_path + 'base', 'cogs')
target_folder = os.path.join(current_path, bot_name)

shutil.copytree(source_folder, os.path.join(target_folder, 'cogs'))

with open(f'{current_path}base/py_context.txt', 'r') as txt:
    context = txt.read()
    formatted_context = context.format(
        bot_name=bot_name,
        bot_prefix=bot_prefix,
        token_name=token_name,
        globals=globals(),
    )

    with open(f'{target_folder}/main.py', 'w') as file:
        file.write(formatted_context)

    with open(f'{target_folder}/.env', 'w') as file:
        file.write(f"{token_name} = '{globals()[token_name]}'")
