// Data Models

class VehicleModel {
  final int id;
  final String vin;
  final String? plateNumber;
  final String manufacturer;
  final String model;
  final int modelYear;
  final String? color;
  final String? engineType;
  final String? fuelType;
  final String? transmission;
  final String status;
  final DateTime createdAt;
  final DateTime updatedAt;

  VehicleModel({
    required this.id,
    required this.vin,
    this.plateNumber,
    required this.manufacturer,
    required this.model,
    required this.modelYear,
    this.color,
    this.engineType,
    this.fuelType,
    this.transmission,
    required this.status,
    required this.createdAt,
    required this.updatedAt,
  });

  factory VehicleModel.fromJson(Map<String, dynamic> json) {
    return VehicleModel(
      id: json['id'],
      vin: json['vin'],
      plateNumber: json['plate_number'],
      manufacturer: json['manufacturer'],
      model: json['model'],
      modelYear: json['model_year'],
      color: json['color'],
      engineType: json['engine_type'],
      fuelType: json['fuel_type'],
      transmission: json['transmission'],
      status: json['status'],
      createdAt: DateTime.parse(json['created_at']),
      updatedAt: DateTime.parse(json['updated_at']),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'vin': vin,
      'plate_number': plateNumber,
      'manufacturer': manufacturer,
      'model': model,
      'model_year': modelYear,
      'color': color,
      'engine_type': engineType,
      'fuel_type': fuelType,
      'transmission': transmission,
      'status': status,
      'created_at': createdAt.toIso8601String(),
      'updated_at': updatedAt.toIso8601String(),
    };
  }
}
