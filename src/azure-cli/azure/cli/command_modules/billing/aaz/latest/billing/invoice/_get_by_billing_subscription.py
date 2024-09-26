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
    "billing invoice get-by-billing-subscription",
)
class GetByBillingSubscription(AAZCommand):
    """Get an invoice by subscription ID and invoice ID. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

    :example: InvoicesGetByBillingSubscription
        az billing invoice get-by-billing-subscription --invoice-name E123456789
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/default/billingsubscriptions/{}/invoices/{}", "2024-04-01"],
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
        _args_schema.invoice_name = AAZStrArg(
            options=["--invoice-name"],
            help="The ID that uniquely identifies an invoice.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^(H[0-9]-[A-Z0-9]+)$|^(?:([GHT]|HT){1}[A-Z0-9]{9})$|^(?:[D]{1}[A-Z0-9]{9})$|^(?:E{1}[B-Z0-9]{1}[A-Z0-9]{8})$|^(?:EA[A-Z0-9]{8})$",
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.InvoicesGetByBillingSubscription(ctx=self.ctx)()
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

    class InvoicesGetByBillingSubscription(AAZHttpOperation):
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
                "/providers/Microsoft.Billing/billingAccounts/default/billingSubscriptions/{subscriptionId}/invoices/{invoiceName}",
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
                    "invoiceName", self.ctx.args.invoice_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
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
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.amount_due = AAZObjectType(
                serialized_name="amountDue",
            )
            properties.azure_prepayment_applied = AAZObjectType(
                serialized_name="azurePrepaymentApplied",
            )
            properties.billed_amount = AAZObjectType(
                serialized_name="billedAmount",
            )
            properties.billed_document_id = AAZStrType(
                serialized_name="billedDocumentId",
                flags={"read_only": True},
            )
            properties.billing_profile_display_name = AAZStrType(
                serialized_name="billingProfileDisplayName",
                flags={"read_only": True},
            )
            properties.billing_profile_id = AAZStrType(
                serialized_name="billingProfileId",
                flags={"read_only": True},
            )
            properties.credit_amount = AAZObjectType(
                serialized_name="creditAmount",
            )
            properties.credit_for_document_id = AAZStrType(
                serialized_name="creditForDocumentId",
                flags={"read_only": True},
            )
            properties.document_type = AAZStrType(
                serialized_name="documentType",
                flags={"read_only": True},
            )
            properties.documents = AAZListType(
                flags={"read_only": True},
            )
            properties.due_date = AAZStrType(
                serialized_name="dueDate",
                flags={"read_only": True},
            )
            properties.failed_payments = AAZListType(
                serialized_name="failedPayments",
                flags={"read_only": True},
            )
            properties.free_azure_credit_applied = AAZObjectType(
                serialized_name="freeAzureCreditApplied",
            )
            properties.invoice_date = AAZStrType(
                serialized_name="invoiceDate",
                flags={"read_only": True},
            )
            properties.invoice_period_end_date = AAZStrType(
                serialized_name="invoicePeriodEndDate",
                flags={"read_only": True},
            )
            properties.invoice_period_start_date = AAZStrType(
                serialized_name="invoicePeriodStartDate",
                flags={"read_only": True},
            )
            properties.invoice_type = AAZStrType(
                serialized_name="invoiceType",
                flags={"read_only": True},
            )
            properties.is_monthly_invoice = AAZBoolType(
                serialized_name="isMonthlyInvoice",
                flags={"read_only": True},
            )
            properties.payments = AAZListType(
                flags={"read_only": True},
            )
            properties.purchase_order_number = AAZStrType(
                serialized_name="purchaseOrderNumber",
                flags={"read_only": True},
            )
            properties.rebill_details = AAZObjectType(
                serialized_name="rebillDetails",
                flags={"read_only": True},
            )
            _GetByBillingSubscriptionHelper._build_schema_rebill_details_read(properties.rebill_details)
            properties.refund_details = AAZObjectType(
                serialized_name="refundDetails",
            )
            properties.special_taxation_type = AAZStrType(
                serialized_name="specialTaxationType",
                flags={"read_only": True},
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.sub_total = AAZObjectType(
                serialized_name="subTotal",
            )
            properties.subscription_display_name = AAZStrType(
                serialized_name="subscriptionDisplayName",
                flags={"read_only": True},
            )
            properties.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
                flags={"read_only": True},
            )
            properties.tax_amount = AAZObjectType(
                serialized_name="taxAmount",
            )
            properties.total_amount = AAZObjectType(
                serialized_name="totalAmount",
            )

            amount_due = cls._schema_on_200.properties.amount_due
            amount_due.currency = AAZStrType(
                flags={"read_only": True},
            )
            amount_due.value = AAZFloatType(
                flags={"read_only": True},
            )

            azure_prepayment_applied = cls._schema_on_200.properties.azure_prepayment_applied
            azure_prepayment_applied.currency = AAZStrType(
                flags={"read_only": True},
            )
            azure_prepayment_applied.value = AAZFloatType(
                flags={"read_only": True},
            )

            billed_amount = cls._schema_on_200.properties.billed_amount
            billed_amount.currency = AAZStrType(
                flags={"read_only": True},
            )
            billed_amount.value = AAZFloatType(
                flags={"read_only": True},
            )

            credit_amount = cls._schema_on_200.properties.credit_amount
            credit_amount.currency = AAZStrType(
                flags={"read_only": True},
            )
            credit_amount.value = AAZFloatType(
                flags={"read_only": True},
            )

            documents = cls._schema_on_200.properties.documents
            documents.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.documents.Element
            _element.document_numbers = AAZListType(
                serialized_name="documentNumbers",
                flags={"read_only": True},
            )
            _element.external_url = AAZStrType(
                serialized_name="externalUrl",
                flags={"read_only": True},
            )
            _element.kind = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.source = AAZStrType(
                flags={"read_only": True},
            )
            _element.url = AAZStrType(
                flags={"read_only": True},
            )

            document_numbers = cls._schema_on_200.properties.documents.Element.document_numbers
            document_numbers.Element = AAZStrType()

            failed_payments = cls._schema_on_200.properties.failed_payments
            failed_payments.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.failed_payments.Element
            _element.date = AAZStrType(
                flags={"read_only": True},
            )
            _element.failed_payment_reason = AAZStrType(
                serialized_name="failedPaymentReason",
                flags={"read_only": True},
            )

            free_azure_credit_applied = cls._schema_on_200.properties.free_azure_credit_applied
            free_azure_credit_applied.currency = AAZStrType(
                flags={"read_only": True},
            )
            free_azure_credit_applied.value = AAZFloatType(
                flags={"read_only": True},
            )

            payments = cls._schema_on_200.properties.payments
            payments.Element = AAZObjectType(
                flags={"read_only": True},
            )

            _element = cls._schema_on_200.properties.payments.Element
            _element.amount = AAZObjectType()
            _element.date = AAZStrType(
                flags={"read_only": True},
            )
            _element.payment_method_family = AAZStrType(
                serialized_name="paymentMethodFamily",
                flags={"read_only": True},
            )
            _element.payment_method_id = AAZStrType(
                serialized_name="paymentMethodId",
                flags={"read_only": True},
            )
            _element.payment_method_type = AAZStrType(
                serialized_name="paymentMethodType",
                flags={"read_only": True},
            )
            _element.payment_type = AAZStrType(
                serialized_name="paymentType",
                flags={"read_only": True},
            )

            amount = cls._schema_on_200.properties.payments.Element.amount
            amount.currency = AAZStrType(
                flags={"read_only": True},
            )
            amount.value = AAZFloatType(
                flags={"read_only": True},
            )

            refund_details = cls._schema_on_200.properties.refund_details
            refund_details.amount_refunded = AAZObjectType(
                serialized_name="amountRefunded",
            )
            refund_details.amount_requested = AAZObjectType(
                serialized_name="amountRequested",
            )
            refund_details.approved_on = AAZStrType(
                serialized_name="approvedOn",
                flags={"read_only": True},
            )
            refund_details.completed_on = AAZStrType(
                serialized_name="completedOn",
                flags={"read_only": True},
            )
            refund_details.rebill_invoice_id = AAZStrType(
                serialized_name="rebillInvoiceId",
                flags={"read_only": True},
            )
            refund_details.refund_operation_id = AAZStrType(
                serialized_name="refundOperationId",
                flags={"read_only": True},
            )
            refund_details.refund_reason = AAZStrType(
                serialized_name="refundReason",
                flags={"read_only": True},
            )
            refund_details.refund_status = AAZStrType(
                serialized_name="refundStatus",
                flags={"read_only": True},
            )
            refund_details.requested_on = AAZStrType(
                serialized_name="requestedOn",
                flags={"read_only": True},
            )
            refund_details.transaction_count = AAZIntType(
                serialized_name="transactionCount",
                flags={"read_only": True},
            )

            amount_refunded = cls._schema_on_200.properties.refund_details.amount_refunded
            amount_refunded.currency = AAZStrType(
                flags={"read_only": True},
            )
            amount_refunded.value = AAZFloatType(
                flags={"read_only": True},
            )

            amount_requested = cls._schema_on_200.properties.refund_details.amount_requested
            amount_requested.currency = AAZStrType(
                flags={"read_only": True},
            )
            amount_requested.value = AAZFloatType(
                flags={"read_only": True},
            )

            sub_total = cls._schema_on_200.properties.sub_total
            sub_total.currency = AAZStrType(
                flags={"read_only": True},
            )
            sub_total.value = AAZFloatType(
                flags={"read_only": True},
            )

            tax_amount = cls._schema_on_200.properties.tax_amount
            tax_amount.currency = AAZStrType(
                flags={"read_only": True},
            )
            tax_amount.value = AAZFloatType(
                flags={"read_only": True},
            )

            total_amount = cls._schema_on_200.properties.total_amount
            total_amount.currency = AAZStrType(
                flags={"read_only": True},
            )
            total_amount.value = AAZFloatType(
                flags={"read_only": True},
            )

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


class _GetByBillingSubscriptionHelper:
    """Helper class for GetByBillingSubscription"""

    _schema_rebill_details_read = None

    @classmethod
    def _build_schema_rebill_details_read(cls, _schema):
        if cls._schema_rebill_details_read is not None:
            _schema.credit_note_document_id = cls._schema_rebill_details_read.credit_note_document_id
            _schema.invoice_document_id = cls._schema_rebill_details_read.invoice_document_id
            _schema.rebill_details = cls._schema_rebill_details_read.rebill_details
            return

        cls._schema_rebill_details_read = _schema_rebill_details_read = AAZObjectType(
            flags={"read_only": True}
        )

        rebill_details_read = _schema_rebill_details_read
        rebill_details_read.credit_note_document_id = AAZStrType(
            serialized_name="creditNoteDocumentId",
            flags={"read_only": True},
        )
        rebill_details_read.invoice_document_id = AAZStrType(
            serialized_name="invoiceDocumentId",
            flags={"read_only": True},
        )
        rebill_details_read.rebill_details = AAZObjectType(
            serialized_name="rebillDetails",
            flags={"read_only": True},
        )
        cls._build_schema_rebill_details_read(rebill_details_read.rebill_details)

        _schema.credit_note_document_id = cls._schema_rebill_details_read.credit_note_document_id
        _schema.invoice_document_id = cls._schema_rebill_details_read.invoice_document_id
        _schema.rebill_details = cls._schema_rebill_details_read.rebill_details


__all__ = ["GetByBillingSubscription"]
