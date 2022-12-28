import os
import time
from pypresence import Presence

def Discord_Rpc():

	epoch_time = int(time.time())
	output_discord = os.popen("wmic process get description").read()

	if output_discord.find("Discord.exe") != -1:

		client_id = "1056228703073476731"
		Rpc = Presence(client_id)
		Rpc.connect()

		Rpc.update(details="ver 1.1.5", state="Credits: NoNoDu88, FoxTroT, Kef", large_image="l4d2_map_selector_icon", start=epoch_time,
		buttons=[{"label": "The Program\U0001F40D (1.1.5)" , "url": "https://github.com/ZombarDu88/Left-4-dead-2-Map-Selector"}])

	else:
		print("\033[0;31mDiscord is not launched no rpc\033[0;37m")