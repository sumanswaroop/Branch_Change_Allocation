#!/usr/bin/env python3
import os
import sys
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "branchchange.settings")
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
