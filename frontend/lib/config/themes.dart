import 'package:flutter/material.dart';

const Color _primaryColor = Color(0xFF1F77F2);
const Color _secondaryColor = Color(0xFF00D9A3);
const Color _errorColor = Color(0xFFEF4444);
const Color _warningColor = Color(0xFFFB923C);
const Color _successColor = Color(0xFF22C55E);

final lightTheme = ThemeData(
  useMaterial3: true,
  brightness: Brightness.light,
  colorScheme: const ColorScheme.light(
    primary: _primaryColor,
    secondary: _secondaryColor,
    error: _errorColor,
    surface: Color(0xFFFAFAFA),
    onSurface: Color(0xFF1F2937),
    outline: Color(0xFFE5E7EB),
  ),
  scaffoldBackgroundColor: Colors.white,
  appBarTheme: const AppBarTheme(
    backgroundColor: Colors.white,
    elevation: 0,
    iconTheme: IconThemeData(color: Color(0xFF1F2937)),
    titleTextStyle: TextStyle(
      color: Color(0xFF1F2937),
      fontSize: 18,
      fontWeight: FontWeight.w600,
    ),
  ),
  inputDecorationTheme: InputDecorationTheme(
    filled: true,
    fillColor: Color(0xFFF3F4F6),
    border: OutlineInputBorder(
      borderRadius: BorderRadius.circular(8),
      borderSide: BorderSide.none,
    ),
    focusedBorder: OutlineInputBorder(
      borderRadius: BorderRadius.circular(8),
      borderSide: const BorderSide(color: _primaryColor, width: 2),
    ),
    errorBorder: OutlineInputBorder(
      borderRadius: BorderRadius.circular(8),
      borderSide: const BorderSide(color: _errorColor),
    ),
    contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
  ),
  elevatedButtonTheme: ElevatedButtonThemeData(
    style: ElevatedButton.styleFrom(
      backgroundColor: _primaryColor,
      foregroundColor: Colors.white,
      padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
      elevation: 0,
    ),
  ),
  textButtonTheme: TextButtonThemeData(
    style: TextButton.styleFrom(
      foregroundColor: _primaryColor,
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
    ),
  ),
  cardTheme: CardTheme(
    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
    elevation: 0,
    color: Colors.white,
  ),
);

final darkTheme = ThemeData(
  useMaterial3: true,
  brightness: Brightness.dark,
  colorScheme: const ColorScheme.dark(
    primary: _primaryColor,
    secondary: _secondaryColor,
    error: _errorColor,
    surface: Color(0xFF111827),
    onSurface: Color(0xFFF3F4F6),
    outline: Color(0xFF374151),
  ),
  scaffoldBackgroundColor: const Color(0xFF0F172A),
  appBarTheme: const AppBarTheme(
    backgroundColor: Color(0xFF111827),
    elevation: 0,
    iconTheme: IconThemeData(color: Color(0xFFF3F4F6)),
    titleTextStyle: TextStyle(
      color: Color(0xFFF3F4F6),
      fontSize: 18,
      fontWeight: FontWeight.w600,
    ),
  ),
  inputDecorationTheme: InputDecorationTheme(
    filled: true,
    fillColor: const Color(0xFF1F2937),
    border: OutlineInputBorder(
      borderRadius: BorderRadius.circular(8),
      borderSide: BorderSide.none,
    ),
    focusedBorder: OutlineInputBorder(
      borderRadius: BorderRadius.circular(8),
      borderSide: const BorderSide(color: _primaryColor, width: 2),
    ),
    errorBorder: OutlineInputBorder(
      borderRadius: BorderRadius.circular(8),
      borderSide: const BorderSide(color: _errorColor),
    ),
    contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
  ),
  elevatedButtonTheme: ElevatedButtonThemeData(
    style: ElevatedButton.styleFrom(
      backgroundColor: _primaryColor,
      foregroundColor: Colors.white,
      padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
      elevation: 0,
    ),
  ),
  textButtonTheme: TextButtonThemeData(
    style: TextButton.styleFrom(
      foregroundColor: _primaryColor,
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
    ),
  ),
  cardTheme: CardTheme(
    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
    elevation: 0,
    color: const Color(0xFF111827),
  ),
);
