"""
Test filtering ZaakInformatieObject on Zaak.

See:
* https://github.com/VNG-Realisatie/gemma-zaken/issues/154 (us)
* https://github.com/VNG-Realisatie/gemma-zaken/issues/239 (mapping)
"""
from unittest.mock import patch

# import factory
from rest_framework import status
from rest_framework.test import APITestCase
from zds_schema.tests import TypeCheckMixin, get_operation_url

from drc.datamodel.tests.factories import ObjectInformatieObjectFactory

# from django.db.models import signals




class US154Tests(TypeCheckMixin, APITestCase):

    def setUp(self):
        super().setUp()

        patcher = patch('drc.sync.signals.sync_create')
        self.mocked_sync_create = patcher.start()
        self.addCleanup(patcher.stop)

    def test_informatieobjecttype_filter(self):
        zaak_url = 'http://www.example.com/zrc/api/v1/zaken/1'

        ObjectInformatieObjectFactory.create_batch(2, is_zaak=True, object=zaak_url)
        ObjectInformatieObjectFactory.create(is_zaak=True, object='http://www.example.com/zrc/api/v1/zaken/2')

        url = get_operation_url('objectinformatieobject_list')

        response = self.client.get(url, {'object': zaak_url})

        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

        response_data = response.json()
        self.assertEqual(len(response_data), 2)

        for zio in response_data:
            self.assertEqual(zio['object'], zaak_url)
