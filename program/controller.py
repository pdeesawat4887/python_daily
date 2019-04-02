from program import view
from program.model import Person

def showAll():
    #gets list of all Person objects
    people_in_db = Person.getAll()
    #calls view
    return view.showAllView(people_in_db)

def start():
    view.startView()
    input2 = input()
    if input2 == 'y':
        return showAll()
    else:
        return view.endView()

if __name__ == "__main__":
    #running controller function
    start()