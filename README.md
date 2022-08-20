# dockerComposeGenerate
Organize and generate large docker-compose files

## Instalation

### Requirements

 - Python 3
 - PIP

### Instalation

```bash
pip install -r requirements.txt
pip install --editable .
```

## Usage

### Configuration

Create a `.env` file:
```
BASEDIR_COMPOSES=composes-sample
PRE_FILENAME=base.yml
POS_FILENAME=volumes.yml
PATH_FINALFILE=
```

### Running

```bash
generate --help
```

```
Usage: generate [OPTIONS]

  Run generate names

Options:
  -n, --name        Add all .yml files inside of folder ${BASEDIR_COMPOSES}/${name}
  --help            Show this message and exit.
```

### Example
```bash
generate -n elastic
```

a docker-compose.yml has be generated inside ${PATH_FINALFILE}