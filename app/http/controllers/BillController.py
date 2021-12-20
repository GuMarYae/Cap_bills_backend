""" A BillController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Bill import Bill





class BillController(Controller):
    """Class Docstring Description
    """
    
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", BillController)
        """
        id = self.request.param("id")
        return Bill.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", BillController)
        """
        return Bill.all()

    def create(self):
        subject = self.request.input("subject")
        details = self.request.input("details")
        date = self.request.input("date")
        bill = Bill.create({"subject": subject, "details": details, "date": date })
        return bill
    
    def update(self):
        subject = self.request.input("subject")
        details = self.request.input("details")
        date = self.request.input("date")
        id = self.request.param("id")
        Bill.where("id", id).update({"subject": subject, "details": details, "date": date})
        return Bill.where("id", id).get()

   

   

    def destroy(self):
        id = self.request.param("id")
        bill = Bill.where("id", id).get()
        Bill.where("id", id).delete()
        return bill