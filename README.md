# config-library
utility library to find and load configuration files


# Installation
`pip install config-library`

# Usage Example

```python
import configs

config = configs.findAndLoad('app.conf', 'project')
```
file-structure
```
/
├─ etc/
├─ home/user/
│  ├─ path/to/repo/
│  │  ├─ src/code/
│  │  │  ├─ main.py
│  ├─ .config/
```
places where `config-library` searches for the config-file
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
- .yaml (if `pyyaml` is installed)
