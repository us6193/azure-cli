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
    "billing savings-plan-order get-by-billing-account",
)
class GetByBillingAccount(AAZCommand):
    """Get a savings plan order by billing account.

    :example: SavingsPlanOrderGet
        az billing savings-plan-order get-by-billing-account --billing-account-name 00000000-0000-0000-0000-000000000000:00000000-0000-0000-0000-000000000000_2019-05-31 --savings-plan-order-id 20000000-0000-0000-0000-000000000000
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/{}/savingsplanorders/{}", "2024-04-01"],
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
        _args_schema.savings_plan_order_id = AAZStrArg(
            options=["--savings-plan-order-id"],
            help="Order ID of the savings plan",
            required=True,
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="May be used to expand the planInformation.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SavingsPlanOrdersGetByBillingAccount(ctx=self.ctx)()
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

    class SavingsPlanOrdersGetByBillingAccount(AAZHttpOperation):
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
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/savingsPlanOrders/{savingsPlanOrderId}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

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
                    "savingsPlanOrderId", self.ctx.args.savings_plan_order_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "expand", self.ctx.args.expand,
                ),
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
                    "Accept", "application/json",
                ),
            }
            return parameters

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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.sku = AAZObjectType(
                flags={"required": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.benefit_start_time = AAZStrType(
                serialized_name="benefitStartTime",
                flags={"read_only": True},
            )
            properties.billing_account_id = AAZStrType(
                serialized_name="billingAccountId",
                flags={"read_only": True},
            )
            properties.billing_plan = AAZStrType(
                serialized_name="billingPlan",
            )
            properties.billing_profile_id = AAZStrType(
                serialized_name="billingProfileId",
                flags={"read_only": True},
            )
            properties.billing_scope_id = AAZStrType(
                serialized_name="billingScopeId",
            )
            properties.customer_id = AAZStrType(
                serialized_name="customerId",
                flags={"read_only": True},
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.expiry_date_time = AAZStrType(
                serialized_name="expiryDateTime",
                flags={"read_only": True},
            )
            properties.extended_status_info = AAZObjectType(
                serialized_name="extendedStatusInfo",
                flags={"read_only": True},
            )
            _GetByBillingAccountHelper._build_schema_extended_status_info_read(properties.extended_status_info)
            properties.plan_information = AAZObjectType(
                serialized_name="planInformation",
            )
            properties.product_code = AAZStrType(
                serialized_name="productCode",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.savings_plans = AAZListType(
                serialized_name="savingsPlans",
            )
            properties.term = AAZStrType()

            plan_information = cls._schema_on_200.properties.plan_information
            plan_information.next_payment_due_date = AAZStrType(
                serialized_name="nextPaymentDueDate",
            )
            plan_information.pricing_currency_total = AAZObjectType(
                serialized_name="pricingCurrencyTotal",
            )
            _GetByBillingAccountHelper._build_schema_price_read(plan_information.pricing_currency_total)
            plan_information.start_date = AAZStrType(
                serialized_name="startDate",
            )
            plan_information.transactions = AAZListType()

            transactions = cls._schema_on_200.properties.plan_information.transactions
            transactions.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.plan_information.transactions.Element
            _element.billing_currency_total = AAZObjectType(
                serialized_name="billingCurrencyTotal",
            )
            _GetByBillingAccountHelper._build_schema_price_read(_element.billing_currency_total)
            _element.due_date = AAZStrType(
                serialized_name="dueDate",
            )
            _element.extended_status_info = AAZObjectType(
                serialized_name="extendedStatusInfo",
                flags={"read_only": True},
            )
            _GetByBillingAccountHelper._build_schema_extended_status_info_read(_element.extended_status_info)
            _element.payment_date = AAZStrType(
                serialized_name="paymentDate",
            )
            _element.pricing_currency_total = AAZObjectType(
                serialized_name="pricingCurrencyTotal",
            )
            _GetByBillingAccountHelper._build_schema_price_read(_element.pricing_currency_total)
            _element.status = AAZStrType()

            savings_plans = cls._schema_on_200.properties.savings_plans
            savings_plans.Element = AAZStrType(
                flags={"read_only": True},
            )

            sku = cls._schema_on_200.sku
            sku.name = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _GetByBillingAccountHelper:
    """Helper class for GetByBillingAccount"""

    _schema_extended_status_info_read = None

    @classmethod
    def _build_schema_extended_status_info_read(cls, _schema):
        if cls._schema_extended_status_info_read is not None:
            _schema.message = cls._schema_extended_status_info_read.message
            _schema.properties = cls._schema_extended_status_info_read.properties
            _schema.status_code = cls._schema_extended_status_info_read.status_code
            return

        cls._schema_extended_status_info_read = _schema_extended_status_info_read = AAZObjectType(
            flags={"read_only": True}
        )

        extended_status_info_read = _schema_extended_status_info_read
        extended_status_info_read.message = AAZStrType()
        extended_status_info_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        extended_status_info_read.status_code = AAZStrType(
            serialized_name="statusCode",
        )

        properties = _schema_extended_status_info_read.properties
        properties.subscription_id = AAZStrType(
            serialized_name="subscriptionId",
        )

        _schema.message = cls._schema_extended_status_info_read.message
        _schema.properties = cls._schema_extended_status_info_read.properties
        _schema.status_code = cls._schema_extended_status_info_read.status_code

    _schema_price_read = None

    @classmethod
    def _build_schema_price_read(cls, _schema):
        if cls._schema_price_read is not None:
            _schema.amount = cls._schema_price_read.amount
            _schema.currency_code = cls._schema_price_read.currency_code
            return

        cls._schema_price_read = _schema_price_read = AAZObjectType()

        price_read = _schema_price_read
        price_read.amount = AAZFloatType()
        price_read.currency_code = AAZStrType(
            serialized_name="currencyCode",
        )

        _schema.amount = cls._schema_price_read.amount
        _schema.currency_code = cls._schema_price_read.currency_code


__all__ = ["GetByBillingAccount"]
