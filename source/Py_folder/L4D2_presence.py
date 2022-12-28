import os
import time
from pypresence import Presence

def Discord_Rpc():

	epoch_time = int(time.time())
	output_discord = os.popen("wmic process get description").read()

	if output_discord.find("Discord.exe") != -1:

		client_id = "XD no"
		Rpc = Presence(client_id)
		Rpc.connect()

		Rpc.update()

	else:
		print("\033[0;31mDiscord is not launched no rpc\033[0;37m")
