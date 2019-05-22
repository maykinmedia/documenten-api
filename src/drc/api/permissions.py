from vng_api_common.permissions import (
    MainObjAuthScopesRequired, RelatedObjAuthScopesRequired
)


class InformationObjectAuthScopesRequired(MainObjAuthScopesRequired):
    """
    Look at the scopes required for the current action and at informatieobjecttype and vertrouwelijkheidaanduiding
    of current informatieobject and check that they are present in the AC for this client
    """
    permission_fields = ('informatieobjecttype', 'vertrouwelijkheidaanduiding')


class InformationObjectRelatedAuthScopesRequired(RelatedObjAuthScopesRequired):
    """
    Look at the scopes required for the current action and at informatieobjecttype and vertrouwelijkheidaanduiding
    of related informatieobject and check that they are present in the AC for this client
    """
    permission_fields = ('informatieobjecttype', 'vertrouwelijkheidaanduiding')
    obj_path = 'informatieobject'
