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
    "billing subscription cancel",
)
class Cancel(AAZCommand):
    """Cancels a usage-based subscription. This operation is supported only for billing accounts of type Microsoft Partner Agreement.

    :example: BillingSubscriptionsCancel
        az billing subscription cancel --billing-account-name 00000000-0000-0000-0000-000000000000:00000000-0000-0000-0000-000000000000_2019-05-31 --billing-subscription-name 11111111-1111-1111-1111-111111111111 --cancellation-reason Compromise --customer-id 11111111-1111-1111-1111-111111111111
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/{}/billingsubscriptions/{}/cancel", "2024-04-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, None)

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
        )
        _args_schema.billing_subscription_name = AAZStrArg(
            options=["--billing-subscription-name"],
            help="The ID that uniquely identifies a subscription.",
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.cancellation_reason = AAZStrArg(
            options=["--cancellation-reason"],
            arg_group="Parameters",
            help="Cancellation reason.",
            required=True,
            enum={"Compromise": "Compromise", "Dispute": "Dispute", "Other": "Other"},
        )
        _args_schema.customer_id = AAZStrArg(
            options=["--customer-id"],
            arg_group="Parameters",
            help="The fully qualified ID that uniquely identifies a customer.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.BillingSubscriptionsCancel(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class BillingSubscriptionsCancel(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    None,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingSubscriptions/{billingSubscriptionName}/cancel",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

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
                    "billingSubscriptionName", self.ctx.args.billing_subscription_name,
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

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("cancellationReason", AAZStrType, ".cancellation_reason", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("customerId", AAZStrType, ".customer_id")

            return self.serialize_content(_content_value)


class _CancelHelper:
    """Helper class for Cancel"""


__all__ = ["Cancel"]
