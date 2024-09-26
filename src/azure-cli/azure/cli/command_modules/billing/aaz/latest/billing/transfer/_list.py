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
    "billing transfer list",
)
class List(AAZCommand):
    """List the transfer requests for an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.
    """

    _aaz_info = {
        "version": "2019-10-01-preview",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/transfers", "2019-10-01-preview"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    def _execute_operations(self):
        self.pre_operations()
        self.RecipientTransfersList(ctx=self.ctx)()
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

    class RecipientTransfersList(AAZHttpOperation):
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
                "/providers/Microsoft.Billing/transfers",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2019-10-01-preview",
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
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.allowed_product_type = AAZListType(
                serialized_name="allowedProductType",
                flags={"read_only": True},
            )
            properties.canceled_by = AAZStrType(
                serialized_name="canceledBy",
                flags={"read_only": True},
            )
            properties.creation_time = AAZStrType(
                serialized_name="creationTime",
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
            properties.last_modified_time = AAZStrType(
                serialized_name="lastModifiedTime",
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
            )

            allowed_product_type = cls._schema_on_200.value.Element.properties.allowed_product_type
            allowed_product_type.Element = AAZStrType()

            detailed_transfer_status = cls._schema_on_200.value.Element.properties.detailed_transfer_status
            detailed_transfer_status.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.detailed_transfer_status.Element
            _element.error_details = AAZObjectType(
                serialized_name="errorDetails",
            )
            _element.product_id = AAZStrType(
                serialized_name="productId",
                flags={"read_only": True},
            )
            _element.product_type = AAZStrType(
                serialized_name="productType",
            )
            _element.transfer_status = AAZStrType(
                serialized_name="transferStatus",
            )

            error_details = cls._schema_on_200.value.Element.properties.detailed_transfer_status.Element.error_details
            error_details.error_code = AAZStrType(
                serialized_name="errorCode",
                flags={"read_only": True},
            )
            error_details.error_message = AAZStrType(
                serialized_name="errorMessage",
                flags={"read_only": True},
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
