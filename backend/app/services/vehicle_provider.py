"""Vehicle Provider Service - Interface for Authorized Vehicle APIs"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import logging

from app.config import settings
from app.utils.enums import SearchType

logger = logging.getLogger(__name__)


class VehicleInfo:
    """Vehicle Information Data Class"""
    
    def __init__(self, data: Dict[str, Any]):
        self.vin = data.get("vin")
        self.manufacturer = data.get("manufacturer")
        self.model = data.get("model")
        self.model_year = data.get("model_year")
        self.body_type = data.get("body_type")
        self.engine_type = data.get("engine_type")
        self.fuel_type = data.get("fuel_type")
        self.transmission = data.get("transmission")
        self.metadata = data.get("metadata", {})


class IVehicleProvider(ABC):
    """Abstract Base Class for Vehicle Information Providers
    
    IMPORTANT: This interface defines the contract for authorized vehicle
    information APIs only. No implementation should attempt to:
    - Bypass authentication
    - Scrape protected databases
    - Access confidential government records
    - Track vehicle locations
    - Retrieve ownership or transfer history without authorization
    
    All implementations must use official, authorized APIs with proper
    authentication and authorization.
    """

    @abstractmethod
    async def get_vehicle_info(
        self,
        identifier: str,
        search_type: SearchType = SearchType.VIN,
    ) -> Optional[VehicleInfo]:
        """Get vehicle information from authorized API
        
        Args:
            identifier: Search identifier (VIN, plate, etc.)
            search_type: Type of search
            
        Returns:
            VehicleInfo if found, None otherwise
        """
        pass

    @abstractmethod
    async def validate_identifier(
        self,
        identifier: str,
        search_type: SearchType,
    ) -> bool:
        """Validate identifier format before API call
        
        Args:
            identifier: Identifier to validate
            search_type: Type of identifier
            
        Returns:
            True if valid format
        """
        pass


class OfficialVehicleProvider(IVehicleProvider):
    """Placeholder Implementation for Official Vehicle Provider
    
    This is a placeholder implementation designed to connect to
    official, authorized vehicle information APIs in the future.
    
    To implement:
    1. Get API credentials from official provider
    2. Implement authentication
    3. Map vehicle data to VehicleInfo
    4. Handle rate limiting
    5. Add error handling
    """

    def __init__(self, api_key: str, api_url: str):
        """Initialize with authorized API credentials"""
        if not api_key or not api_url:
            logger.warning(
                "Vehicle Provider API credentials not configured. "
                "Using placeholder implementation."
            )
        self.api_key = api_key
        self.api_url = api_url
        self.timeout = settings.VEHICLE_API_TIMEOUT
        self.retries = settings.VEHICLE_API_RETRIES

    async def get_vehicle_info(
        self,
        identifier: str,
        search_type: SearchType = SearchType.VIN,
    ) -> Optional[VehicleInfo]:
        """Get vehicle information
        
        PLACEHOLDER: This method should:
        1. Validate credentials
        2. Check cache
        3. Call authorized API
        4. Map response to VehicleInfo
        5. Cache result
        """
        logger.info(f"Getting vehicle info for {search_type.value}: {identifier}")
        
        if not await self.validate_identifier(identifier, search_type):
            logger.warning(f"Invalid identifier: {identifier}")
            return None

        # TODO: Implement authorized API call
        # This is where you would:
        # 1. Call the official vehicle information API
        # 2. Handle authentication
        # 3. Parse response
        # 4. Return VehicleInfo object
        
        logger.warning(
            f"OfficialVehicleProvider.get_vehicle_info() not yet implemented. "
            f"Please configure with authorized API credentials."
        )
        return None

    async def validate_identifier(
        self,
        identifier: str,
        search_type: SearchType,
    ) -> bool:
        """Validate identifier format"""
        if not identifier:
            return False

        if search_type == SearchType.VIN:
            from app.utils.validators import VINValidator
            return VINValidator.validate_format(identifier)
        
        elif search_type == SearchType.PLATE_NUMBER:
            from app.utils.validators import PlateValidator
            return PlateValidator.validate(identifier)
        
        return len(identifier) > 3


class MockVehicleProvider(IVehicleProvider):
    """Mock Vehicle Provider for Development/Testing
    
    Use for testing and development. Returns mock data.
    NOT for production use.
    """

    MOCK_VEHICLES = {
        "WBADT43452G296706": {
            "vin": "WBADT43452G296706",
            "manufacturer": "BMW",
            "model": "3 Series",
            "model_year": 2012,
            "body_type": "Sedan",
            "engine_type": "Inline-4",
            "fuel_type": "Petrol",
            "transmission": "Automatic",
        },
    }

    async def get_vehicle_info(
        self,
        identifier: str,
        search_type: SearchType = SearchType.VIN,
    ) -> Optional[VehicleInfo]:
        """Get mock vehicle information"""
        logger.debug(f"[MOCK] Getting vehicle info for {search_type.value}: {identifier}")
        
        if search_type == SearchType.VIN:
            data = self.MOCK_VEHICLES.get(identifier.upper())
            if data:
                return VehicleInfo(data)
        
        return None

    async def validate_identifier(
        self,
        identifier: str,
        search_type: SearchType,
    ) -> bool:
        """Validate identifier format"""
        return len(identifier) > 3


def get_vehicle_provider() -> IVehicleProvider:
    """Factory function to get vehicle provider instance"""
    if settings.FASTAPI_ENV == "development":
        logger.info("Using MockVehicleProvider for development")
        return MockVehicleProvider()
    else:
        logger.info(f"Using OfficialVehicleProvider: {settings.VEHICLE_API_PROVIDER}")
        return OfficialVehicleProvider(
            api_key=settings.VEHICLE_API_KEY,
            api_url=settings.VEHICLE_API_URL,
        )
