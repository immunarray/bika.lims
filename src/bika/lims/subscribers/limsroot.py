# -*- coding: utf-8 -*-
from Products.CMFCore.permissions import ListFolderContents, View
from bika.lims.events import LIMSCreatedEvent
from bika.lims.permissions import *
from zope.event import notify


# from immunarray.lims.permissions import AddClincalAliquot

def Added(lims, event):
    """When a new LIMS root is created, we must create it's folder structure
    and do some configuration.

    The order in which items are created here defines the default order
    of the site navigation.

    The permissions set here are inherited by children.
    """

    # Prevent anyone from adding a LIMSRoot inside of a LIMSRoot Allow for
    # all users to see folder
    # @formatter:off
    lims.manage_permission(AddLIMSRoot, [], 0)
    lims.manage_permission(ListFolderContents, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'Administrator', 'Member', 'RandDLabClerk', 'RandDLabManager'], 0)
    lims.manage_permission(View, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'Administrator', 'Member', 'RandDLabClerk', 'RandDLabManager'], 0)
    # @formatter:on

    notify(LIMSCreatedEvent(lims))
