from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

import os
import shutil

import sys
if sys.platform.startswith("win"):
    import _locale
    # pylint: disable=protected-access
    _locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class TextBasedBrowserTest(StageTest):

    def generate(self):

        dir_for_files = 'tb_tabs'
        return [
            TestCase(
                stdin='bloomberg.com\nbloomberg\nexit',
                attach='Bloomberg',
                args=[dir_for_files]
            ),
            TestCase(
                stdin='nytimes.com\nnytimes\nexit',
                attach='The New York Times',
                args=[dir_for_files]
            ),
        ]

    def _check_files(self, path_for_tabs: str, right_word: str) -> int:
        """
        Helper which checks that browser saves visited url in files and
        provides access to them.

        :param path_for_tabs: directory which must contain saved tabs
        :param right_word: Word-marker which must be in right tab
        :return: True, if right_words is present in saved tab
        """

        path, dirs, filenames = next(os.walk(path_for_tabs))

        for file in filenames:
            print("file: {}".format(file))
            with open(os.path.join(path_for_tabs, file), 'r', encoding='utf-8') as tab:
                try:
                    content = tab.read()
                except UnicodeDecodeError:
                    return -1
                print(content)
                if 'html' in content and right_word in content:
                    return 1

        return 0

    def check(self, reply, attach):

        # Incorrect URL
        if attach is None:
            if '<p>' in reply:
                return CheckResult.wrong('You haven\'t checked whether the URL was correct')
            else:
                return CheckResult.correct()

        # Correct URL
        if isinstance(attach, str):
            right_word = attach

            path_for_tabs = os.path.join(os.curdir, 'tb_tabs')

            if not os.path.isdir(path_for_tabs):
                return CheckResult.wrong("There are no directory for tabs")

            check_files_result = self._check_files(path_for_tabs, right_word)
            if not check_files_result:
                return CheckResult.wrong('There are no correct saved tabs')
            elif check_files_result == -1:
                return CheckResult.wrong('An error occurred while reading your saved tab. '
                                         'Perhaps you used the wrong encoding?')

            try:
                shutil.rmtree(path_for_tabs)
            except PermissionError:
                return CheckResult.wrong("Impossible to remove the directory for tabs. Perhaps you haven't closed some file?")

            if '<body' in reply and right_word in reply:
                return CheckResult.correct()

            return CheckResult.wrong('You haven\'t print result of request')


TextBasedBrowserTest('browser.browser').run_tests()
