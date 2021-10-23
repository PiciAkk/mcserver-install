# mcserver-install
Simple install script for minecraft servers

*Disclaimer: currently only supports vanilla minecraft servers*

## Usage

1. Clone this repository
```bash
git clone https://github.com/piciakk/mcserver-install
```
2. Go to the cloned repo
```bash
cd mcserver-install
```
3. Install Java (or OpenJDK), if you haven't already done that
4. Install the dependencies
```bash
pip install -r requirements.txt
``` 
5. Run the installer
```bash
python install.py -v 1.12.2 -s vanilla
```

*Arguments:*

`-v`: minecraft server version to install (latest by default)

`-s`: minecraft server type (vanilla by default)

`-h`: display help page

## Removing the server

```bash
python remove.py
```

## Using as library

```python
import install # import the install.py library

install.getLatestVersion() # returns latest minecraft version

install.installServer(servertype, serverversion)
# servertype can be vanilla, bukkit, sponge, etc.
# serverversion can be any minecraft version (that you can use in the launcher)

install.removeServer() # remove the server directory
```
