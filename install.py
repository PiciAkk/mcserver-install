import json
import os
import argparse
import requests
from progress.bar import Bar

parser = argparse.ArgumentParser(description='Minecraft server installer')

parser.add_argument("--servertype", "-s", dest='serverType', help="Type of the server, ex: spigot, sponge, spongeforge, bukkit, forge")
parser.add_argument("--version", "-v", dest="minecraftVersion", help="Minecraft version of the server, ex: 1.12.2")
args = parser.parse_args()

# default server type
if args.serverType == None:
    serverType = "vanilla"
else:
    serverType = args.serverType

# default minecraft version
if args.minecraftVersion == None:
    minecraftVersion = json.loads(requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json").text)["latest"]["release"]
else:
    minecraftVersion = args.minecraftVersion

if serverType == "vanilla":
    print(f"Installing vanilla minecraft server. Version: {minecraftVersion}")
    bar = Bar('Downloading...', max=2)
    url = f"https://s3.amazonaws.com/Minecraft.Download/versions/{minecraftVersion}/minecraft_server.{minecraftVersion}.jar"
    bar.next()
    filename = url.rsplit('/', 1)[1]
    open(filename, "wb").write(requests.get(url).content)
    bar.next()
    bar.finish()
    bar = Bar('Making directory...', max=1)
    os.mkdir("server")
    bar.next()
    bar.finish()
    bar = Bar('Moving file...', max=1)
    os.replace(filename, f"server/{filename}")
    bar.next()
    bar.finish()
    bar = Bar('Generating server...', max=1)
    os.system(f"cd server && java -jar {filename}")
    bar.next()
    bar.finish()
    bar = Bar('Accepting eula.txt...', max=1)
    open("server/eula.txt", "w").write("\neula=true")
    bar.next()
    bar.finish()
    bar = Bar("Running server...", max=1)
    os.system(f"cd server && java -jar {filename}")
    bar.next()
    bar.finish()
