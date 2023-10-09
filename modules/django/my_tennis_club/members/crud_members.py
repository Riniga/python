"""
    py manage.py shell
"""
from models import Member

def Create():
    member = Member(firstname='Emil', lastname='Refsnes')
    member.save()

def Read():
    print(Member.objects.all().values())

def Update():
    x = Member.objects.all()[4]
    x.firstname = "Stalikken"
    x.save()

def Delete():
    x = Member.objects.all()[5]
    x.delete()