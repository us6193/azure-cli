# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "billing role-assignment delete-by-billing-account",
    confirmation="Are you sure you want to perform this operation?",
)
class DeleteByBillingAccount(AAZCommand):
    """Delete a role assignment on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement.

    :example: BillingRoleAssignmentDeleteByBillingAccount
        az billing role-assignment delete-by-billing-account --billing-account-name 00000000-0000-0000-0000-000000000000:00000000-0000-0000-0000-000000000000_2018-09-30 --billing-role-assignment-name 10000000-aaaa-bbbb-cccc-100000000000_6fd330f6-7d26-4aff-b9cf-7bd699f965b9
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/{}/billingroleassignments/{}", "2024-04-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return None

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.billing_account_name = AAZStrArg(
            options=["--billing-account-name"],
            help="The ID that uniquely identifies a billing account.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^([0-9]+|([Pp][Cc][Nn]\\.[A-Za-z0-9]+)|[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}(:[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}_[0-9]{4}(-[0-9]{2}){2})?)$",
            ),
        )
        _args_schema.billing_role_assignment_name = AAZStrArg(
            options=["--billing-role-assignment-name"],
            help="The ID that uniquely identifies a role assignment.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-fA-F0-9]{8}[-]?([a-fA-F0-9]{4}[-]?){3}[a-fA-F0-9]{12}(_[a-fA-F0-9]{8}[-]?([a-fA-F0-9]{4}[-]?){3}[a-fA-F0-9]{12})?$",
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.BillingRoleAssignmentsDeleteByBillingAccount(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class BillingRoleAssignmentsDeleteByBillingAccount(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)
            if session.http_response.status_code in [204]:
                return self.on_204(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleAssignments/{billingRoleAssignmentName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "DELETE"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "billingAccountName", self.ctx.args.billing_account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "billingRoleAssignmentName", self.ctx.args.billing_role_assignment_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-04-01",
                    required=True,
                ),
            }
            return parameters

        def on_200(self, session):
            pass

        def on_204(self, session):
            pass


class _DeleteByBillingAccountHelper:
    """Helper class for DeleteByBillingAccount"""


__all__ = ["DeleteByBillingAccount"]