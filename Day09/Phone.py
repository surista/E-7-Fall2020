#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Module documentation goes here
"""


class Phone:
    "A Class defining valid Phone Numbers"

    def __init__(self, raw):
        "Create new instance"
        self.number = self._normalize(raw)

    def __str__(self) -> str:
        "Create printable representation"
        return '('+self.number[0:3]+') '+self.number[3:6]+'-'+self.number[6:10]

    def area_code(self) -> str:
        "Return the area code"
        return self.number[0:3]

    def _normalize(self, raw: str) -> str:
        """"Take string presented and return string with digits
            Throws a ValueError Exception if not a NANP number"""
        pnumber = ''.join([char for char in raw if char.isdigit()])
        if len(pnumber) == 11 and pnumber[0] != '1':
            raise ValueError("invalid country code")
        if pnumber[0] == '1':
            pnumber = pnumber[1:]
        if len(pnumber) > 10:
            raise ValueError("invalid - too many digits")
        if len(pnumber) < 10:
            raise ValueError("invalid - too few digits")
        if pnumber[0] < '2':
            raise ValueError("invalid area code")
        if pnumber[3] < '2':
            raise ValueError("invalid exchange code")
        return pnumber


def test_phone():
    p = Phone('+1 (617) 495-4024')
    assert (p.__str__() == '(617) 495-4024')

    p = Phone('617-495-4024')
    assert (p.__str__() == '(617) 495-4024')

    p = Phone('1 617 495 4024')
    assert (p.__str__() == '(617) 495-4024')

    p = Phone('617.495.4024')
    assert (p.__str__() == '(617) 495-4024')
    assert (p.area_code() == '617')

    p = Phone('+1 (508) 495  4024')
    assert (p.__str__() == '(508) 495-4024')

    p = Phone('508 - 495 - 4024')
    assert (p.__str__() == '(508) 495-4024')

    p = Phone('1 508 (495) [4024]')
    assert (p.__str__() == '(508) 495-4024')

    p = Phone('508!495?4024')
    assert (p.__str__() == '(508) 495-4024')
    assert (p.area_code() == '508')

    print("Success!")


test_phone()