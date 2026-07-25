import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:plakyab/data/models/vehicle_model.dart';
import 'package:plakyab/data/repositories/vehicle_repository.dart';

final vehicleSearchProvider = FutureProvider.family<
    Map<String, dynamic>,
    {
      String? manufacturer,
      String? model,
      int? modelYear,
    }>((ref, params) async {
  final repository = ref.watch(vehicleRepositoryProvider);
  return await repository.searchVehicles(
    manufacturer: params['manufacturer'],
    model: params['model'],
    modelYear: params['modelYear'],
  );
});

final vehicleDetailProvider =
    FutureProvider.family<VehicleModel, String>((ref, vin) async {
  final repository = ref.watch(vehicleRepositoryProvider);
  return await repository.getVehicleByVin(vin);
});

final vinDecoderProvider =
    FutureProvider.family<Map<String, dynamic>, String>((ref, vin) async {
  final repository = ref.watch(vehicleRepositoryProvider);
  return await repository.decodeVin(vin);
});

final vinValidationProvider =
    FutureProvider.family<Map<String, dynamic>, String>((ref, vin) async {
  final repository = ref.watch(vehicleRepositoryProvider);
  return await repository.validateVin(vin);
});
