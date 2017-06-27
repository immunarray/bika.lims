# -*- coding: utf-8 -*-
from Products.CMFCore.permissions import ModifyPortalContent
from Products.CMFCore.permissions import ListFolderContents, View
from plone import api
from zope.event import notify

from bika.lims import messagefactory as _
from bika.lims.events import LIMSCreatedEvent
from bika.lims.permissions import *
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.permissions import AddClinicalSample
from immunarray.lims.permissions import AddRandDSample
from immunarray.lims.permissions import AddSite
from immunarray.lims.permissions import AddQCSample

#from immunarray.lims.permissions import AddClincalAliquot

def Added(lims, event):
    """When a new LIMS root is created, we must create it's folder structure
    and do some configuration.

    The order in which items are created here defines the default order
    of the site navigation.

    The permissions set here are inherited by children.
    """

    # Prevent anyone from adding a LIMSRoot inside of a LIMSRoot Allow for all users to see folder
    lims.manage_permission(AddLIMSRoot, [], 0)
    lims.manage_permission(ListFolderContents, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'Administrator', 'Member', 'RandDLabClerk', 'RandDLabManager'], 0)
    lims.manage_permission(View, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'Administrator', 'Member', 'RandDLabClerk', 'RandDLabManager'], 0)

    create_structure(lims)
    structure_permissions(lims)
    notify(LIMSCreatedEvent(lims))


def create_structure(lims):
    for x in [
        [lims, 'Folder', 'sites', _(u"Sites")],
        [lims, 'Folder', 'samples', _(u"Samples")],
        [lims, 'Folder', 'analysisrequests', _(u"Analysis Requests")],
        [lims, 'Folder', 'configuration', _(u"Configuration")],
    ]:
        instance = api.content.create(
            container=x[0], type=x[1], id=x[2], title=x[3])
        instance.setLayout('folder_contents')
        disallow_default_contenttypes(instance)

    configuration = lims.configuration
    for x in [
        # [configuration, 'Laboratory', 'laboratory', _(u"Laboratory")],
        [configuration, 'Folder', 'aliquoting', _(u"Aliquoting")],
        [configuration, 'Folder', 'departments', _(u"Departments")],
        [configuration, 'Folder', 'contacts', _(u"Contacts")],
        [configuration, 'Folder', 'samplepoints', _(u"Sample Points")],
        [configuration, 'Folder', 'sampletypes', _(u"Sample Types")],
        [configuration, 'Folder', 'analysisservices', _(u"Analysis Services")],
        [configuration, 'Folder', 'calculations', _(u"Calculations")],
    ]:
        instance = api.content.create(
            container=x[0], type=x[1], id=x[2], title=x[3])
        instance.setLayout('folder_contents')
        disallow_default_contenttypes(instance)


