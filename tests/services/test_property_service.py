import unittest
from unittest.mock import patch

from src.services.property_service import PropertyService


class TestPropertyService(unittest.TestCase):
    def setUp(self) -> None:
        self.property_service = PropertyService()
        self.properties = [
            {
                "id": 1,
                "address": "carrera 100 #15-90",
                "city": "bogota",
                "status": "en_venta",
                "price": 350000000,
                "description": "Amplio apartamento en conjunto cerrado",
                "year": 2011,
            },
            {
                "id": 2,
                "address": "calle 23 #45-67",
                "city": "medellin",
                "status": "pre_venta",
                "price": 210000000,
                "description": "",
                "year": 2020,
            },
            {
                "id": 3,
                "address": "diagonal 23 #28-21",
                "city": "bogota",
                "status": "vendido",
                "price": 270000000,
                "description": "Apartamento con hermosas vistas",
                "year": 2020,
            },
            {
                "id": 4,
                "address": "carrera 100 #15-90",
                "city": "barranquilla",
                "status": "pre_venta",
                "price": 35000000,
                "description": None,
                "year": 2020,
            },
            {
                "id": 5,
                "address": "Cll 1A #11B-20",
                "city": "pereira",
                "status": "vendido",
                "price": 300000000,
                "description": "hermoso acabado, listo para estrenar super comodo",
                "year": 2019,
            },
        ]
        self.pre_sale_properties = list(
            filter(lambda p: p["status"] == "pre_venta", self.properties)
        )
        self.properties_built_in_2020 = list(
            filter(lambda p: p["year"] == 2020, self.properties)
        )
        self.properties_in_medellin = list(
            filter(lambda p: p["city"] == "medellin", self.properties)
        )

    def test_get_properties(self) -> None:
        with patch.object(
            self.property_service, "get_properties", return_value=self.properties
        ) as mocked_properties:
            result = self.property_service.get_properties(
                status=None, year=None, city=None
            )
            self.assertEqual(result, self.properties)
        mocked_properties.assert_called_with(status=None, year=None, city=None)

    def test_get_properties_by_status(self) -> None:
        with patch.object(
            self.property_service,
            "get_properties",
            return_value=self.pre_sale_properties,
        ) as mocked_properties_by_status:
            result = self.property_service.get_properties(
                status="PRE_SALE", year=None, city=None
            )
            self.assertEqual(result, self.pre_sale_properties)
        mocked_properties_by_status.assert_called_with(
            status="PRE_SALE", year=None, city=None
        )

    def test_get_properties_by_year(self) -> None:
        with patch.object(
            self.property_service,
            "get_properties",
            return_value=self.properties_built_in_2020,
        ) as mocked_properties_by_year:
            result = self.property_service.get_properties(
                status=None, year=2020, city=None
            )
            self.assertEqual(result, self.properties_built_in_2020)
        mocked_properties_by_year.assert_called_with(status=None, year=2020, city=None)

    def test_get_properties_by_city(self) -> None:
        with patch.object(
            self.property_service,
            "get_properties",
            return_value=self.properties_in_medellin,
        ) as mocked_properties_by_city:
            result = self.property_service.get_properties(
                status=None, year=None, city="medellin"
            )
            self.assertEqual(result, self.properties_in_medellin)
        mocked_properties_by_city.assert_called_with(
            status=None, year=None, city="medellin"
        )

    def test_invalid_status(self) -> None:
        try:
            self.property_service.validate_property_params(
                status="PRE_SOLD", year=None, city=None
            )
        except Exception as e:
            self.assertRegex(str(e), "Invalid status")

    def test_invalid_year(self) -> None:
        try:
            self.property_service.validate_property_params(
                status=None, year="house", city=None
            )
        except Exception as e:
            self.assertRegex(str(e), "Invalid year")

    def test_invalid_city(self) -> None:
        try:
            self.property_service.validate_property_params(
                status=None, year=None, city=2022
            )
        except Exception as e:
            self.assertRegex(str(e), "Invalid city")
