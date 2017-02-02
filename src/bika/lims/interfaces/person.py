# -*- coding: utf-8 -*-
from zope import schema

from plone.schema import Email
from plone.supermodel import model
from zope.interface import Interface

from bika.lims import messagefactory as _


class IPerson(Interface):
    """All person things
    """
    first_name = schema.TextLine(
        title=_(u"First name"),
        required=True,
    )

    last_name = schema.TextLine(
        title=_(u"Last name"),
        required=False,
    )

    phone_numbers = schema.List(
        title=_(u"Phone numbers"),
        description=_(u"List of contact telephone and fax numbers"),
        value_type=schema.TextLine(),
        unique=True,
        required=False,
    )

    email_address = Email(
        title=_(u"Email address"),
        description=_(u"Email address"),
        required=False,
    )

    job_title = schema.TextLine(
        title=_(u"Job title"),
        required=False,
    )

    model.fieldset('physicaladdress',
                   label=_(u"Physical Address"),
                   fields=['physical_address',
                           'physical_address_cont',
                           'physical_address_city',
                           'physical_address_state',
                           'physical_address_zipcode',
                           'physical_address_country',
                           ]
                   )

    physical_address = schema.TextLine(
        title=_("Physical address"),
        required=False,
    )

    physical_address_cont = schema.TextLine(
        title=_("Physical address continued"),
        required=False,
    )

    physical_address_city = schema.TextLine(
        title=_("Physical address city"),
        required=False,
    )

    physical_address_state = schema.TextLine(
        title=_("Physical address state"),
        required=False,
    )

    physical_address_zipcode = schema.TextLine(
        title=_("Physical address zipcode"),
        required=False,
    )

    physical_address_country = schema.TextLine(
        title=_("Physical address"),
        required=False,
    )

    model.fieldset('postaladdress',
                   label=_(u"Postal Address"),
                   fields=['postal_address',
                           'postal_address_cont',
                           'postal_address_city',
                           'postal_address_state',
                           'postal_address_zipcode',
                           'postal_address_country',
                           ]
                   )
    postal_address = schema.TextLine(
        title=_("Postal address"),
        required=False,
    )

    postal_address_cont = schema.TextLine(
        title=_("Postal address continued"),
        required=False,
    )

    postal_address_city = schema.TextLine(
        title=_("Postal address city"),
        required=False,
    )

    postal_address_state = schema.TextLine(
        title=_("Postal address state"),
        required=False,
    )

    postal_address_zipcode = schema.TextLine(
        title=_("Postal address zipcode"),
        required=False,
    )

    postal_address_country = schema.TextLine(
        title=_("Postal address country"),
        required=False,
    )

    model.fieldset('billingaddress',
                   label=_(u"Billing Address"),
                   fields=['billing_address',
                           'billing_address_cont',
                           'billing_address_city',
                           'billing_address_state',
                           'billing_address_zipcode',
                           'billing_address_country',
                           ]
                   )
    billing_address = schema.TextLine(
        title=_("Billing address"),
        required=False,
    )

    billing_address_cont = schema.TextLine(
        title=_("Billing address continued"),
        required=False,
    )

    billing_address_city = schema.TextLine(
        title=_("Billing address city"),
        required=False,
    )

    billing_address_state = schema.TextLine(
        title=_("Billing address state"),
        required=False,
    )

    billing_address_zipcode = schema.TextLine(
        title=_("Billing address zipcode"),
        required=False,
    )

    billing_address_country = schema.TextLine(
        title=_("Billing address country"),
        required=False,
    )

    model.fieldset('logindetails',
                   label=_(u"Login Details"),
                   fields=['username',
                           'password',
                           ]
                   )

    username = schema.TextLine(
        title=_(u"Username"),
        required=False,
    )

    password = schema.Password(
        title=_(u"Password"),
        required=False,
    )
