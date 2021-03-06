from os import close
import click
import chevron
# from commands import cb_init
# from utils import string_utils

# init_manager = cb_init.CrystalBallInitializeManager()
# str_utils = string_utils.StringUtils()

@click.group()
def cli():
    """
    Crystal Ball is a Command Line Interface tool that can be used to setup 
    easy to use monitoring for basic health checks for your system
    """
    pass


@cli.command()
@click.argument('name')
@click.option('--format', '-f',
                prompt= 'Please enter your preferred format (yaml/json)', 
                help='Preferred format to generate the project definition file')
def init(name: str = None, format: str = "yaml"):
    if name and name.strip() and len(name) > 0: 
        click.echo(f"Initializing {name}!")
    else:
        name = click.prompt("Please give your project a name")
        click.echo(f"Initializing {name}!")

    if format == "yaml":
        with open('./mustache/project-definition-yaml.mustache') as yaml:
            yaml_str = yaml.readlines()
            project_def_yaml = chevron.render(yaml_str, { 'name': 'test' })
            click.echo(project_def_yaml)
            close()
    elif format == "json":
        with open('./mustache/project-definition-json.mustache') as json:
            json_str = json.readlines()
            project_def_json = chevron.render(json_str, { 'name': 'test' })
            click.echo(project_def_json)
            close()
    else:
        click.echo('POOP')
    
# @app.command()
# def execute(project_name: str = None)

if __name__ == "__main__":
    cli()