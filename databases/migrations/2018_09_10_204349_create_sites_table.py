from orator.migrations import Migration


class CreateSitesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('sites') as table:
            table.increments('id')
            table.string('url')
            table.string('image_url')
            table.string('site_name')
            table.string('submitter_name')
            table.string('submitter_email')
            table.boolean('approved')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('sites')
