class AppConfig {
  // API Configuration
  static const String apiBaseUrl = 'http://localhost:8000/api/v1';
  static const Duration apiTimeout = Duration(seconds: 30);

  // App Information
  static const String appName = 'Plakyab';
  static const String appVersion = '1.0.0';
  static const String appBuild = '1';

  // Feature Flags
  static const bool enableOfflineMode = true;
  static const bool enablePushNotifications = true;
  static const bool enableAnalytics = true;
  static const bool enableDarkMode = true;
  static const bool enableMultiLanguage = true;

  // Cache Configuration
  static const Duration cacheDuration = Duration(hours: 24);
  static const Duration shortCacheDuration = Duration(hours: 1);

  // VIN Decoder
  static const bool vinValidationEnabled = true;
  static const bool vinCheckDigitValidation = true;
}
