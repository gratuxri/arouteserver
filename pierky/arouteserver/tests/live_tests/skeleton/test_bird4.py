# Copyright (C) 2017 Pier Carlo Chiodi
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

from base import SkeletonScenario
from pierky.arouteserver.tests.live_tests.bird import BIRDInstanceIPv4

class SkeletonScenario_BIRDIPv4(SkeletonScenario):
    __test__ = True

    SHORT_DESCR = "Live test, BIRD, skeleton, IPv4"
    RS_INSTANCE_CLASS = BIRDInstanceIPv4
    CLIENT_INSTANCE_CLASS = BIRDInstanceIPv4
    IP_VER = 4

    DATA = {
        "rs_IPAddress":             "99.0.2.2",
        "AS1_IPAddress":            "99.0.2.11",
        "AS2_IPAddress":            "99.0.2.22",

        "AS2_prefix1":              "2.0.1.0/24"
    }