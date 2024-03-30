class Artwork:
    def __init__ (self, title, artist,date, sign, location):
        self._title = title
        self._artist = artist
        self._date = date
        self._sign = sign
        self._location = location

    #getter and setters for all
    def get_title (self):
        return self._title

    def set_title (self, title):
        self._title = title

    def get_artist (self):
        return self._artist

    def set_artist (self, artist):
        self._artist = artist

    def get_date (self):
        return self._date

    def set_date (self, date):
        self._date = date

    def get_sign (self):
        return self._sign

    def set_sign (self, sign):
        self._sign = sign

    def get_location (self):
        return self._location

    def set_location (self, location):
        self._location = location

from datetime import datetime

class Exhibition:
    def __init__ (self, title, start, end, location):
        self._title = title
        self._start = start
        self._end = end
        self._location = location

    # getter and setters for all
    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_start(self):
        return self._start

    def set_start(self, start):
        self._start = start

    def get_end(self):
        return self._end

    def set_end(self, end):
        self._end = end

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

class Location:
    def __init__(self, name, type):
        self._name = name
        self._type = type

    #getter and setters for all
    def get_name (self):
        return self._name

    def set_name (self, name):
        self._name = name

    def get_type (self):
        return self._type

    def set_type (self, type):
        self._type = type

class Visitor:
    def __init__ (self, name, age, nationalID):
        self._name = name
        self._age = age
        self._nationalID = nationalID
        self._ticketHis = []

    # getter and setters for all
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_nationalID(self):
        return self._nationalID

    def set_nationalID(self, nationalID):
        self._nationalID = nationalID

    def get_ticketHis(self):
        return self._ticketHis

    def add_ticketHis(self, ticket):
        self._ticketHis.append(ticket)

class Ticket:
    def __init__(self, id, price, visitor, event):
        self.id = id
        self.price = price
        self.visitor = visitor
        self.event = event

    # getter and setters for all
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_visitor(self):
        return self._visitor

    def set_visitor(self, visitor):
        self._visitor = visitor

    def get_event(self):
        return self._event

    def set_event(self, event):
        self._event = event

    def calc(self):
        base = self._event.get_price() if isinstance(self._event, SpecialEvent) else 63.00
        if self._visitor.get_age() < 18 or self._visitor.get_age() >= 60 or isinstance(self._visitor, Teacher) or isinstance(self._visitor, Student):
            return 0  # The ticket will be free
        elif isinstance(self._visitor, Group):
            return base * 0.5  # 50% discount for groups
        else:
            return base

    def vet (self, price):
        return price * 1.05 #5% VAT

class SpecialEvent:
    def __init__(self, title, duration, location):
        self.title = title
        self.duration = duration
        self.location = location

    # getter and setters for all
    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        self._duration = duration

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location