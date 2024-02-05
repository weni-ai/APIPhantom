import os
import json

from django.conf import settings

from .interfaces import Faker


class CLIJSFFaker(Faker):

    COMMAND = "node {path} --schema '{schema}'"
    CLI_FILE = "jsffaker/cli.js"

    def _get_command(self, schema: str) -> str:
        cli_path = os.path.join(settings.BASE_DIR, self.CLI_FILE)
        return self.COMMAND.format(path=cli_path, schema=schema)

    def _convert_schema_to_json(self, schema: dict) -> str:
        return json.dumps(schema)

    def generate_data_by_schema(self, schema: dict) -> dict:
        schema = self._convert_schema_to_json(schema)
        command = self._get_command(schema)
        data = os.popen(command).read()

        return json.loads(data)
