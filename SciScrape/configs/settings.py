#!/usr/bin/python3

import yaml

from configs.env import Env

from exceptions.settings_exception import SettingsException

class Settings:

    @classmethod
    def search_property_in_file(self, property):
        try:
            with open(Env.CONFIGS_FILE, 'r') as file:
                lines = file.readlines()

                for line_number, line in enumerate(lines, start=1):
                    if property.split('.')[-1] in line:
                        return f"{line_number} -> '{line.strip()}'"

        except FileNotFoundError:
            return None

    @classmethod
    def is_valid(self, property, value, data_type):
        if type(value) == str:
            value_type = 'STRING'
        elif type(value) == int:
            value_type = 'INT'
        elif type(value) == float:
            value_type = 'FLOAT'
        elif type(value) == bool:
            value_type = 'BOOLEAN'

        data_type = data_type.upper()
        configs_file = Env.CONFIGS_FILE.replace('./', '')
        line_position = self.search_property_in_file(property)

        if value_type != data_type:
            raise SettingsException(f"The '{property}' configuration is invalid. Expected type {data_type}, but "
                                    f"instead a {value_type} was passed. Please "
                                    f"fix it in the file: {configs_file}:{line_position}")

        return value

    @classmethod
    def get(self, property, data_type):
        try:
            with open(Env.CONFIGS_FILE, 'r') as content:
                data = yaml.safe_load(content)

            value = data
            property_parts = property.split('.')

            for part in property_parts:
                value = value[part]

            return self.is_valid(property, value, data_type)

        except FileNotFoundError:
            raise SettingsException(f"File '{Env.CONFIGS_FILE.replace('./', '')}' not found")

        except yaml.YAMLError as e:
            raise SettingsException(f"Error while parsing the YAML file.: {e}")
