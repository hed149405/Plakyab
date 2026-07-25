import 'package:dio/dio.dart';
import 'package:plakyab/config/app_config.dart';
import 'package:plakyab/core/network/network_exception.dart';

class APIClient {
  late final Dio _dio;

  APIClient() {
    _dio = Dio(
      BaseOptions(
        baseUrl: AppConfig.apiBaseUrl,
        connectTimeout: AppConfig.apiTimeout,
        receiveTimeout: AppConfig.apiTimeout,
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
      ),
    );

    // Add interceptors
    _dio.interceptors.add(_createInterceptor());
  }

  Interceptor _createInterceptor() {
    return InterceptorsWrapper(
      onRequest: (options, handler) {
        // Add authorization token if available
        // TODO: Get token from secure storage
        return handler.next(options);
      },
      onResponse: (response, handler) {
        return handler.next(response);
      },
      onError: (error, handler) {
        return handler.next(error);
      },
    );
  }

  Future<T> get<T>({
    required String endpoint,
    Map<String, dynamic>? queryParameters,
  }) async {
    try {
      final response = await _dio.get(
        endpoint,
        queryParameters: queryParameters,
      );
      return response.data;
    } on DioException catch (e) {
      throw _handleError(e);
    }
  }

  Future<T> post<T>({
    required String endpoint,
    Map<String, dynamic>? data,
    Map<String, dynamic>? queryParameters,
  }) async {
    try {
      final response = await _dio.post(
        endpoint,
        data: data,
        queryParameters: queryParameters,
      );
      return response.data;
    } on DioException catch (e) {
      throw _handleError(e);
    }
  }

  Future<T> put<T>({
    required String endpoint,
    Map<String, dynamic>? data,
  }) async {
    try {
      final response = await _dio.put(
        endpoint,
        data: data,
      );
      return response.data;
    } on DioException catch (e) {
      throw _handleError(e);
    }
  }

  Future<void> delete({
    required String endpoint,
  }) async {
    try {
      await _dio.delete(endpoint);
    } on DioException catch (e) {
      throw _handleError(e);
    }
  }

  NetworkException _handleError(DioException error) {
    switch (error.type) {
      case DioExceptionType.connectionTimeout:
      case DioExceptionType.receiveTimeout:
      case DioExceptionType.sendTimeout:
        return TimeoutException();
      case DioExceptionType.badResponse:
        return ServerException(
          message: error.response?.data['message'] ?? 'Server error',
          statusCode: error.response?.statusCode,
        );
      case DioExceptionType.connectionError:
        return ConnectionException();
      default:
        return NetworkException(
          message: error.message ?? 'Unknown error',
          originalError: error,
        );
    }
  }
}
