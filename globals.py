from django.utils.timezone import now, localtime
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from core.utils import getNumEnding
from pytils.translit import slugify

import os.path


def domain(request):
    return (request.is_secure() and 'https://' or 'http://') + str(get_current_site(request).replace('dev.', ''))


def num_ending(integer, words):
    return getNumEnding(integer, words)


MONTHES = {
    '01': {
        'simple': 'Январь',
        'default': 'января',
    },
    '02': {
        'simple': 'Февраль',
        'default': 'февраля',
    },
    '03': {
        'simple': 'Март',
        'default': 'марта',
    },
    '04': {
        'simple': 'Апрель',
        'default': 'апреля',
    },
    '05': {
        'simple': 'Май',
        'default': 'мая',
    },
    '06': {
        'simple': 'Июнь',
        'default': 'июня',
    },
    '07': {
        'simple': 'Июль',
        'default': 'июля',
    },
    '08': {
        'simple': 'Август',
        'default': 'августа',
    },
    '09': {
        'simple': 'Сентябрь',
        'default': 'сентября',
    },
    '10': {
        'simple': 'Октябрь',
        'default': 'октября',
    },
    '11': {
        'simple': 'Ноябрь',
        'default': 'ноября',
    },
    '12': {
        'simple': 'Декабрь',
        'default': 'декабря',
    },
}


def get_date(text=None):

    if not text:
        return localtime(now())

    _localtime = localtime(now())

    now_YEAR = int(_localtime.strftime('%Y'))
    now_day = int(_localtime.strftime('%d'))

    looking_for = localtime(text)
    looking_for_YEAR = int(looking_for.strftime('%Y'))
    looking_for_DAY = int(looking_for.strftime('%d'))

    if looking_for_YEAR == now_YEAR:
        if now_day == looking_for_DAY:
            return '{} в {}'.format(_('сегодня'), looking_for.strftime('%H:%M'))
        if now_day - 1 == looking_for_DAY:
            return '{} в {}'.format(_('вчера'), looking_for.strftime('%H:%M'))

        month = looking_for.strftime('%m')
        return '{} {}, {}'.format(looking_for.strftime('%d'), MONTHES[month]['default'], looking_for.strftime('%H:%M'))

    month = looking_for.strftime('%m')
    return '{} {} {}'.format(looking_for.strftime('%d'), MONTHES[month]['default'], looking_for_YEAR)

    return looking_for.strftime()
