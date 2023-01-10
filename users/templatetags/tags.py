from django import template
register = template.Library()
import time
import datetime

def countdown(t):
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1


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

@register.filter('new_bid_amount')
def new_bid_amount(bid_amount):
    return bid_amount + (20 * bid_amount/100)

