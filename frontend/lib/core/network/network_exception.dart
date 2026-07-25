// Network exceptions

class NetworkException implements Exception {
  final String message;
  final int? statusCode;
  final dynamic originalError;

  NetworkException({
    required this.message,
    this.statusCode,
    this.originalError,
  });

  @override
  String toString() => message;
}

class ConnectionException extends NetworkException {
  ConnectionException()
      : super(
          message: 'No internet connection',
        );
}

class TimeoutException extends NetworkException {
  TimeoutException()
      : super(
          message: 'Request timeout',
        );
}

class ServerException extends NetworkException {
  ServerException({required String message, int? statusCode})
      : super(
          message: message,
          statusCode: statusCode,
        );
}
