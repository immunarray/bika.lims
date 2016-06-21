# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INavigationSchema
from Products.CMFPlone.interfaces import INonInstallable
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.interface import implementer

from bika.lims.permissions import *


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'bika.lims:uninstall',
        ]


def setup_roles(context):
    """Configure roles
    """
    portal = context.getSite()
    if context.readDataFile('bikalims_default.txt') is None:
        return

    prm = portal.acl_users.portal_role_manager
    for role in (
        'LabManager',
        'LabClerk',
        'Analyst',
        'Verifier',
        'Sampler',
        'Preserver',
        'Publisher',
        'Member',
        'Reviewer',
        'RegulatoryInspector',
        'Client'
    ):
        if role not in prm.listRoleIds():
            prm.addRole(role)
        portal._addRole(role)


def setup_groups(context):
    """Configure groups
    """
    portal = context.getSite()
    if context.readDataFile('bikalims_default.txt') is None:
        return

    portal_groups = portal.portal_groups
    groups = portal_groups.listGroupIds()
    addgroup = portal_groups.addGroup
    if 'LabManagers' not in groups:
        addgroup('LabManagers',
                 title="Lab Managers",
                 roles=['Member', 'LabManager', ])
    if 'LabClerks' not in groups:
        addgroup('LabClerks',
                 title="Lab Clerks",
                 roles=['Member', 'LabClerk'])
    if 'Analysts' not in groups:
        addgroup('Analysts',
                 title="Lab Technicians",
                 roles=['Member', 'Analyst'])
    if 'Verifiers' not in groups:
        addgroup('Verifiers',
                 title="Verifiers",
                 roles=['Verifier'])
    if 'Samplers' not in groups:
        addgroup('Samplers',
                 title="Samplers",
                 roles=['Sampler'])
    if 'Preservers' not in groups:
        addgroup('Preservers',
                 title="Preservers",
                 roles=['Preserver'])
    if 'Publishers' not in groups:
        addgroup('Publishers',
                 title="Publishers",
                 roles=['Publisher'])
    if 'Clients' not in groups:
        addgroup('Clients',
                 title="Clients",
                 roles=['Member', 'Client'])
    if 'Suppliers' not in groups:
        addgroup('Suppliers',
                 title="Suppliers",
                 roles=['Member', ])
    if 'RegulatoryInspectors' not in groups:
        addgroup('RegulatoryInspectors',
                 title="Regulatory Inspectors",
                 roles=['Member', 'RegulatoryInspector'])


def setup_permissions(context):
    """Configure roles
    """
    portal = context.getSite()
    if context.readDataFile('bikalims_default.txt') is None:
        return

    mp = portal.manage_permission
    mp(AddLIMSRoot, ['Manager'], 0)
    mp(AddAliquot, [], 0)
    mp(AddAnalysisRequest, [], 0)
    mp(AddClient, [], 0)
    mp(AddContact, [], 0)
    mp(AddDepartment, [], 0)
    mp(AddLaboratory, [], 0)
    mp(AddSample, [], 0)
    mp(AddSamplePoint, [], 0)
    mp(AddSampleType, [], 0)


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('bikalims_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
    pass


def postInstall(context):
    if context.readDataFile('bikalims_default.txt') is None:
        return
    setup_roles(context)
    setup_groups(context)
    setup_permissions(context)

    # Display 'LIMSRoot' objects in the navigation
    registry = getUtility(IRegistry)
    settings = registry.forInterface(INavigationSchema, prefix="plone")
    displayed_types = list(settings.displayed_types)
    if 'LIMSRoot' not in displayed_types:
        displayed_types.append('LIMSRoot')
        settings.displayed_types = tuple(displayed_types)
