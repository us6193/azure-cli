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
    "billing profile wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/{}/billingprofiles/{}", "2024-04-01"],
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
        _args_schema.billing_profile_name = AAZStrArg(
            options=["--billing-profile-name"],
            help="The ID that uniquely identifies a billing profile.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-_]{1,128}$",
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.BillingProfilesGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class BillingProfilesGet(AAZHttpOperation):
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
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}",
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
            properties.bill_to = AAZObjectType(
                serialized_name="billTo",
            )
            properties.billing_relationship_type = AAZStrType(
                serialized_name="billingRelationshipType",
                flags={"read_only": True},
            )
            properties.currency = AAZStrType(
                flags={"read_only": True},
            )
            properties.current_payment_term = AAZObjectType(
                serialized_name="currentPaymentTerm",
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.enabled_azure_plans = AAZListType(
                serialized_name="enabledAzurePlans",
            )
            properties.has_read_access = AAZBoolType(
                serialized_name="hasReadAccess",
                flags={"read_only": True},
            )
            properties.indirect_relationship_info = AAZObjectType(
                serialized_name="indirectRelationshipInfo",
            )
            properties.invoice_day = AAZIntType(
                serialized_name="invoiceDay",
                flags={"read_only": True},
            )
            properties.invoice_email_opt_in = AAZBoolType(
                serialized_name="invoiceEmailOptIn",
            )
            properties.invoice_recipients = AAZListType(
                serialized_name="invoiceRecipients",
            )
            properties.other_payment_terms = AAZListType(
                serialized_name="otherPaymentTerms",
                flags={"read_only": True},
            )
            properties.po_number = AAZStrType(
                serialized_name="poNumber",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.ship_to = AAZObjectType(
                serialized_name="shipTo",
            )
            properties.sold_to = AAZObjectType(
                serialized_name="soldTo",
            )
            properties.spending_limit = AAZStrType(
                serialized_name="spendingLimit",
                flags={"read_only": True},
            )
            properties.spending_limit_details = AAZListType(
                serialized_name="spendingLimitDetails",
                flags={"read_only": True},
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.status_reason_code = AAZStrType(
                serialized_name="statusReasonCode",
                flags={"read_only": True},
            )
            properties.system_id = AAZStrType(
                serialized_name="systemId",
                flags={"read_only": True},
            )
            properties.tags = AAZDictType()
            properties.target_clouds = AAZListType(
                serialized_name="targetClouds",
                flags={"read_only": True},
            )

            bill_to = cls._schema_on_200.properties.bill_to
            bill_to.address_line1 = AAZStrType(
                serialized_name="addressLine1",
                flags={"required": True},
            )
            bill_to.address_line2 = AAZStrType(
                serialized_name="addressLine2",
            )
            bill_to.address_line3 = AAZStrType(
                serialized_name="addressLine3",
            )
            bill_to.city = AAZStrType()
            bill_to.company_name = AAZStrType(
                serialized_name="companyName",
            )
            bill_to.country = AAZStrType(
                flags={"required": True},
            )
            bill_to.district = AAZStrType()
            bill_to.email = AAZStrType()
            bill_to.first_name = AAZStrType(
                serialized_name="firstName",
            )
            bill_to.is_valid_address = AAZBoolType(
                serialized_name="isValidAddress",
            )
            bill_to.last_name = AAZStrType(
                serialized_name="lastName",
            )
            bill_to.middle_name = AAZStrType(
                serialized_name="middleName",
            )
            bill_to.phone_number = AAZStrType(
                serialized_name="phoneNumber",
            )
            bill_to.postal_code = AAZStrType(
                serialized_name="postalCode",
            )
            bill_to.region = AAZStrType()

            current_payment_term = cls._schema_on_200.properties.current_payment_term
            current_payment_term.end_date = AAZStrType(
                serialized_name="endDate",
            )
            current_payment_term.is_default = AAZBoolType(
                serialized_name="isDefault",
                flags={"read_only": True},
            )
            current_payment_term.start_date = AAZStrType(
                serialized_name="startDate",
            )
            current_payment_term.term = AAZStrType()

            enabled_azure_plans = cls._schema_on_200.properties.enabled_azure_plans
            enabled_azure_plans.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.enabled_azure_plans.Element
            _element.product_id = AAZStrType(
                serialized_name="productId",
            )
            _element.sku_description = AAZStrType(
                serialized_name="skuDescription",
            )
            _element.sku_id = AAZStrType(
                serialized_name="skuId",
            )

            indirect_relationship_info = cls._schema_on_200.properties.indirect_relationship_info
            indirect_relationship_info.billing_account_name = AAZStrType(
                serialized_name="billingAccountName",
            )
            indirect_relationship_info.billing_profile_name = AAZStrType(
                serialized_name="billingProfileName",
            )
            indirect_relationship_info.display_name = AAZStrType(
                serialized_name="displayName",
            )

            invoice_recipients = cls._schema_on_200.properties.invoice_recipients
            invoice_recipients.Element = AAZStrType()

            other_payment_terms = cls._schema_on_200.properties.other_payment_terms
            other_payment_terms.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.other_payment_terms.Element
            _element.end_date = AAZStrType(
                serialized_name="endDate",
            )
            _element.is_default = AAZBoolType(
                serialized_name="isDefault",
                flags={"read_only": True},
            )
            _element.start_date = AAZStrType(
                serialized_name="startDate",
            )
            _element.term = AAZStrType()

            ship_to = cls._schema_on_200.properties.ship_to
            ship_to.address_line1 = AAZStrType(
                serialized_name="addressLine1",
                flags={"required": True},
            )
            ship_to.address_line2 = AAZStrType(
                serialized_name="addressLine2",
            )
            ship_to.address_line3 = AAZStrType(
                serialized_name="addressLine3",
            )
            ship_to.city = AAZStrType()
            ship_to.company_name = AAZStrType(
                serialized_name="companyName",
            )
            ship_to.country = AAZStrType(
                flags={"required": True},
            )
            ship_to.district = AAZStrType()
            ship_to.email = AAZStrType()
            ship_to.first_name = AAZStrType(
                serialized_name="firstName",
            )
            ship_to.is_valid_address = AAZBoolType(
                serialized_name="isValidAddress",
            )
            ship_to.last_name = AAZStrType(
                serialized_name="lastName",
            )
            ship_to.middle_name = AAZStrType(
                serialized_name="middleName",
            )
            ship_to.phone_number = AAZStrType(
                serialized_name="phoneNumber",
            )
            ship_to.postal_code = AAZStrType(
                serialized_name="postalCode",
            )
            ship_to.region = AAZStrType()

            sold_to = cls._schema_on_200.properties.sold_to
            sold_to.address_line1 = AAZStrType(
                serialized_name="addressLine1",
                flags={"required": True},
            )
            sold_to.address_line2 = AAZStrType(
                serialized_name="addressLine2",
            )
            sold_to.address_line3 = AAZStrType(
                serialized_name="addressLine3",
            )
            sold_to.city = AAZStrType()
            sold_to.company_name = AAZStrType(
                serialized_name="companyName",
            )
            sold_to.country = AAZStrType(
                flags={"required": True},
            )
            sold_to.district = AAZStrType()
            sold_to.email = AAZStrType()
            sold_to.first_name = AAZStrType(
                serialized_name="firstName",
            )
            sold_to.is_valid_address = AAZBoolType(
                serialized_name="isValidAddress",
            )
            sold_to.last_name = AAZStrType(
                serialized_name="lastName",
            )
            sold_to.middle_name = AAZStrType(
                serialized_name="middleName",
            )
            sold_to.phone_number = AAZStrType(
                serialized_name="phoneNumber",
            )
            sold_to.postal_code = AAZStrType(
                serialized_name="postalCode",
            )
            sold_to.region = AAZStrType()

            spending_limit_details = cls._schema_on_200.properties.spending_limit_details
            spending_limit_details.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.spending_limit_details.Element
            _element.amount = AAZFloatType()
            _element.currency = AAZStrType()
            _element.end_date = AAZStrType(
                serialized_name="endDate",
            )
            _element.start_date = AAZStrType(
                serialized_name="startDate",
            )
            _element.status = AAZStrType()
            _element.type = AAZStrType()

            tags = cls._schema_on_200.properties.tags
            tags.Element = AAZStrType()

            target_clouds = cls._schema_on_200.properties.target_clouds
            target_clouds.Element = AAZStrType()

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


class _WaitHelper:
    """Helper class for Wait"""


__all__ = ["Wait"]
