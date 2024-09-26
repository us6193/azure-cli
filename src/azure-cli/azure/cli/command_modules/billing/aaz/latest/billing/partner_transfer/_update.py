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
    "billing partner-transfer update",
)
class Update(AAZCommand):
    """Update a request to a user in a customer's billing account to transfer billing ownership of their subscriptions. The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/{}/billingprofiles/{}/customers/{}/transfers/{}", "2024-04-01"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.customer_name = AAZStrArg(
            options=["--customer-name"],
            help="The ID that uniquely identifies a customer.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-_]{1,128}$",
            ),
        )
        _args_schema.transfer_name = AAZStrArg(
            options=["--transfer-name"],
            help="The ID that uniquely identifies a transfer request.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-z0-9]*$",
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.recipient_email_id = AAZStrArg(
            options=["--recipient-email-id"],
            arg_group="Properties",
            help="The email ID of the recipient to whom the transfer request is sent.",
            nullable=True,
        )
        _args_schema.reseller_id = AAZStrArg(
            options=["--reseller-id"],
            arg_group="Properties",
            help="Optional MPN ID of the reseller for transfer requests that are sent from a Microsoft Partner Agreement billing account.",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PartnerTransfersGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.PartnerTransfersInitiate(ctx=self.ctx)()
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

    class PartnerTransfersGet(AAZHttpOperation):
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
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/customers/{customerName}/transfers/{transferName}",
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
                **self.serialize_url_param(
                    "transferName", self.ctx.args.transfer_name,
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
            _UpdateHelper._build_schema_partner_transfer_details_read(cls._schema_on_200)

            return cls._schema_on_200

    class PartnerTransfersInitiate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/customers/{customerName}/transfers/{transferName}",
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
                    "billingProfileName", self.ctx.args.billing_profile_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "customerName", self.ctx.args.customer_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "transferName", self.ctx.args.transfer_name,
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
            _UpdateHelper._build_schema_partner_transfer_details_read(cls._schema_on_200_201)

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

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("recipientEmailId", AAZStrType, ".recipient_email_id")
                properties.set_prop("resellerId", AAZStrType, ".reseller_id")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_partner_transfer_details_read = None

    @classmethod
    def _build_schema_partner_transfer_details_read(cls, _schema):
        if cls._schema_partner_transfer_details_read is not None:
            _schema.id = cls._schema_partner_transfer_details_read.id
            _schema.name = cls._schema_partner_transfer_details_read.name
            _schema.properties = cls._schema_partner_transfer_details_read.properties
            _schema.system_data = cls._schema_partner_transfer_details_read.system_data
            _schema.tags = cls._schema_partner_transfer_details_read.tags
            _schema.type = cls._schema_partner_transfer_details_read.type
            return

        cls._schema_partner_transfer_details_read = _schema_partner_transfer_details_read = AAZObjectType()

        partner_transfer_details_read = _schema_partner_transfer_details_read
        partner_transfer_details_read.id = AAZStrType(
            flags={"read_only": True},
        )
        partner_transfer_details_read.name = AAZStrType(
            flags={"read_only": True},
        )
        partner_transfer_details_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        partner_transfer_details_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        partner_transfer_details_read.tags = AAZDictType()
        partner_transfer_details_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_partner_transfer_details_read.properties
        properties.canceled_by = AAZStrType(
            serialized_name="canceledBy",
            flags={"read_only": True},
        )
        properties.detailed_transfer_status = AAZListType(
            serialized_name="detailedTransferStatus",
            flags={"read_only": True},
        )
        properties.expiration_time = AAZStrType(
            serialized_name="expirationTime",
            flags={"read_only": True},
        )
        properties.initiator_customer_type = AAZStrType(
            serialized_name="initiatorCustomerType",
            flags={"read_only": True},
        )
        properties.initiator_email_id = AAZStrType(
            serialized_name="initiatorEmailId",
            flags={"read_only": True},
        )
        properties.recipient_email_id = AAZStrType(
            serialized_name="recipientEmailId",
            flags={"read_only": True},
        )
        properties.reseller_id = AAZStrType(
            serialized_name="resellerId",
            flags={"read_only": True},
        )
        properties.reseller_name = AAZStrType(
            serialized_name="resellerName",
            flags={"read_only": True},
        )
        properties.transfer_status = AAZStrType(
            serialized_name="transferStatus",
            flags={"read_only": True},
        )

        detailed_transfer_status = _schema_partner_transfer_details_read.properties.detailed_transfer_status
        detailed_transfer_status.Element = AAZObjectType()

        _element = _schema_partner_transfer_details_read.properties.detailed_transfer_status.Element
        _element.error_details = AAZObjectType(
            serialized_name="errorDetails",
        )
        _element.product_id = AAZStrType(
            serialized_name="productId",
            flags={"read_only": True},
        )
        _element.product_name = AAZStrType(
            serialized_name="productName",
            flags={"read_only": True},
        )
        _element.product_type = AAZStrType(
            serialized_name="productType",
            flags={"read_only": True},
        )
        _element.sku_description = AAZStrType(
            serialized_name="skuDescription",
            flags={"read_only": True},
        )
        _element.transfer_status = AAZStrType(
            serialized_name="transferStatus",
            flags={"read_only": True},
        )

        error_details = _schema_partner_transfer_details_read.properties.detailed_transfer_status.Element.error_details
        error_details.code = AAZStrType(
            flags={"read_only": True},
        )
        error_details.message = AAZStrType(
            flags={"read_only": True},
        )

        system_data = _schema_partner_transfer_details_read.system_data
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

        tags = _schema_partner_transfer_details_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_partner_transfer_details_read.id
        _schema.name = cls._schema_partner_transfer_details_read.name
        _schema.properties = cls._schema_partner_transfer_details_read.properties
        _schema.system_data = cls._schema_partner_transfer_details_read.system_data
        _schema.tags = cls._schema_partner_transfer_details_read.tags
        _schema.type = cls._schema_partner_transfer_details_read.type


__all__ = ["Update"]
