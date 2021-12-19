import re
import subprocess

from django.db import models

from cabot.cabotapp.models import StatusCheck, StatusCheckResult


class NPINGStatusCheck(StatusCheck):
    check_name = 'nping'
    edit_url_name = f'update-{check_name}-check'
    duplicate_url_name = f'duplicate-{check_name}-check'
    icon_class = 'glyphicon-import'
    host = models.TextField(
        help_text='Host to check.',
        verbose_name="Target host(s)"
    )
    nping_cmd_line_switches = models.TextField(
        help_text='Enter switches as they vould be entered on the command line.',
        verbose_name="NPing command line switches"
    )

    count = models.PositiveIntegerField(
        help_text='Number of packet to send.',
        default=1
    )

    def _run(self):
        regex = r".+Lost: ([0-9]+).*"
        result = StatusCheckResult(status_check=self)
        args = ['nping'] + str(self.nping_cmd_line_switches).split() + ['-c', str(self.count)] + str(self.host).split()
        lost_count = 0
        try:
            # We redirect stderr to STDOUT because ping can write to both, depending on the kind of error.
            output = str(subprocess.run(args, capture_output=True).stdout.decode())
            # Count lost packets to determine if test passed or not
            matches = re.finditer(regex, output)
            for line in matches:
                lost_count += int(line.group(1))

            if lost_count == 0:
                result.succeeded = True
            else:
                result.succeeded = False
                result.error = "Packets were lost while pinging"
                result.raw_data = output

        except subprocess.CalledProcessError as e:
            result.succeeded = False
            result.error = f'Error occurred while executing NPing: {e.message}'
            result.raw_data = e.output

        return result
