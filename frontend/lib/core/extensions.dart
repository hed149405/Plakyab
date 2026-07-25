// Extension methods

extension StringExtension on String {
  bool isValidEmail() {
    final emailRegex = RegExp(
      r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    );
    return emailRegex.hasMatch(this);
  }

  bool isValidVIN() {
    if (length != 17) return false;
    final vinRegex = RegExp(r'^[A-HJ-NPR-Z0-9]{17}$');
    return vinRegex.hasMatch(toUpperCase());
  }

  String capitalize() {
    if (isEmpty) return this;
    return '${this[0].toUpperCase()}${substring(1)}';
  }
}

extension DateTimeExtension on DateTime {
  String toReadableString() {
    return '$day/$month/$year';
  }
}
