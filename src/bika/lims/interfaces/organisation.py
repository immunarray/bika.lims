# -*- coding: utf-8 -*-
from zope import schema

from bika.lims import messagefactory as _
from plone.schema import Email
from plone.supermodel import model


class IOrganisation(model.Schema):
    """Base fields for all organisation types
    """

    phone_number = schema.TextLine(
        title=_(u"Phone number"),
        required=False,
    )

    email_address = Email(
        title=_(u"Email address"),
        required=False,
    )

    website = schema.URI(
        title=_(u"Website"),
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
        title=_("Physical address country"),
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

    physical_address = schema.Text(
        title=_(u"Physical address"),
        required=False,
    )

    postal_address = schema.Text(
        title=_(u"Postal address"),
        required=False,
    )

    billing_address = schema.Text(
        title=_(u"Billing address"),
        required=False,
    )

    model.fieldset('banking',
                   label=_(u"Banking details"),
                   fields=['account_type',
                           'account_name',
                           'account_number',
                           'bank_name',
                           'bank_branch',
                           'swift_code',
                           'tax_number',
                           ]
                   )

    account_type = schema.TextLine(
        title=_(u"Account type"),
        required=False,
    )

    account_name = schema.TextLine(
        title=_(u"Account name"),
        required=False,
    )

    account_number = schema.TextLine(
        title=_(u"Account number"),
        required=False,
    )

    bank_name = schema.TextLine(
        title=_(u"Bank name"),
        required=False,
    )

    bank_branch = schema.TextLine(
        title=_(u"Bank branch"),
        required=False,
    )

    swift_code = schema.TextLine(
        title=_(u"SWIFT code"),
        required=False,
    )

    tax_number = schema.TextLine(
        title=_(u"Tax number"),
        required=False,
    )
