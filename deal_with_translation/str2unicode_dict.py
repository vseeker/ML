# encoding=utf-8
from django.utils.translation import ugettext_lazy as _



# "Cannot handle subnet of type(.*)": _("Cannot handle subnet of type %(subnet_type)s"),
# 这是我们要的格式,前面是模版但必须是unicode,因为我们要用re的unicode来进行匹配
dict_regex_and_str = {
    u"Cannot handle subnet of type(.*)": _("Cannot handle subnet of type %(subnet_type)s"),
    u"Unknown address type (.*)": _("Unknown address type %(address_type)s"),
    u"IP address (.*) already allocated in subnet (.*)": _("IP address %(ip)s already allocated in subnet %(subnet_id)s"),
    u"IP address (.*) does not belong to subnet (.*)": _("IP address %(ip)s does not belong to subnet %(subnet_id)s"),
    u"The address allocation request could not be satisfied because: (.*)": _("The address allocation request could not be satisfied because: %(reason)s"),
    u"The subnet request could not be satisfied because: (.*)": _("The subnet request could not be satisfied because: %(reason)s"),
    u'Invalid input for operation: Requested subnet with cidr:(.*) for network: (.*) overlaps with another subnet.': _('Invalid input for operation: Requested subnet with cidr:(%cidr)sfor network: (network_id)s overlaps with another subnet.  ')
}


