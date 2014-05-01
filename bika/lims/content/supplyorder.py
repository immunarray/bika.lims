from AccessControl import ClassSecurityInfo
from bika.lims import bikaMessageFactory as _
from bika.lims.browser.widgets import DateTimeWidget
from bika.lims.config import PROJECTNAME
from bika.lims.content.bikaschema import BikaSchema
from bika.lims.interfaces import ISupplyOrder
from DateTime import DateTime
from Products.Archetypes import atapi
from Products.Archetypes.public import *
from Products.Archetypes.references import HoldingReference
from Products.CMFCore.permissions import View
from Products.CMFPlone.interfaces import IConstrainTypes
from Products.CMFPlone.utils import safe_unicode
from zope.component import getAdapter
from zope.interface import implements

import sys

schema = BikaSchema.copy() + Schema((
    ReferenceField(
      'Contact',
      required=1,
      vocabulary='getContacts',
      default_method='getContactUIDForUser',
      vocabulary_display_path_bound=sys.maxsize,
      allowed_types=('Contact',),
      referenceClass=HoldingReference,
      relationship='SupplyOrderContact',
      widget=ReferenceWidget(
        render_own_label=True,
      ),
    ),
    StringField('OrderNumber',
                required=1,
                searchable=True,
                widget=StringWidget(
                    label=_("Order Number"),
                    ),
                ),
    ReferenceField('Invoice',
                   vocabulary_display_path_bound=sys.maxsize,
                   allowed_types=('Invoice',),
                   referenceClass=HoldingReference,
                   relationship='OrderInvoice',
                   ),
    DateTimeField(
      'OrderDate',
      required=1,
      default_method='current_date',
      widget=DateTimeWidget(
        label=_("Order Date"),
        size=12,
        render_own_label=True,
        visible={
          'edit': 'visible',
          'view': 'visible',
          'add': 'visible',
          'secondary': 'invisible'
        },
      ),
    ),
    DateTimeField('DateDispatched',
                  widget=DateTimeWidget(
                      label=_("Date Dispatched"),
                      ),
                  ),
    TextField('Remarks',
        searchable=True,
        default_content_type='text/plain',
        allowed_content_types=('text/plain', ),
        default_output_type="text/plain",
        widget = TextAreaWidget(
            macro="bika_widgets/remarks",
            label=_('Remarks'),
            append_only=True,
        ),
    ),
    ComputedField('ClientUID',
                  expression = 'here.aq_parent.UID()',
                  widget = ComputedWidget(
                      visible=False,
                      ),
                  ),
    ComputedField('ProductUID',
                  expression = 'context.getProductUIDs()',
                  widget = ComputedWidget(
                      visible=False,
                      ),
                  ),
),
)

schema['title'].required = False


class SupplyOrder(BaseFolder):

    implements(ISupplyOrder, IConstrainTypes)

    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        from bika.lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    def getInvoiced(self):
        if self.getInvoice():
            return True
        else:
            return False

    def Title(self):
        """ Return the OrderNumber as title """
        return safe_unicode(self.getOrderNumber()).encode('utf-8')

    def getOrderNumber(self):
        return safe_unicode(self.getId()).encode('utf-8')

    def getContacts(self):
        adapter = getAdapter(self.aq_parent, name='getContacts')
        return adapter()

    security.declarePublic('getContactUIDForUser')

    def getContactUIDForUser(self):
        """ get the UID of the contact associated with the authenticated
            user
        """
        user = self.REQUEST.AUTHENTICATED_USER
        user_id = user.getUserName()
        r = self.portal_catalog(
            portal_type='Contact',
            getUsername=user_id
        )
        if len(r) == 1:
            return r[0].UID

    security.declareProtected(View, 'getTotalQty')

    def getTotalQty(self):
        """ Compute total qty """
        return sum(
            [obj.getQuantity()
             for obj in self.objectValues('SupplyOrderItem')])

    security.declareProtected(View, 'getSubtotal')

    def getSubtotal(self):
        """ Compute Subtotal """
        return sum(
            [float(obj.getTotal())
             for obj in self.objectValues('SupplyOrderItem')])

    security.declareProtected(View, 'getVAT')

    def getVATTotal(self):
        """ Compute VAT """
        return self.getTotal() - self.getSubtotal()

    security.declareProtected(View, 'getTotal')

    def getTotal(self):
        """ Compute TotalPrice """
        return sum(
            [float(obj.getTotalIncludingVAT())
             for obj in self.objectValues('SupplyOrderItem')])

    def workflow_script_dispatch(self):
        """ dispatch order """
        self.setDateDispatched(DateTime())
        self.reindexObject()

    security.declareProtected(View, 'getProductUIDs')

    def getProductUIDs(self):
        """ return the uids of the products referenced by order items
        """
        uids = []
        for orderitem in self.objectValues('SupplyOrderItem'):
            product = orderitem.getProduct()
            if product is not None:
                uids.append(orderitem.getProduct().UID())
        return uids

    security.declarePublic('current_date')

    def current_date(self):
        """ return current date """
        return DateTime()


atapi.registerType(SupplyOrder, PROJECTNAME)
