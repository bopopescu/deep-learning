# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command for spanner instances add-iam-policy-binding."""

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.iam import iam_util
from googlecloudsdk.command_lib.spanner import flags
from googlecloudsdk.command_lib.spanner import iam
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources


class AddIamPolicyBinding(base.Command):
  """Add an IAM policy binding to a Cloud Spanner instance."""

  @staticmethod
  def Args(parser):
    """Args is called by calliope to gather arguments for this command.

    Please add arguments in alphabetical order except for no- or a clear-
    pair for that argument which can follow the argument itself.
    Args:
      parser: An argparse parser that you can use to add arguments that go
          on the command line after this command. Positional arguments are
          allowed.
    """
    flags.Instance().AddToParser(parser)

    iam_util.AddArgsForAddIamPolicyBinding(parser)

  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      Some value that we want to have printed later.
    """
    instance_ref = resources.REGISTRY.Parse(
        args.instance,
        params={'projectsId': properties.VALUES.core.project.GetOrFail},
        collection='spanner.projects.instances')
    return iam.AddInstanceIamPolicyBinding(instance_ref, args.member, args.role)
