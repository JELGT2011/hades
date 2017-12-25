
## Getting Started

```bash
make env
source env/bin/activate
make bootstrap
```

```bash
echo "$USER $HOST = (root) NOPASSWD: `which python`" >>! /etc/sudoers.d/python 
```

create a file in the virtualenv called `env/bin/python_sudo.sh`
```bash
#!/bin/bash
sudo `which python` "$@"
```

make it executable
```bash
chmod +x env/bin/python_sudo.sh
```

alias it
```bash
alias sudopy=env/bin/python_sudo.sh
```
