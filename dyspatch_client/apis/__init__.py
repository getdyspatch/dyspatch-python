
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.drafts_api import DraftsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from dyspatch_client.api.drafts_api import DraftsApi
from dyspatch_client.api.localizations_api import LocalizationsApi
from dyspatch_client.api.templates_api import TemplatesApi
