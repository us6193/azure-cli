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
    "billing reservation list-by-billing-profile",
)
class ListByBillingProfile(AAZCommand):
    """List the reservations for a billing profile and the roll up counts of reservations group by provisioning state.

    :example: ReservationsListByBillingProfile
        az billing reservation list-by-billing-profile --billing-account-name 00000000-0000-0000-0000-000000000000:00000000-0000-0000-0000-000000000000_2019-05-31 --billing-profile-name AAAA-AAAA-AAA-AAA --selected-state Succeeded
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/{}/billingprofiles/{}/reservations", "2024-04-01"],
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
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="May be used to filter by reservation properties. The filter supports 'eq', 'or', and 'and'. It does not currently support 'ne', 'gt', 'le', 'ge', or 'not'.",
        )
        _args_schema.order_by = AAZStrArg(
            options=["--order-by"],
            help="The orderby query option allows clients to request resources in a particular order.",
        )
        _args_schema.refresh_summary = AAZStrArg(
            options=["--refresh-summary"],
            help="To indicate whether to refresh the roll up counts of the reservations group by provisioning state",
        )
        _args_schema.selected_state = AAZStrArg(
            options=["--selected-state"],
            help="The selected provisioning state",
        )
        _args_schema.skiptoken = AAZFloatArg(
            options=["--skiptoken"],
            help="The number of reservations to skip from the list before returning results",
        )
        _args_schema.take = AAZFloatArg(
            options=["--take"],
            help="The number of reservations to return in API response.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ReservationsListByBillingProfile(ctx=self.ctx)()
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

    class ReservationsListByBillingProfile(AAZHttpOperation):
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
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/reservations",
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
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "orderBy", self.ctx.args.order_by,
                ),
                **self.serialize_query_param(
                    "refreshSummary", self.ctx.args.refresh_summary,
                ),
                **self.serialize_query_param(
                    "selectedState", self.ctx.args.selected_state,
                ),
                **self.serialize_query_param(
                    "skiptoken", self.ctx.args.skiptoken,
                ),
                **self.serialize_query_param(
                    "take", self.ctx.args.take,
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
            _schema_on_200.summary = AAZObjectType()
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            summary = cls._schema_on_200.summary
            summary.cancelled_count = AAZFloatType(
                serialized_name="cancelledCount",
                flags={"read_only": True},
            )
            summary.expired_count = AAZFloatType(
                serialized_name="expiredCount",
                flags={"read_only": True},
            )
            summary.expiring_count = AAZFloatType(
                serialized_name="expiringCount",
                flags={"read_only": True},
            )
            summary.failed_count = AAZFloatType(
                serialized_name="failedCount",
                flags={"read_only": True},
            )
            summary.no_benefit_count = AAZFloatType(
                serialized_name="noBenefitCount",
                flags={"read_only": True},
            )
            summary.pending_count = AAZFloatType(
                serialized_name="pendingCount",
                flags={"read_only": True},
            )
            summary.processing_count = AAZFloatType(
                serialized_name="processingCount",
                flags={"read_only": True},
            )
            summary.succeeded_count = AAZFloatType(
                serialized_name="succeededCount",
                flags={"read_only": True},
            )
            summary.warning_count = AAZFloatType(
                serialized_name="warningCount",
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZIntType()
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.applied_scope_properties = AAZObjectType(
                serialized_name="appliedScopeProperties",
            )
            _ListByBillingProfileHelper._build_schema_reservation_applied_scope_properties_read(properties.applied_scope_properties)
            properties.applied_scope_type = AAZStrType(
                serialized_name="appliedScopeType",
                flags={"read_only": True},
            )
            properties.applied_scopes = AAZListType(
                serialized_name="appliedScopes",
            )
            properties.archived = AAZBoolType()
            properties.benefit_start_time = AAZStrType(
                serialized_name="benefitStartTime",
            )
            properties.billing_plan = AAZStrType(
                serialized_name="billingPlan",
            )
            properties.billing_scope_id = AAZStrType(
                serialized_name="billingScopeId",
                flags={"read_only": True},
            )
            properties.capabilities = AAZStrType()
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"read_only": True},
            )
            properties.display_provisioning_state = AAZStrType(
                serialized_name="displayProvisioningState",
                flags={"read_only": True},
            )
            properties.effective_date_time = AAZStrType(
                serialized_name="effectiveDateTime",
                flags={"read_only": True},
            )
            properties.expiry_date = AAZStrType(
                serialized_name="expiryDate",
                flags={"read_only": True},
            )
            properties.expiry_date_time = AAZStrType(
                serialized_name="expiryDateTime",
            )
            properties.extended_status_info = AAZObjectType(
                serialized_name="extendedStatusInfo",
            )
            properties.instance_flexibility = AAZStrType(
                serialized_name="instanceFlexibility",
            )
            properties.last_updated_date_time = AAZStrType(
                serialized_name="lastUpdatedDateTime",
                flags={"read_only": True},
            )
            properties.merge_properties = AAZObjectType(
                serialized_name="mergeProperties",
            )
            properties.product_code = AAZStrType(
                serialized_name="productCode",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.provisioning_sub_state = AAZStrType(
                serialized_name="provisioningSubState",
                flags={"read_only": True},
            )
            properties.purchase_date = AAZStrType(
                serialized_name="purchaseDate",
            )
            properties.purchase_date_time = AAZStrType(
                serialized_name="purchaseDateTime",
            )
            properties.quantity = AAZFloatType(
                flags={"read_only": True},
            )
            properties.renew = AAZBoolType(
                flags={"read_only": True},
            )
            properties.renew_destination = AAZStrType(
                serialized_name="renewDestination",
            )
            properties.renew_properties = AAZObjectType(
                serialized_name="renewProperties",
            )
            properties.renew_source = AAZStrType(
                serialized_name="renewSource",
                flags={"read_only": True},
            )
            properties.reserved_resource_type = AAZStrType(
                serialized_name="reservedResourceType",
                flags={"read_only": True},
            )
            properties.review_date_time = AAZStrType(
                serialized_name="reviewDateTime",
            )
            properties.sku_description = AAZStrType(
                serialized_name="skuDescription",
                flags={"read_only": True},
            )
            properties.split_properties = AAZObjectType(
                serialized_name="splitProperties",
            )
            properties.swap_properties = AAZObjectType(
                serialized_name="swapProperties",
            )
            properties.term = AAZStrType(
                flags={"read_only": True},
            )
            properties.user_friendly_applied_scope_type = AAZStrType(
                serialized_name="userFriendlyAppliedScopeType",
                flags={"read_only": True},
            )
            properties.user_friendly_renew_state = AAZStrType(
                serialized_name="userFriendlyRenewState",
                flags={"read_only": True},
            )
            properties.utilization = AAZObjectType(
                flags={"client_flatten": True, "read_only": True},
            )

            applied_scopes = cls._schema_on_200.value.Element.properties.applied_scopes
            applied_scopes.Element = AAZStrType(
                flags={"read_only": True},
            )

            extended_status_info = cls._schema_on_200.value.Element.properties.extended_status_info
            extended_status_info.message = AAZStrType()
            extended_status_info.properties = AAZObjectType()
            extended_status_info.status_code = AAZStrType(
                serialized_name="statusCode",
            )

            properties = cls._schema_on_200.value.Element.properties.extended_status_info.properties
            properties.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
            )

            merge_properties = cls._schema_on_200.value.Element.properties.merge_properties
            merge_properties.merge_destination = AAZStrType(
                serialized_name="mergeDestination",
            )
            merge_properties.merge_sources = AAZListType(
                serialized_name="mergeSources",
            )

            merge_sources = cls._schema_on_200.value.Element.properties.merge_properties.merge_sources
            merge_sources.Element = AAZStrType()

            renew_properties = cls._schema_on_200.value.Element.properties.renew_properties
            renew_properties.billing_currency_total = AAZObjectType(
                serialized_name="billingCurrencyTotal",
            )
            _ListByBillingProfileHelper._build_schema_price_read(renew_properties.billing_currency_total)
            renew_properties.pricing_currency_total = AAZObjectType(
                serialized_name="pricingCurrencyTotal",
            )
            _ListByBillingProfileHelper._build_schema_price_read(renew_properties.pricing_currency_total)
            renew_properties.purchase_properties = AAZObjectType(
                serialized_name="purchaseProperties",
            )

            purchase_properties = cls._schema_on_200.value.Element.properties.renew_properties.purchase_properties
            purchase_properties.location = AAZStrType()
            purchase_properties.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            purchase_properties.sku = AAZObjectType()

            properties = cls._schema_on_200.value.Element.properties.renew_properties.purchase_properties.properties
            properties.applied_scope_properties = AAZObjectType(
                serialized_name="appliedScopeProperties",
            )
            _ListByBillingProfileHelper._build_schema_reservation_applied_scope_properties_read(properties.applied_scope_properties)
            properties.applied_scope_type = AAZStrType(
                serialized_name="appliedScopeType",
            )
            properties.applied_scopes = AAZListType(
                serialized_name="appliedScopes",
            )
            properties.billing_plan = AAZStrType(
                serialized_name="billingPlan",
            )
            properties.billing_scope_id = AAZStrType(
                serialized_name="billingScopeId",
                flags={"read_only": True},
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.quantity = AAZIntType()
            properties.renew = AAZBoolType()
            properties.reserved_resource_properties = AAZObjectType(
                serialized_name="reservedResourceProperties",
                flags={"client_flatten": True},
            )
            properties.reserved_resource_type = AAZStrType(
                serialized_name="reservedResourceType",
                flags={"read_only": True},
            )
            properties.review_date_time = AAZStrType(
                serialized_name="reviewDateTime",
            )
            properties.term = AAZStrType(
                flags={"read_only": True},
            )

            applied_scopes = cls._schema_on_200.value.Element.properties.renew_properties.purchase_properties.properties.applied_scopes
            applied_scopes.Element = AAZStrType()

            reserved_resource_properties = cls._schema_on_200.value.Element.properties.renew_properties.purchase_properties.properties.reserved_resource_properties
            reserved_resource_properties.instance_flexibility = AAZStrType(
                serialized_name="instanceFlexibility",
            )

            sku = cls._schema_on_200.value.Element.properties.renew_properties.purchase_properties.sku
            sku.name = AAZStrType()

            split_properties = cls._schema_on_200.value.Element.properties.split_properties
            split_properties.split_destinations = AAZListType(
                serialized_name="splitDestinations",
            )
            split_properties.split_source = AAZStrType(
                serialized_name="splitSource",
            )

            split_destinations = cls._schema_on_200.value.Element.properties.split_properties.split_destinations
            split_destinations.Element = AAZStrType()

            swap_properties = cls._schema_on_200.value.Element.properties.swap_properties
            swap_properties.swap_destination = AAZStrType(
                serialized_name="swapDestination",
            )
            swap_properties.swap_source = AAZStrType(
                serialized_name="swapSource",
            )

            utilization = cls._schema_on_200.value.Element.properties.utilization
            utilization.aggregates = AAZListType()
            utilization.trend = AAZStrType(
                flags={"read_only": True},
            )

            aggregates = cls._schema_on_200.value.Element.properties.utilization.aggregates
            aggregates.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.utilization.aggregates.Element
            _element.grain = AAZFloatType(
                flags={"read_only": True},
            )
            _element.grain_unit = AAZStrType(
                serialized_name="grainUnit",
                flags={"read_only": True},
            )
            _element.value = AAZFloatType(
                flags={"read_only": True},
            )
            _element.value_unit = AAZStrType(
                serialized_name="valueUnit",
                flags={"read_only": True},
            )

            sku = cls._schema_on_200.value.Element.sku
            sku.name = AAZStrType(
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


class _ListByBillingProfileHelper:
    """Helper class for ListByBillingProfile"""

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

    _schema_reservation_applied_scope_properties_read = None

    @classmethod
    def _build_schema_reservation_applied_scope_properties_read(cls, _schema):
        if cls._schema_reservation_applied_scope_properties_read is not None:
            _schema.display_name = cls._schema_reservation_applied_scope_properties_read.display_name
            _schema.management_group_id = cls._schema_reservation_applied_scope_properties_read.management_group_id
            _schema.resource_group_id = cls._schema_reservation_applied_scope_properties_read.resource_group_id
            _schema.subscription_id = cls._schema_reservation_applied_scope_properties_read.subscription_id
            _schema.tenant_id = cls._schema_reservation_applied_scope_properties_read.tenant_id
            return

        cls._schema_reservation_applied_scope_properties_read = _schema_reservation_applied_scope_properties_read = AAZObjectType()

        reservation_applied_scope_properties_read = _schema_reservation_applied_scope_properties_read
        reservation_applied_scope_properties_read.display_name = AAZStrType(
            serialized_name="displayName",
        )
        reservation_applied_scope_properties_read.management_group_id = AAZStrType(
            serialized_name="managementGroupId",
        )
        reservation_applied_scope_properties_read.resource_group_id = AAZStrType(
            serialized_name="resourceGroupId",
        )
        reservation_applied_scope_properties_read.subscription_id = AAZStrType(
            serialized_name="subscriptionId",
        )
        reservation_applied_scope_properties_read.tenant_id = AAZStrType(
            serialized_name="tenantId",
        )

        _schema.display_name = cls._schema_reservation_applied_scope_properties_read.display_name
        _schema.management_group_id = cls._schema_reservation_applied_scope_properties_read.management_group_id
        _schema.resource_group_id = cls._schema_reservation_applied_scope_properties_read.resource_group_id
        _schema.subscription_id = cls._schema_reservation_applied_scope_properties_read.subscription_id
        _schema.tenant_id = cls._schema_reservation_applied_scope_properties_read.tenant_id


__all__ = ["ListByBillingProfile"]