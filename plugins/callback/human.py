# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback import CallbackBase
from ansible.utils.color import stringc

class CallbackModule(CallbackBase):

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'human'

    def __init__(self):
        super(CallbackModule, self).__init__()
        self.line = ""

    def v2_runner_on_failed(self, result, ignore_errors=False):
        if 'exception' in result._result:
            if self._display.verbosity < 3:
                # extract just the actual error message from the exception text
                error = result._result['exception'].strip().split('\n')[-1]
                msg = "An exception occurred during task execution. To see the full traceback, use -vvv. The error was: %s" % error
            else:
                msg = "An exception occurred during task execution. The full traceback is:\n" + result._result['exception']

            self._display.display("> " + msg, color='red')

            # finally, remove the exception from the result so it's not shown every time
            del result._result['exception']

        self._display.display(" > %s" % (self._dump_results(result._result)), color='red')

    def v2_runner_on_ok(self, result):
        if result._result.get('changed', True):
            self._display.display(self.line, color='green')
        self._handle_warnings(result._result)
        self.line = ""

    def v2_runner_on_skipped(self, result):
        self.line = ""

    def v2_runner_on_unreachable(self, result):
        self._display.display(self.line + "> UNREACHABLE!", color='yellow')

    def v2_playbook_on_play_start(self, play):
        self._display.display(self.line + " RUNNING PLAYBOOK...", color='yellow')

    def v2_playbook_on_task_start(self, task, is_conditional):
        self.line = "  " + task.get_name().strip()

    def v2_on_file_diff(self, result):
        if 'diff' in result._result:
            self._display.display("   " + self._get_diff(result._result['diff']))
