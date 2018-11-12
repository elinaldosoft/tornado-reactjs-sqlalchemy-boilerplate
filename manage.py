#!/usr/bin/env python
# from importlib import import_module
import argparse
import subprocess


def runserver(args):
    subprocess.run(["python", "server.py"])


def makemigrations(args):
    subprocess.run(["alembic", "revision", "--autogenerate"])


def migrate(args):
    subprocess.run(["alembic", "upgrade", "head"])


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# Run server
runserver_parser = subparsers.add_parser("runserver")
runserver_parser.set_defaults(func=runserver)
# Run migrations
migrate_parser = subparsers.add_parser("migrate")
migrate_parser.set_defaults(func=migrate)
# Run makemigrations prepare migrate
makemigrations_parser = subparsers.add_parser("makemigrations")
makemigrations_parser.set_defaults(func=makemigrations)


if __name__ == "__main__":
    args = parser.parse_args()
    args.func(args)  # call the default function
