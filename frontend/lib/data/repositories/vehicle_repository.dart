import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:plakyab/core/network/api_client.dart';
import 'package:plakyab/data/models/vehicle_model.dart';

final vehicleRepositoryProvider = Provider((ref) => VehicleRepository());

class VehicleRepository {
  final _apiClient = APIClient();

  Future<VehicleModel> getVehicleByVin(String vin) async {
    final response = await _apiClient.get(
      endpoint: '/vehicles/by-vin/$vin',
    );
    return VehicleModel.fromJson(response);
  }

  Future<VehicleModel> getVehicleById(int id) async {
    final response = await _apiClient.get(
      endpoint: '/vehicles/$id',
    );
    return VehicleModel.fromJson(response);
  }

  Future<Map<String, dynamic>> searchVehicles({
    String? manufacturer,
    String? model,
    int? modelYear,
    int limit = 20,
    int offset = 0,
  }) async {
    final response = await _apiClient.post(
      endpoint: '/vehicles/search',
      data: {
        'manufacturer': manufacturer,
        'model': model,
        'model_year': modelYear,
        'limit': limit,
        'offset': offset,
      },
    );
    return response;
  }

  Future<Map<String, dynamic>> decodeVin(String vin) async {
    final response = await _apiClient.post(
      endpoint: '/vin/decode',
      queryParameters: {'vin': vin},
    );
    return response;
  }

  Future<Map<String, dynamic>> validateVin(String vin) async {
    final response = await _apiClient.get(
      endpoint: '/vin/validate/$vin',
    );
    return response;
  }
}
