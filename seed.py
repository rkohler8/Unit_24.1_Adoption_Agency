"""Seed file to make sample data for db."""

from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()


Pet.query.delete()
# EmployeeProject.query.delete()
# Employee.query.delete()
# Department.query.delete()
# Project.query.delete()

# Add sample Petss
pet1 = Pet(name='Toby', species='Dog', age='13', photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Labrador_Retriever_portrait.jpg/1200px-Labrador_Retriever_portrait.jpg", notes='Toberski', available=False)
pet2 = Pet(name='Jeffery', species='Cat', age='12', photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/1200px-Cat_November_2010-1a.jpg", notes='Jeff', available=True)
pet3 = Pet(name='Brandy', species='Dog', age='12', available=True)
pet4 = Pet(name='Koda', species='Dog', age='2', photo_url="https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg", available=True)

db.session.add_all([pet1, pet2, pet3, pet4])
db.session.commit()


# df = Department(dept_code='fin', dept_name='Finance', phone='555-1000')
# dl = Department(dept_code='legal', dept_name='Legal', phone='555-2222')
# dm = Department(dept_code='mktg', dept_name='Marketing', phone='555-9999')

# leonard = Employee(name='Leonard', dept=dl)
# liz = Employee(name='Liz', dept=dl)
# maggie = Employee(name='Maggie', state='DC', dept=dm)
# nadine = Employee(name='Nadine')

# db.session.add_all([df, dl, dm, leonard, liz, maggie, nadine])
# db.session.commit()

# pc = Project(proj_code='car', proj_name='Design Car',
#              assignments=[EmployeeProject(emp_id=liz.id, role='Chair'),
#                           EmployeeProject(emp_id=maggie.id)])
# ps = Project(proj_code='server', proj_name='Deploy Server',
#              assignments=[EmployeeProject(emp_id=liz.id),
#                           EmployeeProject(emp_id=leonard.id, role='Auditor')])

# db.session.add_all([ps, pc])
# db.session.commit()
