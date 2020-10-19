# plat.py
#
# Illustrate platform library
# Careful not to call this program  platform.py
#     would 'pollute namespace' -
#     We'd be unable to import platform
#
# Usage:
#      % python plat.py
#
# Jeff Parker, June 2018

import platform


print('Ver:  ', platform.python_version())
print('Build:', platform.python_build())
