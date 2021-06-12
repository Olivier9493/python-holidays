# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, FEB, MAR, MAY, AUG, SEP, NOV, DEC
from holidays.holiday_base import HolidayBase

class Liechtenstein(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Liechtenstein
    """
    This class returns the holidays for Liechtenstein (LI/LIE/FL)
    Even if the country is pretty small, the following date aren't offical holidays
    but only for some branches (Bankfeiertag) and mainly not worked
   - "Berchtoldstag" : Jan 2nd (Saint Berchtold's Day)
   - "Fasnachtsdienstag" : 47 days before Easter (Carnival - Shrove Tuesday)
   - "Karfreitag" : Friday before Easter
   - "Heiliger Abend"  : Dec 24th (Christmas Eve)
    """

    def __init__(self, **kwargs):
        self.country = "LI"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, JAN, 1)] = "Neujahr"
        self[date(year, JAN, 2)] = "Berchtoldstag"
        self[date(year, JAN, 6)] = "Heilige Drei König"
        self[date(year, FEB, 2)] = "Lichtmess"
        self[date(year, MAR, 19)] = "Joseftag"
        self[easter(year) - rd(days=-47)] = "Fasnachtsdienstag"
        self[easter(year) - rd(days=2)] = "Karfreitag"
        self[easter(year)] = "Ostersonntag"
        self[easter(year) + rd(days=1)] = "Ostermontag"
        self[date(year, MAY, 1)] = "Tag der Arbeit"
        self[easter(year) + rd(days=39)] = "Christi Himmelfahrt"
        self[easter(year) + rd(days=49)] = "Pfingsten"
        self[easter(year) + rd(days=50)] = "Pfingstmontag"
        self[easter(year) + rd(days=60)] = "Fronleichnam"
        self[date(year, AUG, 15)] = "Staatsfeiertag"
        self[date(year, SEP, 8)] = "Mariä Geburt"
        self[date(year, NOV, 1)] = "Allerheiligen"
        self[date(year, DEC, 8)] = "Mariä Empfängnis"
        self[date(year, DEC, 24)] = "Heiliger Abend"
        self[date(year, DEC, 25)] = "Weihnachten"
        self[date(year, DEC, 26)] = "Stephanstag"

class LIE(Liechtenstein):
    pass

class FL(Liechtenstein):
    pass