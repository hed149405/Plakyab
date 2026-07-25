import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:plakyab/core/network/api_client.dart';
import 'package:plakyab/data/models/auth_model.dart';

final authRepositoryProvider = Provider((ref) => AuthRepository());

class AuthRepository {
  final _apiClient = APIClient();

  Future<AuthModel> login(String email, String password) async {
    final response = await _apiClient.post(
      endpoint: '/auth/login',
      data: {
        'email': email,
        'password': password,
      },
    );
    return AuthModel.fromJson(response);
  }

  Future<Map<String, dynamic>> register(
    String email,
    String password,
    String fullName,
    String? phone,
  ) async {
    final response = await _apiClient.post(
      endpoint: '/auth/register',
      data: {
        'email': email,
        'password': password,
        'full_name': fullName,
        'phone': phone,
      },
    );
    return response;
  }

  Future<AuthModel> refreshToken(String refreshToken) async {
    final response = await _apiClient.post(
      endpoint: '/auth/refresh',
      data: {
        'refresh_token': refreshToken,
      },
    );
    return AuthModel.fromJson(response);
  }
}
