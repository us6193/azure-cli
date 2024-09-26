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
    "billing request get",
)
class Get(AAZCommand):
    """Get a billing request by its ID.

    :example: BillingRequestsGet
        az billing request get --billing-request-name 00000000-0000-0000-0000-000000000000
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingrequests/{}", "2024-04-01"],
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
        _args_schema.billing_request_name = AAZStrArg(
            options=["--billing-request-name"],
            help="The ID that uniquely identifies a billing request.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$",
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.BillingRequestsGet(ctx=self.ctx)()
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

    class BillingRequestsGet(AAZHttpOperation):
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
                "/providers/Microsoft.Billing/billingRequests/{billingRequestName}",
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
                    "billingRequestName", self.ctx.args.billing_request_name,
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
            properties.additional_information = AAZDictType(
                serialized_name="additionalInformation",
            )
            properties.billing_account_display_name = AAZStrType(
                serialized_name="billingAccountDisplayName",
                flags={"read_only": True},
            )
            properties.billing_account_id = AAZStrType(
                serialized_name="billingAccountId",
                flags={"read_only": True},
            )
            properties.billing_account_name = AAZStrType(
                serialized_name="billingAccountName",
                flags={"read_only": True},
            )
            properties.billing_account_primary_billing_tenant_id = AAZStrType(
                serialized_name="billingAccountPrimaryBillingTenantId",
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
            properties.billing_profile_name = AAZStrType(
                serialized_name="billingProfileName",
                flags={"read_only": True},
            )
            properties.billing_scope = AAZStrType(
                serialized_name="billingScope",
                flags={"read_only": True},
            )
            properties.created_by = AAZObjectType(
                serialized_name="createdBy",
            )
            properties.creation_date = AAZStrType(
                serialized_name="creationDate",
                flags={"read_only": True},
            )
            properties.customer_display_name = AAZStrType(
                serialized_name="customerDisplayName",
                flags={"read_only": True},
            )
            properties.customer_id = AAZStrType(
                serialized_name="customerId",
                flags={"read_only": True},
            )
            properties.customer_name = AAZStrType(
                serialized_name="customerName",
                flags={"read_only": True},
            )
            properties.decision_reason = AAZStrType(
                serialized_name="decisionReason",
            )
            properties.expiration_date = AAZStrType(
                serialized_name="expirationDate",
                flags={"read_only": True},
            )
            properties.invoice_section_display_name = AAZStrType(
                serialized_name="invoiceSectionDisplayName",
                flags={"read_only": True},
            )
            properties.invoice_section_id = AAZStrType(
                serialized_name="invoiceSectionId",
                flags={"read_only": True},
            )
            properties.invoice_section_name = AAZStrType(
                serialized_name="invoiceSectionName",
                flags={"read_only": True},
            )
            properties.justification = AAZStrType()
            properties.last_updated_by = AAZObjectType(
                serialized_name="lastUpdatedBy",
            )
            properties.last_updated_date = AAZStrType(
                serialized_name="lastUpdatedDate",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.recipients = AAZListType()
            properties.request_scope = AAZStrType(
                serialized_name="requestScope",
            )
            properties.reviewal_date = AAZStrType(
                serialized_name="reviewalDate",
                flags={"read_only": True},
            )
            properties.reviewed_by = AAZObjectType(
                serialized_name="reviewedBy",
            )
            properties.status = AAZStrType()
            properties.subscription_display_name = AAZStrType(
                serialized_name="subscriptionDisplayName",
                flags={"read_only": True},
            )
            properties.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
                flags={"read_only": True},
            )
            properties.subscription_name = AAZStrType(
                serialized_name="subscriptionName",
                flags={"read_only": True},
            )
            properties.type = AAZStrType()

            additional_information = cls._schema_on_200.properties.additional_information
            additional_information.Element = AAZStrType()

            created_by = cls._schema_on_200.properties.created_by
            created_by.object_id = AAZStrType(
                serialized_name="objectId",
            )
            created_by.tenant_id = AAZStrType(
                serialized_name="tenantId",
            )
            created_by.upn = AAZStrType()

            last_updated_by = cls._schema_on_200.properties.last_updated_by
            last_updated_by.object_id = AAZStrType(
                serialized_name="objectId",
            )
            last_updated_by.tenant_id = AAZStrType(
                serialized_name="tenantId",
            )
            last_updated_by.upn = AAZStrType()

            recipients = cls._schema_on_200.properties.recipients
            recipients.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.recipients.Element
            _element.object_id = AAZStrType(
                serialized_name="objectId",
            )
            _element.tenant_id = AAZStrType(
                serialized_name="tenantId",
            )
            _element.upn = AAZStrType()

            reviewed_by = cls._schema_on_200.properties.reviewed_by
            reviewed_by.object_id = AAZStrType(
                serialized_name="objectId",
            )
            reviewed_by.tenant_id = AAZStrType(
                serialized_name="tenantId",
            )
            reviewed_by.upn = AAZStrType()

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


class _GetHelper:
    """Helper class for Get"""


__all__ = ["Get"]