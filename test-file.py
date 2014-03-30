# Copyright (C) 2012 Red Hat, Inc.
# Authors: Jan Kaluza <jkaluza@redhat.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#

import os
import sys
import errno
from subprocess import Popen, PIPE
import pickle
import mimetypes
import difflib
from pyfile import *

# run this only if started as script from command line
if __name__ == '__main__':
	mimetypes.init()

	metadata = get_simple_metadata(sys.argv[1])
	stored_metadata = get_stored_metadata(sys.argv[1])

	if is_regression(stored_metadata, metadata):
		sys.exit(1)
