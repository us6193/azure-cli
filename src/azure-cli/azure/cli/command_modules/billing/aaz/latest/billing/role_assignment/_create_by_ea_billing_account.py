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
    "billing role-assignment create-by-ea-billing-account",
)
class CreateByEaBillingAccount(AAZCommand):
    """Create a billing role assignment. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

    :example: BillingRoleAssignmentCreateOrUpdateByBillingAccount
        az billing role-assignment create-by-ea-billing-account --billing-account-name 7898901 --billing-role-assignment-name 9dfd08c2-62a3-4d47-85bd-1cdba1408402 --principal-id 00000000-0000-0000-0000-000000000000 --principal-tenant-id 076915e7-de10-4323-bb34-a58c904068bb --role-definition-id /providers/Microsoft.Billing/billingAccounts/7898901/billingRoleDefinitions/9f1983cb-2574-400c-87e9-34cf8e2280db --user-email-address john@contoso.com
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/{}/billingroleassignments/{}", "2024-04-01"],
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
            fmt=AAZStrArgFormat(
                pattern="^([0-9]+|([Pp][Cc][Nn]\\.[A-Za-z0-9]+)|[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}(:[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}_[0-9]{4}(-[0-9]{2}){2})?)$",
            ),
        )
        _args_schema.billing_role_assignment_name = AAZStrArg(
            options=["--billing-role-assignment-name"],
            help="The ID that uniquely identifies a role assignment.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-fA-F0-9]{8}[-]?([a-fA-F0-9]{4}[-]?){3}[a-fA-F0-9]{12}(_[a-fA-F0-9]{8}[-]?([a-fA-F0-9]{4}[-]?){3}[a-fA-F0-9]{12})?$",
            ),
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \\ ? /",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.principal_id = AAZStrArg(
            options=["--principal-id"],
            arg_group="Properties",
            help="The object id of the user to whom the role was assigned.",
        )
        _args_schema.principal_puid = AAZStrArg(
            options=["--principal-puid"],
            arg_group="Properties",
            help="The principal PUID of the user to whom the role was assigned.",
        )
        _args_schema.principal_tenant_id = AAZStrArg(
            options=["--principal-tenant-id"],
            arg_group="Properties",
            help="The principal tenant id of the user to whom the role was assigned.",
        )
        _args_schema.role_definition_id = AAZStrArg(
            options=["--role-definition-id"],
            arg_group="Properties",
            help="The ID of the role definition.",
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        _args_schema.scope = AAZStrArg(
            options=["--scope"],
            arg_group="Properties",
            help="The scope at which the role was assigned.",
        )
        _args_schema.user_authentication_type = AAZStrArg(
            options=["--user-authentication-type"],
            arg_group="Properties",
            help="The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.",
        )
        _args_schema.user_email_address = AAZStrArg(
            options=["--user-email-address"],
            arg_group="Properties",
            help="The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.BillingRoleAssignmentsCreateOrUpdateByBillingAccount(ctx=self.ctx)()
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

    class BillingRoleAssignmentsCreateOrUpdateByBillingAccount(AAZHttpOperation):
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
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleAssignments/{billingRoleAssignmentName}",
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
                    "billingAccountName", self.ctx.args.billing_account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "billingRoleAssignmentName", self.ctx.args.billing_role_assignment_name,
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
            _builder.set_prop("properties", AAZObjectType)
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("principalId", AAZStrType, ".principal_id")
                properties.set_prop("principalPuid", AAZStrType, ".principal_puid")
                properties.set_prop("principalTenantId", AAZStrType, ".principal_tenant_id")
                properties.set_prop("roleDefinitionId", AAZStrType, ".role_definition_id", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("scope", AAZStrType, ".scope")
                properties.set_prop("userAuthenticationType", AAZStrType, ".user_authentication_type")
                properties.set_prop("userEmailAddress", AAZStrType, ".user_email_address")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

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

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType()
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
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

            system_data = cls._schema_on_200_201.system_data
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

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateByEaBillingAccountHelper:
    """Helper class for CreateByEaBillingAccount"""


__all__ = ["CreateByEaBillingAccount"]
