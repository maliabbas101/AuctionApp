from django import template
register = template.Library()


@register.filter('is_admin')
def is_admin(string):
    if str(string) == 'admin':
        return True
    return False

@register.filter('is_buyer')
def is_buyer(string):
    if str(string) == 'buyer':
        return True
    return False

@register.filter('is_seller')
def is_seller(string):
    if str(string) == 'seller':
        return True
    return False

@register.filter('is_owner')
def is_owner(string1, string2):
    if str(string1) == str(string2):
        return True
    return False

@register.filter('is_pending')
def is_pending(string):
    if str(string) == 'SP':
        return True
    return False

@register.filter('is_approved')
def is_approved(string):
    if str(string) == 'SP' or str(string) == 'SE':
        return False
    return True

@register.filter('new_bid_amount')
def new_bid_amount(bid_amount):
    return bid_amount + (20 * bid_amount/100)

