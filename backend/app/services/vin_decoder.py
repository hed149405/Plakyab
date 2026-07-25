"""VIN Decoder Service - ISO 3779 Compliant"""

import logging
from typing import Optional, Dict, Any

from app.utils.validators import VINValidator
from app.utils.constants import VIN_TRANSLITERATION

logger = logging.getLogger(__name__)


class VINDecoder:
    """VIN Decoder - Extracts information from VIN
    
    Implements ISO/IEC 3779 standard for VIN decoding.
    """

    # WMI - World Manufacturer Identifier
    WMI_MANUFACTURERS = {
        "WBA": {"name": "BMW", "country": "Germany"},
        "WAG": {"name": "Audi", "country": "Germany"},
        "WVW": {"name": "Volkswagen", "country": "Germany"},
        "WDB": {"name": "Mercedes-Benz", "country": "Germany"},
        "ZAR": {"name": "General Motors", "country": "South Africa"},
        "JHM": {"name": "Honda", "country": "Japan"},
        "JT2": {"name": "Toyota", "country": "Japan"},
        "JMZ": {"name": "Mazda", "country": "Japan"},
        # Add more WMIs as needed
    }

    @staticmethod
    def validate(vin: str) -> bool:
        """Validate VIN using ISO 3779"""
        return VINValidator.validate(vin)

    @staticmethod
    def get_wmi(vin: str) -> Dict[str, str]:
        """Get World Manufacturer Identifier info
        
        Args:
            vin: Vehicle Identification Number
            
        Returns:
            Dictionary with manufacturer info
        """
        if not vin or len(vin) < 3:
            return {"manufacturer": "Unknown", "country": "Unknown"}

        wmi = vin[:3].upper()
        return VINDecoder.WMI_MANUFACTURERS.get(
            wmi,
            {"manufacturer": "Unknown", "country": "Unknown"},
        )

    @staticmethod
    def get_vds(vin: str) -> str:
        """Get Vehicle Descriptor Section (positions 4-9)
        
        The VDS is manufacturer-specific and describes vehicle type,
        series, body style, engine, transmission, and safety features.
        """
        if not vin or len(vin) < 9:
            return ""
        return vin[3:9].upper()

    @staticmethod
    def get_vis(vin: str) -> str:
        """Get Vehicle Identifier Section (positions 10-17)
        
        The VIS contains the check digit and sequential number.
        """
        if not vin or len(vin) < 17:
            return ""
        return vin[9:17].upper()

    @staticmethod
    def get_check_digit(vin: str) -> Optional[str]:
        """Get check digit (position 9)"""
        if not vin or len(vin) < 9:
            return None
        return vin[8].upper()

    @staticmethod
    def decode(vin: str) -> Optional[Dict[str, Any]]:
        """Decode VIN to extract information
        
        Args:
            vin: Vehicle Identification Number
            
        Returns:
            Dictionary with decoded information
        """
        if not VINValidator.validate(vin):
            logger.warning(f"Invalid VIN: {vin}")
            return None

        vin = vin.upper()

        wmi_info = VINDecoder.get_wmi(vin)

        return {
            "vin": vin,
            "wmi": vin[:3],
            "vds": VINDecoder.get_vds(vin),
            "vis": VINDecoder.get_vis(vin),
            "check_digit": VINDecoder.get_check_digit(vin),
            "manufacturer": wmi_info.get("manufacturer"),
            "country": wmi_info.get("country"),
            "year_from_check": VINDecoder._get_year_from_check(vin),
        }

    @staticmethod
    def _get_year_from_check(vin: str) -> Optional[int]:
        """Estimate year from check digit position
        
        Note: This is a rough estimate. Actual year decoding requires
        manufacturer-specific information.
        """
        check_pos = vin[9].upper()
        
        # Simplified mapping (this varies by manufacturer)
        year_map = {
            'A': 2010, 'B': 2011, 'C': 2012, 'D': 2013, 'E': 2014,
            'F': 2015, 'G': 2016, 'H': 2017, 'J': 2018, 'K': 2019,
            'L': 2020, 'M': 2021, 'N': 2022, 'P': 2023, 'R': 2024,
            'S': 2025, 'T': 2026, 'V': 2027, 'W': 2028, 'X': 2029,
            'Y': 2030, '1': 2031, '2': 2032,
        }
        
        return year_map.get(check_pos)
