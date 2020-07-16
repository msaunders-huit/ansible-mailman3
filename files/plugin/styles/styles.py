# Copyright (C) 2007-2020 by the Free Software Foundation, Inc.
#
# Portions of this file are part of GNU Mailman.
#
# GNU Mailman is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# GNU Mailman is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# GNU Mailman.  If not, see <https://www.gnu.org/licenses/>.

"""Custom of list styles for new and existing lists."""

from mailman.core.i18n import _
from mailman.interfaces.styles import IStyle
from mailman.interfaces.action import Action
from mailman.styles.base import (
    Announcement, BasicOperation, Bounces, Discussion, Identity, Moderation,
    Private, Public)
from public import public
from zope.interface import implementer

@public
@implementer(IStyle)
class PrivateCustomStyle(
        Identity, BasicOperation, Bounces, Private, Discussion, Moderation):

    """Style for mailing-lists with private archives."""

    name = 'private-custom'
    description = _('Hidden discussion mailing list style with private archives, customized by CCS')

    def apply(self, mailing_list):
        """See `IStyle`."""
        Identity.apply(self, mailing_list)
        BasicOperation.apply(self, mailing_list)
        Bounces.apply(self, mailing_list)
        Private.apply(self, mailing_list)
        Discussion.apply(self, mailing_list)
        Moderation.apply(self, mailing_list)
        mlist = mailing_list
        mlist.advertised = False
        mlist.default_member_action = Action.hold
        mlist.digest_send_periodic = False
        mlist.max_num_recipients = 0
        mlist.max_message_size = 0               # KB, 0 disables check
        