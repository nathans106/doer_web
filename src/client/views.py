import datetime
from datetime import date

from django.shortcuts import render

from doer import storage, config
from doer.model import Data

import doer_web


def _day(request, date_: date):
    data = Data(storage.database(), config.context())
    day_ = data.day(date_)
    context = {
        'date': datetime.datetime(date_.year, date_.month, date_.day),
        'day': day_,
        'version': doer_web.__version__,
    }

    return render(request, 'day.html', context)


def day(request, year, month, day):
    return _day(request, datetime.date(year, month, day))


def today(request):
    return _day(request, date.today())
