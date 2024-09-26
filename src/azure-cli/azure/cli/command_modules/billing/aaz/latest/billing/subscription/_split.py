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
    "billing subscription split",
)
class Split(AAZCommand):
    """Splits a subscription into a new subscription with quantity less than current subscription quantity and not equal to 0.

    :example: BillingSubscriptionsSplit
        az billing subscription split --billing-account-name 00000000-0000-0000-0000-000000000000:00000000-0000-0000-0000-000000000000_2019-05-31 --billing-subscription-name 11111111-1111-1111-1111-111111111111 --target-product-type-id XYZ56789 --target-sku-id 0001 --quantity 1 --term-duration P1M --billing-frequency P1M
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/{}/billingsubscriptions/{}/split", "2024-04-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

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
        _args_schema.billing_frequency = AAZStrArg(
            options=["--billing-frequency"],
            arg_group="Parameters",
            help="The billing frequency of the target subscription in the ISO8601 format. Example: P1M, P3M, P1Y\"",
        )
        _args_schema.quantity = AAZIntArg(
            options=["--quantity"],
            arg_group="Parameters",
            help="The quantity of the target product to which the subscription needs to be split into.",
        )
        _args_schema.target_product_type_id = AAZStrArg(
            options=["--target-product-type-id"],
            arg_group="Parameters",
            help="The ID of the target product to which the subscription needs to be split into. This value is not same as the value returned in Get API call and can be retrieved from Catalog API to know the product id to split into.",
        )
        _args_schema.target_sku_id = AAZStrArg(
            options=["--target-sku-id"],
            arg_group="Parameters",
            help="The ID of the target product to which the subscription needs to be split into. This value is not same as the value returned in Get API call and can be retrieved from Catalog API to know the sku id to split into.",
        )
        _args_schema.term_duration = AAZStrArg(
            options=["--term-duration"],
            arg_group="Parameters",
            help="The term duration of the target in ISO8601 format product to which the subscription needs to be split into. Example: P1M, P1Y",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.BillingSubscriptionsSplit(ctx=self.ctx)()
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

    class BillingSubscriptionsSplit(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingSubscriptions/{billingSubscriptionName}/split",
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
            _builder.set_prop("billingFrequency", AAZStrType, ".billing_frequency")
            _builder.set_prop("quantity", AAZIntType, ".quantity")
            _builder.set_prop("targetProductTypeId", AAZStrType, ".target_product_type_id")
            _builder.set_prop("targetSkuId", AAZStrType, ".target_sku_id")
            _builder.set_prop("termDuration", AAZStrType, ".term_duration")

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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
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
            properties.auto_renew = AAZStrType(
                serialized_name="autoRenew",
            )
            properties.beneficiary = AAZObjectType()
            properties.beneficiary_tenant_id = AAZStrType(
                serialized_name="beneficiaryTenantId",
            )
            properties.billing_frequency = AAZStrType(
                serialized_name="billingFrequency",
            )
            properties.billing_policies = AAZDictType(
                serialized_name="billingPolicies",
                flags={"read_only": True},
            )
            properties.billing_profile_display_name = AAZStrType(
                serialized_name="billingProfileDisplayName",
                flags={"read_only": True},
            )
            properties.billing_profile_id = AAZStrType(
                serialized_name="billingProfileId",
            )
            properties.billing_profile_name = AAZStrType(
                serialized_name="billingProfileName",
                flags={"read_only": True},
            )
            properties.consumption_cost_center = AAZStrType(
                serialized_name="consumptionCostCenter",
            )
            properties.customer_display_name = AAZStrType(
                serialized_name="customerDisplayName",
                flags={"read_only": True},
            )
            properties.customer_id = AAZStrType(
                serialized_name="customerId",
            )
            properties.customer_name = AAZStrType(
                serialized_name="customerName",
                flags={"read_only": True},
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.enrollment_account_display_name = AAZStrType(
                serialized_name="enrollmentAccountDisplayName",
                flags={"read_only": True},
            )
            properties.enrollment_account_id = AAZStrType(
                serialized_name="enrollmentAccountId",
                flags={"read_only": True},
            )
            properties.enrollment_account_subscription_details = AAZObjectType(
                serialized_name="enrollmentAccountSubscriptionDetails",
                flags={"client_flatten": True, "read_only": True},
            )
            properties.invoice_section_display_name = AAZStrType(
                serialized_name="invoiceSectionDisplayName",
                flags={"read_only": True},
            )
            properties.invoice_section_id = AAZStrType(
                serialized_name="invoiceSectionId",
            )
            properties.invoice_section_name = AAZStrType(
                serialized_name="invoiceSectionName",
                flags={"read_only": True},
            )
            properties.last_month_charges = AAZObjectType(
                serialized_name="lastMonthCharges",
                flags={"read_only": True},
            )
            _SplitHelper._build_schema_amount_read(properties.last_month_charges)
            properties.month_to_date_charges = AAZObjectType(
                serialized_name="monthToDateCharges",
                flags={"read_only": True},
            )
            _SplitHelper._build_schema_amount_read(properties.month_to_date_charges)
            properties.next_billing_cycle_details = AAZObjectType(
                serialized_name="nextBillingCycleDetails",
                flags={"read_only": True},
            )
            properties.offer_id = AAZStrType(
                serialized_name="offerId",
                flags={"read_only": True},
            )
            properties.operation_status = AAZStrType(
                serialized_name="operationStatus",
                flags={"read_only": True},
            )
            properties.product_category = AAZStrType(
                serialized_name="productCategory",
                flags={"read_only": True},
            )
            properties.product_type = AAZStrType(
                serialized_name="productType",
                flags={"read_only": True},
            )
            properties.product_type_id = AAZStrType(
                serialized_name="productTypeId",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.provisioning_tenant_id = AAZStrType(
                serialized_name="provisioningTenantId",
            )
            properties.purchase_date = AAZStrType(
                serialized_name="purchaseDate",
                flags={"read_only": True},
            )
            properties.quantity = AAZIntType()
            properties.renewal_term_details = AAZObjectType(
                serialized_name="renewalTermDetails",
                flags={"read_only": True},
            )
            properties.reseller = AAZObjectType(
                flags={"read_only": True},
            )
            properties.resource_uri = AAZStrType(
                serialized_name="resourceUri",
                flags={"read_only": True},
            )
            properties.sku_description = AAZStrType(
                serialized_name="skuDescription",
                flags={"read_only": True},
            )
            properties.sku_id = AAZStrType(
                serialized_name="skuId",
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
                flags={"read_only": True},
            )
            properties.suspension_reason_details = AAZListType(
                serialized_name="suspensionReasonDetails",
                flags={"read_only": True},
            )
            properties.suspension_reasons = AAZListType(
                serialized_name="suspensionReasons",
                flags={"read_only": True},
            )
            properties.system_overrides = AAZObjectType(
                serialized_name="systemOverrides",
            )
            properties.term_duration = AAZStrType(
                serialized_name="termDuration",
            )
            properties.term_end_date = AAZStrType(
                serialized_name="termEndDate",
                flags={"read_only": True},
            )
            properties.term_start_date = AAZStrType(
                serialized_name="termStartDate",
                flags={"read_only": True},
            )

            beneficiary = cls._schema_on_200.properties.beneficiary
            beneficiary.object_id = AAZStrType(
                serialized_name="objectId",
            )
            beneficiary.tenant_id = AAZStrType(
                serialized_name="tenantId",
            )

            billing_policies = cls._schema_on_200.properties.billing_policies
            billing_policies.Element = AAZStrType()

            enrollment_account_subscription_details = cls._schema_on_200.properties.enrollment_account_subscription_details
            enrollment_account_subscription_details.enrollment_account_start_date = AAZStrType(
                serialized_name="enrollmentAccountStartDate",
                flags={"read_only": True},
            )
            enrollment_account_subscription_details.subscription_enrollment_account_status = AAZStrType(
                serialized_name="subscriptionEnrollmentAccountStatus",
                flags={"read_only": True},
            )

            next_billing_cycle_details = cls._schema_on_200.properties.next_billing_cycle_details
            next_billing_cycle_details.billing_frequency = AAZStrType(
                serialized_name="billingFrequency",
                flags={"read_only": True},
            )

            renewal_term_details = cls._schema_on_200.properties.renewal_term_details
            renewal_term_details.billing_frequency = AAZStrType(
                serialized_name="billingFrequency",
                flags={"read_only": True},
            )
            renewal_term_details.product_id = AAZStrType(
                serialized_name="productId",
                flags={"read_only": True},
            )
            renewal_term_details.product_type_id = AAZStrType(
                serialized_name="productTypeId",
                flags={"read_only": True},
            )
            renewal_term_details.quantity = AAZIntType()
            renewal_term_details.sku_id = AAZStrType(
                serialized_name="skuId",
                flags={"read_only": True},
            )
            renewal_term_details.term_duration = AAZStrType(
                serialized_name="termDuration",
                flags={"read_only": True},
            )
            renewal_term_details.term_end_date = AAZStrType(
                serialized_name="termEndDate",
                flags={"read_only": True},
            )

            reseller = cls._schema_on_200.properties.reseller
            reseller.description = AAZStrType(
                flags={"read_only": True},
            )
            reseller.reseller_id = AAZStrType(
                serialized_name="resellerId",
                flags={"read_only": True},
            )

            suspension_reason_details = cls._schema_on_200.properties.suspension_reason_details
            suspension_reason_details.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.suspension_reason_details.Element
            _element.effective_date = AAZStrType(
                serialized_name="effectiveDate",
                flags={"read_only": True},
            )
            _element.reason = AAZStrType(
                flags={"read_only": True},
            )

            suspension_reasons = cls._schema_on_200.properties.suspension_reasons
            suspension_reasons.Element = AAZStrType()

            system_overrides = cls._schema_on_200.properties.system_overrides
            system_overrides.cancellation = AAZStrType(
                flags={"read_only": True},
            )
            system_overrides.cancellation_allowed_end_date = AAZStrType(
                serialized_name="cancellationAllowedEndDate",
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


class _SplitHelper:
    """Helper class for Split"""

    _schema_amount_read = None

    @classmethod
    def _build_schema_amount_read(cls, _schema):
        if cls._schema_amount_read is not None:
            _schema.currency = cls._schema_amount_read.currency
            _schema.value = cls._schema_amount_read.value
            return

        cls._schema_amount_read = _schema_amount_read = AAZObjectType(
            flags={"read_only": True}
        )

        amount_read = _schema_amount_read
        amount_read.currency = AAZStrType(
            flags={"read_only": True},
        )
        amount_read.value = AAZFloatType(
            flags={"read_only": True},
        )

        _schema.currency = cls._schema_amount_read.currency
        _schema.value = cls._schema_amount_read.value


__all__ = ["Split"]
