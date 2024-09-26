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
    "billing product validate-move-eligibility",
)
class ValidateMoveEligibility(AAZCommand):
    """Validates if a product's charges can be moved to a new invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement.

    :example: ProductValidateMoveSuccess
        az billing product validate-move-eligibility --billing-account-name a1a9c77e-4cec-4a6c-a089-867d973a6074:a80d3b1f-c626-4e5e-82ed-1173bd91c838_2019-05-31 --product-name 6b96d3f2-9008-4a9d-912f-f87744185aa3 --destination-invoice-section-id /providers/Microsoft.Billing/billingAccounts/a1a9c77e-4cec-4a6c-a089-867d973a6074:a80d3b1f-c626-4e5e-82ed-1173bd91c838_2019-05-31/billingProfiles/ea36e548-1505-41db-bebc-46fff3d37998/invoiceSections/Q7GV-UUVA-PJA-TGB
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/{}/products/{}/validatemoveeligibility", "2024-04-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

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
        _args_schema.product_name = AAZStrArg(
            options=["--product-name"],
            help="The ID that uniquely identifies a product.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$",
            ),
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.destination_invoice_section_id = AAZStrArg(
            options=["--destination-invoice-section-id"],
            arg_group="Parameters",
            help="The destination invoice section id.",
            required=True,
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ProductsValidateMoveEligibility(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ProductsValidateMoveEligibility(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/products/{productName}/validateMoveEligibility",
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
                    "productName", self.ctx.args.product_name,
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
                **self.serialize_header_param(
                    "Accept", "application/json",
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
            _builder.set_prop("destinationInvoiceSectionId", AAZStrType, ".destination_invoice_section_id", typ_kwargs={"flags": {"required": True}})

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.error_details = AAZObjectType(
                serialized_name="errorDetails",
            )
            _schema_on_200.is_move_eligible = AAZBoolType(
                serialized_name="isMoveEligible",
            )

            error_details = cls._schema_on_200.error_details
            error_details.code = AAZStrType(
                flags={"read_only": True},
            )
            error_details.details = AAZStrType(
                flags={"read_only": True},
            )
            error_details.message = AAZStrType(
                flags={"read_only": True},
            )

            return cls._schema_on_200


class _ValidateMoveEligibilityHelper:
    """Helper class for ValidateMoveEligibility"""


__all__ = ["ValidateMoveEligibility"]
