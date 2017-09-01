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


    notify(LIMSCreatedEvent(lims))
