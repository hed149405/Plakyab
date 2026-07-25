// User Models

class UserModel {
  final int id;
  final String email;
  final String fullName;
  final String? phone;
  final bool isActive;
  final bool isVerified;
  final DateTime createdAt;
  final DateTime updatedAt;
  final List<String> roles;

  UserModel({
    required this.id,
    required this.email,
    required this.fullName,
    this.phone,
    required this.isActive,
    required this.isVerified,
    required this.createdAt,
    required this.updatedAt,
    this.roles = const [],
  });

  factory UserModel.fromJson(Map<String, dynamic> json) {
    return UserModel(
      id: json['id'],
      email: json['email'],
      fullName: json['full_name'],
      phone: json['phone'],
      isActive: json['is_active'],
      isVerified: json['is_verified'],
      createdAt: DateTime.parse(json['created_at']),
      updatedAt: DateTime.parse(json['updated_at']),
      roles: List<String>.from(json['roles'] ?? []),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'email': email,
      'full_name': fullName,
      'phone': phone,
      'is_active': isActive,
      'is_verified': isVerified,
      'created_at': createdAt.toIso8601String(),
      'updated_at': updatedAt.toIso8601String(),
      'roles': roles,
    };
  }
}
