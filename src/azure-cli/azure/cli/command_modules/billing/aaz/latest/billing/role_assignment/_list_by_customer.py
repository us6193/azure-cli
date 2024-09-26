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
    "billing role-assignment list-by-customer",
)
class ListByCustomer(AAZCommand):
    """List the role assignments for the caller on customer. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement.

    :example: BillingRoleAssignmentListByCustomer
        az billing role-assignment list-by-customer --billing-account-name 00000000-0000-0000-0000-000000000000:00000000-0000-0000-0000-000000000000_2018-09-30 --billing-profile-name BKM6-54VH-BG7-PGB --customer-name 703ab484-dda2-4402-827b-a74513b61e2d
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/{}/billingprofiles/{}/customers/{}/billingroleassignments", "2024-04-01"],
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
        _args_schema.customer_name = AAZStrArg(
            options=["--customer-name"],
            help="The ID that uniquely identifies a customer.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-_]{1,128}$",
            ),
        )
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="The filter query option allows clients to filter a collection of resources that are addressed by a request URL.",
        )
        _args_schema.skip = AAZIntArg(
            options=["--skip"],
            help="The skip query option requests the number of items in the queried collection that are to be skipped and not included in the result.",
        )
        _args_schema.top = AAZIntArg(
            options=["--top"],
            help="The top query option requests the number of items in the queried collection to be included in the result. The maximum supported value for top is 50.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.BillingRoleAssignmentsListByCustomer(ctx=self.ctx)()
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

    class BillingRoleAssignmentsListByCustomer(AAZHttpOperation):
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
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/customers/{customerName}/billingRoleAssignments",
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
                    "customerName", self.ctx.args.customer_name,
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
                    "skip", self.ctx.args.skip,
                ),
                **self.serialize_query_param(
                    "top", self.ctx.args.top,
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
            properties.billing_account_display_name = AAZStrType(
                serialized_name="billingAccountDisplayName",
                flags={"read_only": True},
            )
            properties.billing_account_id = AAZStrType(
                serialized_name="billingAccountId",
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
            properties.billing_request_id = AAZStrType(
                serialized_name="billingRequestId",
                flags={"read_only": True},
            )
            properties.created_by_principal_id = AAZStrType(
                serialized_name="createdByPrincipalId",
                flags={"read_only": True},
            )
            properties.created_by_principal_puid = AAZStrType(
                serialized_name="createdByPrincipalPuid",
                flags={"read_only": True},
            )
            properties.created_by_principal_tenant_id = AAZStrType(
                serialized_name="createdByPrincipalTenantId",
                flags={"read_only": True},
            )
            properties.created_by_user_email_address = AAZStrType(
                serialized_name="createdByUserEmailAddress",
                flags={"read_only": True},
            )
            properties.created_on = AAZStrType(
                serialized_name="createdOn",
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
            properties.invoice_section_display_name = AAZStrType(
                serialized_name="invoiceSectionDisplayName",
                flags={"read_only": True},
            )
            properties.invoice_section_id = AAZStrType(
                serialized_name="invoiceSectionId",
                flags={"read_only": True},
            )
            properties.modified_by_principal_id = AAZStrType(
                serialized_name="modifiedByPrincipalId",
                flags={"read_only": True},
            )
            properties.modified_by_principal_puid = AAZStrType(
                serialized_name="modifiedByPrincipalPuid",
                flags={"read_only": True},
            )
            properties.modified_by_principal_tenant_id = AAZStrType(
                serialized_name="modifiedByPrincipalTenantId",
                flags={"read_only": True},
            )
            properties.modified_by_user_email_address = AAZStrType(
                serialized_name="modifiedByUserEmailAddress",
                flags={"read_only": True},
            )
            properties.modified_on = AAZStrType(
                serialized_name="modifiedOn",
                flags={"read_only": True},
            )
            properties.principal_display_name = AAZStrType(
                serialized_name="principalDisplayName",
                flags={"read_only": True},
            )
            properties.principal_id = AAZStrType(
                serialized_name="principalId",
            )
            properties.principal_puid = AAZStrType(
                serialized_name="principalPuid",
            )
            properties.principal_tenant_id = AAZStrType(
                serialized_name="principalTenantId",
            )
            properties.principal_tenant_name = AAZStrType(
                serialized_name="principalTenantName",
                flags={"read_only": True},
            )
            properties.principal_type = AAZStrType(
                serialized_name="principalType",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.role_definition_id = AAZStrType(
                serialized_name="roleDefinitionId",
                flags={"required": True},
            )
            properties.scope = AAZStrType()
            properties.user_authentication_type = AAZStrType(
                serialized_name="userAuthenticationType",
            )
            properties.user_email_address = AAZStrType(
                serialized_name="userEmailAddress",
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


class _ListByCustomerHelper:
    """Helper class for ListByCustomer"""


__all__ = ["ListByCustomer"]
