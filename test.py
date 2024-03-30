from datetime import datetime
from A2 import *
def test():
    artwork = Artwork("Napoleon Crossing the Alps","Jacques-Louis David",
                      "1801 - 1805", "Iconic portrait", "Hall A")
    assert artwork.get_title()=="Napoleon Crossing the Alps"
    assert artwork.get_artist()=="Jacques-Louis David"
    assert artwork.get_date()=="1801 - 1805"
    assert artwork.get_sign()=="Iconic portrait"
    assert artwork.get_location()=="Hall A"
    print("Adding artwork: Successful")

def open():
    start=datetime(2024, 3,26)
    end=datetime(2024, 7, 21)
    exhibition = Exhibition("From Kalila wa Dimna to La Fontaine", start,
                            end, Location("Exhibition Hall", "Temporary"))
    assert exhibition.get_title()=="From Kalila wa Dimna to La Fontaine"
    assert exhibition.get_start()==start
    assert exhibition.get_end()==end
    assert exhibition.get_location().get_name()=="Exhibition Hall"
    assert exhibition.get_location().get_type()=="Temporary"
    print("Open exhibition: Successful")

def purchase():
    visitor= Visitor("Reem Al Shaabi",30,"35782226")
    event = Exhibition("From Kalila wa Dimna to La Fontaine",datetime(2024,3,26),
                       datetime(2024, 7, 21),
                       Location("Exhibition Hall","Temporary"))
    ticket = Ticket ("T022",63.00,visitor,event)
    assert ticket.get_id()=="T022"
    assert ticket.get_price()==63.00
    assert ticket.get_visitor().get_name()=="Reem Al Shaabi"
    assert ticket.get_event().get_title()=="From Kalila wa Dimna to La Fontaine"
    print("Purchase Ticket: Successful")

def display():
    visitor = Visitor("Reem Al Shaabi", 25,"8398232")
    event = SpecialEvent("Under the Stars", "2 hours",
                         Location("Hall B - dark room", "Temporary"))
    ticket = Ticket("T023", 100.00, visitor, event)
    recepit = (f"Ticket ID: {ticket.get_id()}\nVisitor:{ticket.get_visitor().get_name()}/n"
               f"Age:{ticket.get_visitor().get_age()}\n"
               f"Event:{ticket.get_event().get_title()}\n"
               f"Price:{ticket.get_price()} AED")
    print(recepit)