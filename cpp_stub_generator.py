import os
import re
import sublime
import sublime_plugin


INCLUDE_DIR = 'include'


class InsertText(sublime_plugin.TextCommand):
    def run(self, edit, text):
        self.view.insert(edit, 0, text)


class CppStubGenerator(sublime_plugin.WindowCommand):
    def read_lines(self, file_path):
        lines = []

        with open(file_path) as file:
            lines = file.readlines()

        return lines

    def generate_code(self, file_path, lines):
        namespace_name = ''
        class_name = ''
        code = self.generate_include(file_path)

        for line in lines:
            namespace_match = re.search(r'namespace\s(\w+)', line)
            class_match = re.search(r'class\s(\w+)', line)

            if namespace_match:
                namespace_name = namespace_match.group(1)
            elif class_match:
                class_name = class_match.group(1)
            else:
                code += self.process_line(line, namespace_name, class_name)

        return code

    def generate_include(self, file_path):
        include = ''
        file_name = os.path.basename(file_path)

        if INCLUDE_DIR in file_path:
            rel_path = self.find_rel_path(file_path)
            include = f'# include "{rel_path}"'
        else:
            include = f'# include "{file_name}"'

        return include

    def find_rel_path(self, file_path):
        rel_path = ''
        sub_dirs = file_path.split(os.sep)

        for d in sub_dirs:
            rel_path = '' if d == INCLUDE_DIR else os.path.join(rel_path, d)

        return rel_path

    def process_line(self, line, template_name, class_name):
        function = ''
        qualified_name = f'{template_name}::{class_name}' if template_name else class_name

        function_regex = re.compile(
            r'([\w\s\*\-&:<>]*?)([\w\-\+\*\/\[\]%=!<>~]+\([\w\s\*\+\-\(\)&:<>=,]*?\)[\w\s&]*?);'
        )
        match = re.search(function_regex, line.strip())

        if match:
            function = f'\n\n\n{match.group(1)}{qualified_name}::{match.group(2)}'
            function += '\n{\n}'

        return function

    def create_view(self, file_path, code):
        file_name = os.path.basename(file_path)
        file_name, _ = os.path.splitext(file_name)
        file_name = f'{file_name}.cpp'
        new_view = self.window.new_file()
        new_view.set_name(file_name)
        new_view.run_command('insert_text', {'text': code})

    def run(self):
        file_path = self.window.active_view().file_name()
        lines = self.read_lines(file_path)
        code = self.generate_code(file_path, lines)
        self.create_view(file_path, code)
