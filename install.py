import json
import os
import argparse
import requests
from progress.bar import Bar

parser = argparse.ArgumentParser(description='Minecraft server installer')

parser.add_argument("--servertype", "-s", dest='serverType', help="Type of the server, ex: spigot, sponge, spongeforge, bukkit, forge, vanilla")
parser.add_argument("--version", "-v", dest="minecraftVersion", help="Minecraft version of the server, ex: 1.12.2")
args = parser.parse_args()

def getLatestVersion():
    return json.loads(requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json").text)["latest"]["release"]
def installVanilla(minecraftVersion):
    print(f"Installing vanilla minecraft server. Version: {minecraftVersion}")
    bar = Bar('Downloading...', max=4)
    for i in json.loads(requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json").text)["versions"]:
        if i["id"] == minecraftVersion:
            minecraftVersionURL = i["url"]
    bar.next()
    serverDownloadURL = json.loads(requests.get(minecraftVersionURL).text)["downloads"]["server"]["url"]
    bar.next()
    filename = serverDownloadURL.rsplit('/', 1)[1]
    open(filename, "wb").write(requests.get(serverDownloadURL).content)
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
    print("Server successfully installed. To start your server later, run java -jar server/server.jar")

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
    installVanilla(minecraftVersion)
