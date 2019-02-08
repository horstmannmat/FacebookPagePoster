# FacebookPagePoster
# This file is part of the Spotted UFPR 3.0 bot distribution (https://github.com/horstmannmat/spottedPoster).
# Copyright (C) 2019 Matheus Horstmann
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

TESTING = False

try:
    with open('credentials.txt', 'r') as f:
        EMAIL = f.readline().rstrip()
        PASSWORD = f.readline().rstrip()
except FileNotFoundError:
        EMAIL = ""
        PASSWORD = ""

        # Keep preset values
