from django.db import models
from products.models.product import Product
from .bid import Bid
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
import schedule
import time
import threading
from django.conf import settings
from django.core.mail import send_mail


class Auction(models.Model):
    STATUS_EXPIRED = "SE"
    STATUS_APPROVED = "SA"
    STATUS_PENDING = "SP"

    STATUS_CHOICES = [

        (STATUS_EXPIRED, "Expired"),
        (STATUS_APPROVED, "Approved"),
        (STATUS_PENDING, "Pending"),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_bids = models.IntegerField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(
    max_length=2, choices=STATUS_CHOICES, default=STATUS_PENDING)

    def __str__(self):
      return self.product.title

    @staticmethod
    def number_of_auctions():
      return Auction.objects.all().count()


    @staticmethod
    def get_all_auctions():
        return Auction.objects.all()

    @staticmethod
    def get_auction_by_id(id):
        return Auction.objects.filter(id=id)

    @staticmethod
    def get_auction_by_product_user(id):
        return Auction.objects.filter(product__auctionuser__id=id)

    @staticmethod
    def get_auctions_by_category(category_id):
      if (category_id):
        return Auction.objects.filter(product__category__id=category_id)
      else:
          return Auction.get_all_auctions()


@receiver(post_save, sender=Auction)
def set_expiry(sender,instance,created,**kwargs):
   if created:
     end_date = instance.end_time
     time_now = datetime.datetime.now()-datetime.timedelta(hours=-5)
     timesince =  end_date-time_now
     minutessince = int(timesince.total_seconds() / 60)
     schedule.every(minutessince).minutes.do(expiry_job, instance=instance)
     time.sleep(1)

def expiry_job(instance):
    print("Executing Job now")
    instance.status = "SE"
    product_id = instance.product.id
    product = Product.get_product_by_id(product_id).first()
    product.status = "SS"
    max_bid,winner= Bid.get_auction_winner(instance.id)
    product.owner = winner
    subject = 'Congratulations on Winning'
    message = f'Hi {winner.username}, I am pleased to inform you that you have won the product {product.title} in an auction.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [winner.email, ]
    send_mail( subject, message, email_from, recipient_list )
    instance.save()
    product.save()
    return schedule.CancelJob




class Thread(object):
    def __init__(self, interval=10):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(self.interval)

thread = Thread()
