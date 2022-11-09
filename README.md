# py-config-lib
utility library to find and load configuration files


# Usage Example

```python
import config_lib

config = config_lib.findAndLoad('app.conf', 'project')
```
project-structure
```
/
├─ etc/
├─ home/user/
│  ├─ path/to/repo/
│  │  ├─ src/code/
│  │  │  ├─ main.py
│  ├─ .config/
```
places to search for the config-file
- /home/user/path/to/repo/src/code/app.conf
- /home/user/path/to/repo/src/code/project/app.conf
- /home/user/path/to/repo/app.conf
- /home/user/path/to/repo/project/app.conf
- /home/user/.config/app.conf
- /home/user/.config/project/app.conf
- /etc/app.conf
- /etc/project/app.conf

# Supported Config-Types
- .json
- .ini/.conf
- .toml (python3.11+)
