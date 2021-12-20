"""BillTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Bill import Bill


class BillTableSeeder(Seeder):
    def run(self):
        Bill.create({"subject": "girlfriend", "details": "pay her phone bill", "date":"12/20/2021"})
        Bill.create({"subject": "National University", "details": "pay bfore January 1st", "date":"12/31/2021"})
        Bill.create({"subject": "General Assembly", "details": "pay bill before the 23rd", "date":"12/20/2021"})
        Bill.create({"subject": "Birthday", "details": "Dont pay anythng on you birthday", "date":"12/17/2021"})