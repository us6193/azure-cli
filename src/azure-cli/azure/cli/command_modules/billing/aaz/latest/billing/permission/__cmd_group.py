# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "billing permission",
)
class __CMDGroup(AAZCommandGroup):
    """Check Access at multiple scopes like Billing Accounts, Billing Profile, Customer etc.
    """
    pass


__all__ = ["__CMDGroup"]
