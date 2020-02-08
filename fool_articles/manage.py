#!/usr/bin/env python
import env_file
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fool_articles.settings')
    env_file.load()
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
