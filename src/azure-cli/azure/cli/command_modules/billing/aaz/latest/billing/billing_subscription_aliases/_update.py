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
    "billing billing-subscription-aliases update",
)
class Update(AAZCommand):
    """Update a billing subscription by its alias ID.  The operation is supported for seat based billing subscriptions.
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/{}/billingsubscriptionaliases/{}", "2024-04-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.alias_name = AAZStrArg(
            options=["--alias-name"],
            help="The ID that uniquely identifies a subscription alias.",
            required=True,
        )
        _args_schema.billing_account_name = AAZStrArg(
            options=["--billing-account-name"],
            help="The ID that uniquely identifies a billing account.",
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \\ ? /",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.auto_renew = AAZStrArg(
            options=["--auto-renew"],
            arg_group="Properties",
            help="Indicates whether auto renewal is turned on or off for a product.",
            nullable=True,
            enum={"Off": "Off", "On": "On"},
        )
        _args_schema.beneficiary = AAZObjectArg(
            options=["--beneficiary"],
            arg_group="Properties",
            help="The beneficiary of the billing subscription.",
            nullable=True,
        )
        _args_schema.beneficiary_tenant_id = AAZStrArg(
            options=["--beneficiary-tenant-id"],
            arg_group="Properties",
            help="The provisioning tenant of the subscription.",
            nullable=True,
        )
        _args_schema.billing_frequency = AAZStrArg(
            options=["--billing-frequency"],
            arg_group="Properties",
            help="The billing frequency in ISO8601 format of product in the subscription. Example: P1M, P3M, P1Y",
            nullable=True,
        )
        _args_schema.billing_profile_id = AAZStrArg(
            options=["--billing-profile-id"],
            arg_group="Properties",
            help="The fully qualified ID that uniquely identifies a billing profile.",
            nullable=True,
        )
        _args_schema.consumption_cost_center = AAZStrArg(
            options=["--consumption-cost-center"],
            arg_group="Properties",
            help="The cost center applied to the subscription. This field is only available for consumption subscriptions of Microsoft Customer Agreement or Enterprise Agreement Type billing accounts.",
            nullable=True,
        )
        _args_schema.customer_id = AAZStrArg(
            options=["--customer-id"],
            arg_group="Properties",
            help="The fully qualified ID that uniquely identifies a customer.",
            nullable=True,
        )
        _args_schema.display_name = AAZStrArg(
            options=["--display-name"],
            arg_group="Properties",
            help="The name of the billing subscription.",
            nullable=True,
        )
        _args_schema.invoice_section_id = AAZStrArg(
            options=["--invoice-section-id"],
            arg_group="Properties",
            help="The fully qualified ID that uniquely identifies an invoice section.",
            nullable=True,
        )
        _args_schema.product_type_id = AAZStrArg(
            options=["--product-type-id"],
            arg_group="Properties",
            help="Id of the product for which the subscription is purchased.",
            nullable=True,
        )
        _args_schema.provisioning_tenant_id = AAZStrArg(
            options=["--provisioning-tenant-id"],
            arg_group="Properties",
            help="The tenant in which the subscription is provisioned.",
            nullable=True,
        )
        _args_schema.quantity = AAZIntArg(
            options=["--quantity"],
            arg_group="Properties",
            help="The quantity of licenses or fulfillment units for the subscription.",
            nullable=True,
        )
        _args_schema.sku_id = AAZStrArg(
            options=["--sku-id"],
            arg_group="Properties",
            help="The SKU ID of the product for which the subscription is purchased. This field is is only available  for Microsoft Customer Agreement billing accounts.",
            nullable=True,
        )
        _args_schema.term_duration = AAZStrArg(
            options=["--term-duration"],
            arg_group="Properties",
            help="The duration in ISO8601 format for which you can use the subscription. Example: P1M, P3M, P1Y",
            nullable=True,
        )

        beneficiary = cls._args_schema.beneficiary
        beneficiary.object_id = AAZStrArg(
            options=["object-id"],
            help="The ID that uniquely identifies a user in a tenant.",
            nullable=True,
        )
        beneficiary.tenant_id = AAZStrArg(
            options=["tenant-id"],
            help="The ID that uniquely identifies a tenant.",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.BillingSubscriptionsAliasesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.BillingSubscriptionsAliasesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class BillingSubscriptionsAliasesGet(AAZHttpOperation):
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
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingSubscriptionAliases/{aliasName}",
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
                    "aliasName", self.ctx.args.alias_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "billingAccountName", self.ctx.args.billing_account_name,
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
            _UpdateHelper._build_schema_billing_subscription_alias_read(cls._schema_on_200)

            return cls._schema_on_200

    class BillingSubscriptionsAliasesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingSubscriptionAliases/{aliasName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "aliasName", self.ctx.args.alias_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "billingAccountName", self.ctx.args.billing_account_name,
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
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_billing_subscription_alias_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("autoRenew", AAZStrType, ".auto_renew")
                properties.set_prop("beneficiary", AAZObjectType, ".beneficiary")
                properties.set_prop("beneficiaryTenantId", AAZStrType, ".beneficiary_tenant_id")
                properties.set_prop("billingFrequency", AAZStrType, ".billing_frequency")
                properties.set_prop("billingProfileId", AAZStrType, ".billing_profile_id")
                properties.set_prop("consumptionCostCenter", AAZStrType, ".consumption_cost_center")
                properties.set_prop("customerId", AAZStrType, ".customer_id")
                properties.set_prop("displayName", AAZStrType, ".display_name")
                properties.set_prop("invoiceSectionId", AAZStrType, ".invoice_section_id")
                properties.set_prop("productTypeId", AAZStrType, ".product_type_id")
                properties.set_prop("provisioningTenantId", AAZStrType, ".provisioning_tenant_id")
                properties.set_prop("quantity", AAZIntType, ".quantity")
                properties.set_prop("skuId", AAZStrType, ".sku_id")
                properties.set_prop("termDuration", AAZStrType, ".term_duration")

            beneficiary = _builder.get(".properties.beneficiary")
            if beneficiary is not None:
                beneficiary.set_prop("objectId", AAZStrType, ".object_id")
                beneficiary.set_prop("tenantId", AAZStrType, ".tenant_id")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

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

    _schema_billing_subscription_alias_read = None

    @classmethod
    def _build_schema_billing_subscription_alias_read(cls, _schema):
        if cls._schema_billing_subscription_alias_read is not None:
            _schema.id = cls._schema_billing_subscription_alias_read.id
            _schema.name = cls._schema_billing_subscription_alias_read.name
            _schema.properties = cls._schema_billing_subscription_alias_read.properties
            _schema.system_data = cls._schema_billing_subscription_alias_read.system_data
            _schema.tags = cls._schema_billing_subscription_alias_read.tags
            _schema.type = cls._schema_billing_subscription_alias_read.type
            return

        cls._schema_billing_subscription_alias_read = _schema_billing_subscription_alias_read = AAZObjectType()

        billing_subscription_alias_read = _schema_billing_subscription_alias_read
        billing_subscription_alias_read.id = AAZStrType(
            flags={"read_only": True},
        )
        billing_subscription_alias_read.name = AAZStrType(
            flags={"read_only": True},
        )
        billing_subscription_alias_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        billing_subscription_alias_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        billing_subscription_alias_read.tags = AAZDictType()
        billing_subscription_alias_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_billing_subscription_alias_read.properties
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
        properties.billing_subscription_id = AAZStrType(
            serialized_name="billingSubscriptionId",
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
        cls._build_schema_amount_read(properties.last_month_charges)
        properties.month_to_date_charges = AAZObjectType(
            serialized_name="monthToDateCharges",
            flags={"read_only": True},
        )
        cls._build_schema_amount_read(properties.month_to_date_charges)
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

        beneficiary = _schema_billing_subscription_alias_read.properties.beneficiary
        beneficiary.object_id = AAZStrType(
            serialized_name="objectId",
        )
        beneficiary.tenant_id = AAZStrType(
            serialized_name="tenantId",
        )

        billing_policies = _schema_billing_subscription_alias_read.properties.billing_policies
        billing_policies.Element = AAZStrType()

        enrollment_account_subscription_details = _schema_billing_subscription_alias_read.properties.enrollment_account_subscription_details
        enrollment_account_subscription_details.enrollment_account_start_date = AAZStrType(
            serialized_name="enrollmentAccountStartDate",
            flags={"read_only": True},
        )
        enrollment_account_subscription_details.subscription_enrollment_account_status = AAZStrType(
            serialized_name="subscriptionEnrollmentAccountStatus",
            flags={"read_only": True},
        )

        next_billing_cycle_details = _schema_billing_subscription_alias_read.properties.next_billing_cycle_details
        next_billing_cycle_details.billing_frequency = AAZStrType(
            serialized_name="billingFrequency",
            flags={"read_only": True},
        )

        renewal_term_details = _schema_billing_subscription_alias_read.properties.renewal_term_details
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

        reseller = _schema_billing_subscription_alias_read.properties.reseller
        reseller.description = AAZStrType(
            flags={"read_only": True},
        )
        reseller.reseller_id = AAZStrType(
            serialized_name="resellerId",
            flags={"read_only": True},
        )

        suspension_reason_details = _schema_billing_subscription_alias_read.properties.suspension_reason_details
        suspension_reason_details.Element = AAZObjectType()

        _element = _schema_billing_subscription_alias_read.properties.suspension_reason_details.Element
        _element.effective_date = AAZStrType(
            serialized_name="effectiveDate",
            flags={"read_only": True},
        )
        _element.reason = AAZStrType(
            flags={"read_only": True},
        )

        suspension_reasons = _schema_billing_subscription_alias_read.properties.suspension_reasons
        suspension_reasons.Element = AAZStrType()

        system_overrides = _schema_billing_subscription_alias_read.properties.system_overrides
        system_overrides.cancellation = AAZStrType(
            flags={"read_only": True},
        )
        system_overrides.cancellation_allowed_end_date = AAZStrType(
            serialized_name="cancellationAllowedEndDate",
            flags={"read_only": True},
        )

        system_data = _schema_billing_subscription_alias_read.system_data
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

        tags = _schema_billing_subscription_alias_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_billing_subscription_alias_read.id
        _schema.name = cls._schema_billing_subscription_alias_read.name
        _schema.properties = cls._schema_billing_subscription_alias_read.properties
        _schema.system_data = cls._schema_billing_subscription_alias_read.system_data
        _schema.tags = cls._schema_billing_subscription_alias_read.tags
        _schema.type = cls._schema_billing_subscription_alias_read.type


__all__ = ["Update"]