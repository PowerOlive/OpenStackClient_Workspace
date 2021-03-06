#   Copyright 2016 Huawei, Inc. All rights reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#
import logging

from osc_lib.command import command

from workspaceclient.common.i18n import _
from workspaceclient.v1 import resource

LOG = logging.getLogger(__name__)


class ShowJob(command.ShowOne):
    _description = _("list product")

    def get_parser(self, prog_name):
        parser = super(ShowJob, self).get_parser(prog_name)
        parser.add_argument(
            "job_id",
            metavar="<job-id>",
            help=_("Job to show (ID)")
        )
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.workspace.jobs
        job = mgr.get(args.job_id)
        columns = resource.Job.show_column_names
        formatter = resource.Job.formatter
        outputs = job.get_display_data(columns, formatter=formatter)
        return columns, outputs
