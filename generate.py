import os
import click
import pathlib
from dotenv import load_dotenv

@click.command()
@click.option('--name', '-n', multiple=True, help="Add all .yml files inside of folder /composes/${name}")



def cli(name):
    """Run generate requests"""
    load_dotenv(".env")
    
    defaultPath = pathlib.Path(__file__).parent.absolute()
    
    showInfo("Gerando docker-compose para os seguintes serviços:", 'green')

    finalFile = createCompose()

    if (os.environ['PRE_FILENAME']):
        finalFile.writelines(readFileContent(str(defaultPath) + '/' + os.environ['BASEDIR_COMPOSES'] + '/'+ os.environ['PRE_FILENAME']))

    servicesLoaded = []

    for serviceName in name:

        dirToScan = pathlib.Path(str(defaultPath) + '/' + os.environ['BASEDIR_COMPOSES'] + '/' + serviceName)
        composePartList = listFilesInDir(dirToScan)
        composePartList.sort()

        for part in composePartList:
            fileName = part.split('/').pop()

            if fileName not in servicesLoaded:
                finalFile.write('\n')
                if '_' not in fileName:#unique part
                    finalFile.writelines(readFileContent(part))
                else:#generic part
                    genericFileName = fileName.split('_')[0]
                    finalFile.writelines(readFileContent(str(defaultPath) + '/' + os.environ['BASEDIR_COMPOSES'] + '/' + genericFileName + '.yml'))
                    
                servicesLoaded.append(fileName)

    
    if (os.environ['POS_FILENAME']):
        finalFile.write('\n')
        finalFile.writelines(readFileContent(str(defaultPath) + '/' + os.environ['BASEDIR_COMPOSES'] + '/'+ os.environ['POS_FILENAME']))

    showInfo(servicesLoaded)
    showInfo("Arquivo gerado", 'yellow')
    
def showInfo(text, color = ''):
    click.echo(click.style(text, fg=color))

def createCompose():
    return open(os.environ['PATH_FINALFILE'] + 'docker-compose.yml', 'w')

def readFileContent(fileName):
    return open(fileName).readlines()

def listFilesInDir(path):
    return [os.path.join(p, file) for p, _, files in os.walk(os.path.abspath(path)) for file in files]