import uuid

from mongoengine import Document, EmbeddedDocument, StringField, IntField, ListField
from mongoengine import UUIDField
from mongoengine import IntField, BooleanField
from django.conf import settings

from crits.core.crits_mongoengine import CritsBaseAttributes, CritsDocumentFormatter
from crits.core.crits_mongoengine import CritsSourceDocument, CritsDocument, CritsSchemaDocument
from crits.core.crits_mongoengine import CommonAccess, CritsActionsDocument


class SignatureDependency(CritsDocument, CritsSchemaDocument, Document):
    """
    Signature dependency class.
    """

    meta = {
        "collection": settings.COL_SIGNATURE_DEPENDENCY,
        "crits_type": 'SignatureDependency',
        "latest_schema_version": 1,
        "schema_doc": {
            'name': 'The name of this data dependency',
            'active': 'Enabled in the UI (on/off)'
        },
    }

    name = StringField()
    active = StringField(default="on")


class SignatureType(CritsDocument, CritsSchemaDocument, Document):
    """
    Signature type class.
    """

    meta = {
        "collection": settings.COL_SIGNATURE_TYPES,
        "crits_type": 'SignatureType',
        "latest_schema_version": 1,
        "schema_doc": {
            'name': 'The name of this data type',
            'active': 'Enabled in the UI (on/off)'
        },
    }

    name = StringField()
    active = StringField(default="on")


class Signature(CritsBaseAttributes, CritsSourceDocument, CritsActionsDocument,
                Document):
    """
    Signature class.
    """

    meta = {
        "collection": settings.COL_SIGNATURES,
        "crits_type": 'Signature',
        "latest_schema_version": 1,
        "schema_doc": {
        },
        "jtable_opts": {
                         'details_url': 'crits.signatures.views.signature_detail',
                         'details_url_key': 'id',
                         'default_sort': "modified DESC",
                         'searchurl': 'crits.signatures.views.signatures_listing',
                         'fields': [ "title", "data_type", "data_type_min_version",
                                     "data_type_max_version",
                                     "data_type_dependency", "version",
                                     "modified", "source", "campaign",
                                     "id", "status"],
                         'jtopts_fields': [ "details",
                                            "title",
                                            "data_type",
                                            "data_type_min_version",
                                            "data_type_max_version",
                                            "data_type_dependency",
                                            "version",
                                            "modified",
                                            "source",
                                            "campaign",
                                            "status",
                                            "favorite",
                                            "id"],
                         'hidden_fields': [],
                         'linked_fields': ["source", "campaign"],
                         'details_link': 'details',
                         'no_sort': ['details']
                       }
    }

    data_type = StringField()
    data_type_min_version = StringField()
    data_type_max_version = StringField()
    data_type_dependency = ListField()
    data = StringField()
    link_id = UUIDField(binary=True, required=True, default=uuid.uuid4)
    md5 = StringField()
    title = StringField()
    version = IntField()

class SignatureAccess(EmbeddedDocument, CritsDocumentFormatter, CommonAccess):
    """
    ACL for Samples.
    """

    upload_related_sample = BooleanField(default=False)
    upload_related_pcap = BooleanField(default=False)

    text_view = BooleanField(default=False)
    yaml_view = BooleanField(default=False)
    unrar_sample = BooleanField(default=False)
    unzip_sample = BooleanField(default=False)

    filename_edit = BooleanField(default=False)
    filenames_add = BooleanField(default=False)
    filenames_remove = BooleanField(default=False)
