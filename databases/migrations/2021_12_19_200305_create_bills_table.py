"""CreateBillsTable Migration."""

from masoniteorm.migrations import Migration


class CreateBillsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("bills") as table:
            table.increments("id")
            table.string("subject")
            table.string("details")
            table.string("date")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("bills")