import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:plakyab/data/models/auth_model.dart';
import 'package:plakyab/data/repositories/auth_repository.dart';
import 'package:plakyab/core/storage/secure_storage.dart';

final authStateProvider =
    StateNotifierProvider<AuthNotifier, AsyncValue<AuthModel?>>(
  (ref) => AuthNotifier(ref.watch(authRepositoryProvider)),
);

class AuthNotifier extends StateNotifier<AsyncValue<AuthModel?>> {
  final AuthRepository _repository;

  AuthNotifier(this._repository) : super(const AsyncValue.data(null));

  Future<void> login(String email, String password) async {
    state = const AsyncValue.loading();
    try {
      final auth = await _repository.login(email, password);
      await SecureStorage.saveToken(auth.accessToken);
      await SecureStorage.saveRefreshToken(auth.refreshToken);
      state = AsyncValue.data(auth);
    } catch (e, st) {
      state = AsyncValue.error(e, st);
    }
  }

  Future<void> register(
    String email,
    String password,
    String fullName,
    String? phone,
  ) async {
    state = const AsyncValue.loading();
    try {
      await _repository.register(email, password, fullName, phone);
      state = const AsyncValue.data(null);
    } catch (e, st) {
      state = AsyncValue.error(e, st);
    }
  }

  Future<void> logout() async {
    await SecureStorage.deleteToken();
    await SecureStorage.deleteRefreshToken();
    state = const AsyncValue.data(null);
  }
}
