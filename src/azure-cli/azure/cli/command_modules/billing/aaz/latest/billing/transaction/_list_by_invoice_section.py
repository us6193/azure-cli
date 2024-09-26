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
    "billing transaction list-by-invoice-section",
)
class ListByInvoiceSection(AAZCommand):
    """List the billed or unbilled transactions by invoice section name for given start date and end date. Transactions include purchases, refunds and Azure usage charges. Unbilled transactions are listed under pending invoice Id and do not include tax. Tax is added to the amount once an invoice is generated.

    :example: TransactionsListByInvoiceSection
        az billing transaction list-by-invoice-section --billing-account-name 00000000-0000-0000-0000-000000000000:00000000-0000-0000-0000-000000000000_2019-05-31 --billing-profile-name xxxx-xxxx-xxx-xxx --invoice-section-name 22000000-0000-0000-0000-000000000000 --period-start-date 2024-04-01 --period-end-date 2023-05-30 --type Billed --filter properties/date gt '2020-10-01' --search storage
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/{}/billingprofiles/{}/invoicesections/{}/transactions", "2024-04-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

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
        _args_schema.billing_profile_name = AAZStrArg(
            options=["--billing-profile-name"],
            help="The ID that uniquely identifies a billing profile.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-_]{1,128}$",
            ),
        )
        _args_schema.invoice_section_name = AAZStrArg(
            options=["--invoice-section-name"],
            help="The ID that uniquely identifies an invoice section.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-_]{1,128}$",
            ),
        )
        _args_schema.count = AAZBoolArg(
            options=["--count"],
            help="The count query option allows clients to request a count of the matching resources included with the resources in the response.",
        )
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="The filter query option allows clients to filter a collection of resources that are addressed by a request URL.",
        )
        _args_schema.order_by = AAZStrArg(
            options=["--order-by"],
            help="The orderby query option allows clients to request resources in a particular order.",
        )
        _args_schema.period_end_date = AAZDateArg(
            options=["--period-end-date"],
            help="The end date to fetch the transactions. The date should be specified in MM-DD-YYYY format.",
            required=True,
        )
        _args_schema.period_start_date = AAZDateArg(
            options=["--period-start-date"],
            help="The start date to fetch the transactions. The date should be specified in MM-DD-YYYY format.",
            required=True,
        )
        _args_schema.search = AAZStrArg(
            options=["--search"],
            help="The search query option allows clients to request items within a collection matching a free-text search expression. search is only supported for string fields.",
        )
        _args_schema.skip = AAZIntArg(
            options=["--skip"],
            help="The skip query option requests the number of items in the queried collection that are to be skipped and not included in the result.",
        )
        _args_schema.top = AAZIntArg(
            options=["--top"],
            help="The top query option requests the number of items in the queried collection to be included in the result. The maximum supported value for top is 50.",
        )
        _args_schema.type = AAZStrArg(
            options=["--type"],
            help="The type of transaction.",
            required=True,
            enum={"Billed": "Billed", "Other": "Other", "Unbilled": "Unbilled"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.TransactionsListByInvoiceSection(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class TransactionsListByInvoiceSection(AAZHttpOperation):
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
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/transactions",
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
                    "billingProfileName", self.ctx.args.billing_profile_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "invoiceSectionName", self.ctx.args.invoice_section_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "count", self.ctx.args.count,
                ),
                **self.serialize_query_param(
                    "filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "orderBy", self.ctx.args.order_by,
                ),
                **self.serialize_query_param(
                    "periodEndDate", self.ctx.args.period_end_date,
                    required=True,
                ),
                **self.serialize_query_param(
                    "periodStartDate", self.ctx.args.period_start_date,
                    required=True,
                ),
                **self.serialize_query_param(
                    "search", self.ctx.args.search,
                ),
                **self.serialize_query_param(
                    "skip", self.ctx.args.skip,
                ),
                **self.serialize_query_param(
                    "top", self.ctx.args.top,
                ),
                **self.serialize_query_param(
                    "type", self.ctx.args.type,
                    required=True,
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType()
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.azure_credit_applied = AAZObjectType(
                serialized_name="azureCreditApplied",
            )
            properties.azure_plan = AAZStrType(
                serialized_name="azurePlan",
            )
            properties.billing_currency = AAZStrType(
                serialized_name="billingCurrency",
            )
            properties.billing_profile_display_name = AAZStrType(
                serialized_name="billingProfileDisplayName",
            )
            properties.billing_profile_id = AAZStrType(
                serialized_name="billingProfileId",
            )
            properties.consumption_commitment_decremented = AAZObjectType(
                serialized_name="consumptionCommitmentDecremented",
            )
            properties.credit_type = AAZStrType(
                serialized_name="creditType",
            )
            properties.customer_display_name = AAZStrType(
                serialized_name="customerDisplayName",
            )
            properties.customer_id = AAZStrType(
                serialized_name="customerId",
            )
            properties.date = AAZStrType()
            properties.discount = AAZFloatType()
            properties.effective_price = AAZObjectType(
                serialized_name="effectivePrice",
            )
            properties.exchange_rate = AAZFloatType(
                serialized_name="exchangeRate",
            )
            properties.invoice = AAZStrType()
            properties.invoice_id = AAZStrType(
                serialized_name="invoiceId",
            )
            properties.invoice_section_display_name = AAZStrType(
                serialized_name="invoiceSectionDisplayName",
            )
            properties.invoice_section_id = AAZStrType(
                serialized_name="invoiceSectionId",
            )
            properties.is_third_party = AAZBoolType(
                serialized_name="isThirdParty",
            )
            properties.kind = AAZStrType()
            properties.market_price = AAZObjectType(
                serialized_name="marketPrice",
            )
            properties.part_number = AAZStrType(
                serialized_name="partNumber",
            )
            properties.pricing_currency = AAZStrType(
                serialized_name="pricingCurrency",
            )
            properties.product_description = AAZStrType(
                serialized_name="productDescription",
            )
            properties.product_family = AAZStrType(
                serialized_name="productFamily",
            )
            properties.product_type = AAZStrType(
                serialized_name="productType",
            )
            properties.product_type_id = AAZStrType(
                serialized_name="productTypeId",
            )
            properties.quantity = AAZIntType()
            properties.reason_code = AAZStrType(
                serialized_name="reasonCode",
            )
            properties.refund_transaction_details = AAZObjectType(
                serialized_name="refundTransactionDetails",
            )
            properties.service_period_end_date = AAZStrType(
                serialized_name="servicePeriodEndDate",
            )
            properties.service_period_start_date = AAZStrType(
                serialized_name="servicePeriodStartDate",
            )
            properties.special_taxation_type = AAZStrType(
                serialized_name="specialTaxationType",
            )
            properties.sub_total = AAZObjectType(
                serialized_name="subTotal",
            )
            properties.tax = AAZObjectType()
            properties.transaction_amount = AAZObjectType(
                serialized_name="transactionAmount",
            )
            properties.transaction_type = AAZStrType(
                serialized_name="transactionType",
            )
            properties.unit_of_measure = AAZStrType(
                serialized_name="unitOfMeasure",
            )
            properties.unit_type = AAZStrType(
                serialized_name="unitType",
            )
            properties.units = AAZFloatType()

            azure_credit_applied = cls._schema_on_200.value.Element.properties.azure_credit_applied
            azure_credit_applied.currency = AAZStrType(
                flags={"read_only": True},
            )
            azure_credit_applied.value = AAZFloatType(
                flags={"read_only": True},
            )

            consumption_commitment_decremented = cls._schema_on_200.value.Element.properties.consumption_commitment_decremented
            consumption_commitment_decremented.currency = AAZStrType(
                flags={"read_only": True},
            )
            consumption_commitment_decremented.value = AAZFloatType(
                flags={"read_only": True},
            )

            effective_price = cls._schema_on_200.value.Element.properties.effective_price
            effective_price.currency = AAZStrType(
                flags={"read_only": True},
            )
            effective_price.value = AAZFloatType(
                flags={"read_only": True},
            )

            market_price = cls._schema_on_200.value.Element.properties.market_price
            market_price.currency = AAZStrType(
                flags={"read_only": True},
            )
            market_price.value = AAZFloatType(
                flags={"read_only": True},
            )

            refund_transaction_details = cls._schema_on_200.value.Element.properties.refund_transaction_details
            refund_transaction_details.amount_refunded = AAZObjectType(
                serialized_name="amountRefunded",
            )
            refund_transaction_details.amount_requested = AAZObjectType(
                serialized_name="amountRequested",
            )
            refund_transaction_details.refund_operation_id = AAZStrType(
                serialized_name="refundOperationId",
            )

            amount_refunded = cls._schema_on_200.value.Element.properties.refund_transaction_details.amount_refunded
            amount_refunded.currency = AAZStrType(
                flags={"read_only": True},
            )
            amount_refunded.value = AAZFloatType(
                flags={"read_only": True},
            )

            amount_requested = cls._schema_on_200.value.Element.properties.refund_transaction_details.amount_requested
            amount_requested.currency = AAZStrType(
                flags={"read_only": True},
            )
            amount_requested.value = AAZFloatType(
                flags={"read_only": True},
            )

            sub_total = cls._schema_on_200.value.Element.properties.sub_total
            sub_total.currency = AAZStrType(
                flags={"read_only": True},
            )
            sub_total.value = AAZFloatType(
                flags={"read_only": True},
            )

            tax = cls._schema_on_200.value.Element.properties.tax
            tax.currency = AAZStrType(
                flags={"read_only": True},
            )
            tax.value = AAZFloatType(
                flags={"read_only": True},
            )

            transaction_amount = cls._schema_on_200.value.Element.properties.transaction_amount
            transaction_amount.currency = AAZStrType(
                flags={"read_only": True},
            )
            transaction_amount.value = AAZFloatType(
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200.value.Element.system_data
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

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListByInvoiceSectionHelper:
    """Helper class for ListByInvoiceSection"""


__all__ = ["ListByInvoiceSection"]