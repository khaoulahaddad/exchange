import threading    
import time 

from schedule import Scheduler

from alpha_vantage.foreignexchange import ForeignExchange
from exchange.settings import ALPHAKEY
from .models import ExchangeRate

class Worker(Scheduler):
    def exchange(self):
        cc = ForeignExchange(key=ALPHAKEY)
        # There is no metadata in this call
        data, meta_data = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
        print(data)

        rate = ExchangeRate.objects.create(
            from_currency= data['1. From_Currency Code'],
            to_currency=  data['3. To_Currency Code'],
            value =  data['5. Exchange Rate'], 
            last_refresh =  data['6. Last Refreshed']
        )
        rate.save()
    def run_continuously(self, interval=1):

        cease_continuous_run = threading.Event()

        class ScheduleThread(threading.Thread):

            @classmethod
            def run(cls):
                while not cease_continuous_run.is_set():
                    self.exchange()
                    self.run_pending()
                    time.sleep(interval)

        continuous_thread = ScheduleThread()
        continuous_thread.setDaemon(True)
        continuous_thread.start()
        return cease_continuous_run

    Scheduler.run_continuously = run_continuously



