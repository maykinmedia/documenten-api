"""
Serializers of the Document Registratie Component REST API
"""

from rest_framework import serializers

from drc.datamodel.models import EnkelvoudigInformatieObject


class EnkelvoudigInformatieObjectSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the EnkelvoudigInformatieObject model
    """

    class Meta:
        model = EnkelvoudigInformatieObject
        fields = (
            'informatieobjectidentificatie',
            'bronorganisatie',
            'creatiedatum',
            'titel',
            'auteur',
            'formaat',
            'taal',
            'inhoud'
        )
