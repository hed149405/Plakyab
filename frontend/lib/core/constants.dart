// Core module exports

abstract class Constants {
  // API
  static const String apiVersion = 'v1';
  static const Duration apiTimeout = Duration(seconds: 30);

  // Validation
  static const int vinLength = 17;
  static const int minPasswordLength = 8;
  static const int maxPasswordLength = 128;

  // UI
  static const double defaultPadding = 16.0;
  static const double defaultBorderRadius = 8.0;
}
