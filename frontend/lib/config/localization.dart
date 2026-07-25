import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

final themeModeProvider = StateProvider<ThemeMode>((ref) => ThemeMode.system);

final localeProvider = StateProvider<Locale>((ref) => const Locale('en'));

class AppLocalizations {
  static const LocalizationsDelegate<AppLocalizations> delegate =
      _AppLocalizationsDelegate();

  static const List<Locale> supportedLocales = [
    Locale('en'),
    Locale('ar'),
    Locale('fr'),
    Locale('es'),
  ];

  static const List<LocalizationsDelegate> localizationsDelegates = [
    AppLocalizations.delegate,
    GlobalMaterialLocalizations.delegate,
    GlobalWidgetsLocalizations.delegate,
    GlobalCupertinoLocalizations.delegate,
  ];

  // English Strings
  static const Map<String, String> _enStrings = {
    'app_name': 'Plakyab',
    'app_subtitle': 'Vehicle Information & Diagnostics',
    // Auth
    'login': 'Login',
    'register': 'Register',
    'logout': 'Logout',
    'email': 'Email',
    'password': 'Password',
    'confirm_password': 'Confirm Password',
    'full_name': 'Full Name',
    'phone': 'Phone Number',
    'forgot_password': 'Forgot Password?',
    'dont_have_account': "Don't have an account?",
    'already_have_account': 'Already have an account?',
    // Vehicles
    'vehicles': 'Vehicles',
    'search_vehicles': 'Search Vehicles',
    'vehicle_details': 'Vehicle Details',
    'add_vehicle': 'Add Vehicle',
    'vin': 'VIN',
    'plate_number': 'Plate Number',
    'manufacturer': 'Manufacturer',
    'model': 'Model',
    'year': 'Year',
    'color': 'Color',
    'search': 'Search',
    'decode_vin': 'Decode VIN',
    // Common
    'home': 'Home',
    'profile': 'Profile',
    'settings': 'Settings',
    'about': 'About',
    'save': 'Save',
    'cancel': 'Cancel',
    'delete': 'Delete',
    'edit': 'Edit',
    'loading': 'Loading...',
    'error': 'Error',
    'success': 'Success',
    'no_data': 'No data found',
  };

  // Arabic Strings
  static const Map<String, String> _arStrings = {
    'app_name': 'بلاكيب',
    'app_subtitle': 'معلومات المركبات والتشخيص',
    'login': 'دخول',
    'register': 'تسجيل',
    'email': 'البريد الإلكتروني',
    'password': 'كلمة المرور',
    'search': 'بحث',
  };

  // French Strings
  static const Map<String, String> _frStrings = {
    'app_name': 'Plakyab',
    'app_subtitle': 'Informations Véhicules et Diagnostics',
    'login': 'Connexion',
    'register': 'Inscription',
    'email': 'E-mail',
    'password': 'Mot de passe',
    'search': 'Rechercher',
  };

  // Spanish Strings
  static const Map<String, String> _esStrings = {
    'app_name': 'Plakyab',
    'app_subtitle': 'Información y Diagnóstico de Vehículos',
    'login': 'Iniciar sesión',
    'register': 'Registrarse',
    'email': 'Correo electrónico',
    'password': 'Contraseña',
    'search': 'Buscar',
  };

  static String tr(String key) {
    return _enStrings[key] ?? key;
  }
}

class _AppLocalizationsDelegate
    extends LocalizationsDelegate<AppLocalizations> {
  const _AppLocalizationsDelegate();

  @override
  bool isSupported(Locale locale) {
    return AppLocalizations.supportedLocales.contains(locale);
  }

  @override
  Future<AppLocalizations> load(Locale locale) async {
    return AppLocalizations();
  }

  @override
  bool shouldReload(_AppLocalizationsDelegate old) => false;
}

extension StringLocalization on String {
  String tr() => AppLocalizations.tr(this);
}
