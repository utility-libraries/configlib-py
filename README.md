# config-library
utility library to find and load configuration files

## Installation
`pip install config-library`

## Supported Config-Types
- .json
- .jsonc
- .ini/.conf
- .toml (python3.11+ or `pip3 install config-library[toml]`)
- .yaml (`pip3 install config-library[yaml]`)

## Places to search for

```
/etc/
/home/<user>/
/path/to/git-repo/
/path/to/source/code/
```

And in these folder it searches for either directly the config file or a sub-folder that's named like your project.

## Usage Example

```python
import configlib

config = configlib.findAndLoad('app.conf', 'project')
```
system file-structure
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