def structure_permissions(lims):

    #lims/sites (clients)
    mp = lims.sites.manage_permission
    mp(ModifyPortalContent, ['Manager', 'LabManager'], 0)
    mp(AddSite, ['Manager', 'LabManager'], 0)
    mp(View, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'Administrator', 'RandDLabClerk', 'RandDLabManager'], 0)
    mp(permissions.AddFolder, [], 0)

    # lims/samples
    mp = lims.samples.manage_permission
    mp(AddSample, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'RandDLabClerk', 'RandDLabManager'], 0)
    mp(ModifyPortalContent, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'RandDLabClerk', 'RandDLabManager'], 0)
    mp(View, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'RandDLabClerk', 'RandDLabManager'], 0)
    mp(permissions.AddFolder, [], 0)

    # lims/analysisrequests
    mp = lims.analysisrequests.manage_permission
    mp(AddAnalysisRequest, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'RandDLabClerk', 'RandDLabManager'], 0)
    mp(ModifyPortalContent, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'RandDLabClerk', 'RandDLabManager'], 0)
    mp(View, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'Administrator', 'RandDLabClerk', 'RandDLabManager'], 0)
    mp(permissions.AddFolder, [], 0)

    # lims/configuration (folder root)
    mp = lims.configuration.manage_permission
    mp(AddLaboratory, [], 0)
    mp(permissions.AddFolder, [], 0)

    # lims/configuration/departments
    mp = lims.configuration.departments.manage_permission
    mp(AddDepartment, ['Manager', 'LabManager', 'Owner'], 0)
    mp(ModifyPortalContent, ['Manager', 'LabManager', 'Owner'], 0)
    mp(View, ['Manager', 'LabManager', 'LabClerk', 'Owner',], 0)
    mp(permissions.AddFolder, [], 0)

    # lims/configuration/contacts
    mp = lims.configuration.contacts.manage_permission
    mp(AddContact, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    mp(ModifyPortalContent, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    mp(View, ['Manager', 'LabManager', 'LabClerk', 'Owner',], 0)
    mp(permissions.AddFolder, [], 0)

    # lims/configuration/samplepoints
    mp = lims.configuration.samplepoints.manage_permission
    mp(AddSamplePoint, ['Manager', 'LabManager', 'Owner'], 0)
    mp(ModifyPortalContent, ['Manager', 'LabManager', 'Owner'], 0)
    mp(View, ['Manager', 'LabManager', 'LabClerk', 'Owner',], 0)
    mp(permissions.AddFolder, [], 0)

    # lims/configuration/sampletypes
    mp = lims.configuration.sampletypes.manage_permission
    mp(AddSampleType, ['Manager', 'LabManager', 'Owner'], 0)
    mp(ModifyPortalContent, ['Manager', 'LabManager', 'Owner'], 0)
    mp(View, ['Manager', 'LabManager', 'LabClerk', 'Owner',], 0)
    mp(permissions.AddFolder, [], 0)

    # lims/configuration/analysisservices
    mp = lims.configuration.analysisservices.manage_permission
    mp(AddAnalysisService, ['Manager', 'LabManager', 'Owner'], 0)
    mp(ModifyPortalContent, ['Manager', 'LabManager', 'Owner'], 0)
    mp(View, ['Manager', 'LabManager', 'LabClerk', 'Owner',], 0)
    mp(permissions.AddFolder, [], 0)

    # lims/configuration/calculations
    mp = lims.configuration.calculations.manage_permission
    mp(AddCalculation, ['Manager', 'LabManager', 'Owner'], 0)
    mp(ModifyPortalContent, ['Manager', 'LabManager', 'Owner'], 0)
    mp(View, ['Manager', 'LabManager', 'LabClerk', 'Owner',], 0)
    mp(permissions.AddFolder, [], 0)

    # lims/clinicalsamples
    mp = lims.samples.manage_permission
    mp(AddClinicalSample, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    mp(ModifyPortalContent, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    mp(View, ['Manager', 'LabManager', 'LabClerk', 'Owner',], 0)
    mp(permissions.AddFolder, [], 0)

    # lims/R&D samples
    mp = lims.samples.manage_permission
    mp(AddRandDSample, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    mp(ModifyPortalContent, ['Manager', 'LabManager', 'LabClerk', 'Owner','RandDLabClerk', 'RandDLabManager'], 0)
    mp(View, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'RandDLabClerk', 'RandDLabManager'], 0)
    mp(permissions.AddFolder, [], 0)

    # lims/QC samples
    mp = lims.samples.manage_permission
    mp(AddQCSample, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    mp(ModifyPortalContent, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    mp(View, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    mp(permissions.AddFolder, [], 0)

    #lims
    # mp = lims.manage_permission
    # mp(ModifyPortalContent, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'Administrator', 'Member'], 0)
    # mp(ListFolderContents,['Manager', 'LabManager', 'LabClerk', 'Owner', 'Member', 'Administrator'], 0)
    # mp(permissions.AddFolder, [], 0)
