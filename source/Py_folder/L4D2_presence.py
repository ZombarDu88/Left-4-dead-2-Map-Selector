import os
import time
from pypresence import Presence

def Discord_Rpc():

	epoch_time = int(time.time())
	output_discord = os.popen("wmic process get description").read()

	if output_discord.find("Discord.exe") != -1:

		try:
			client_id = "XD no"
			Rpc = Presence(client_id)
			Rpc.connect()

			Rpc.update()
			print("\033[0;35mThe Discord rpc is \033[1;32mon\033[0;37m")

		except:
			print("\033[0;31mDiscord is launched: but the problem may come from the fact that you are launching discord in admin... or idk no rpc\033[0;37m")

	else:
		print("\033[0;33mDiscord is not launched no rpc\033[0;37m")
