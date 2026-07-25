class Formatters {
  static String formatVIN(String vin) {
    return vin.toUpperCase();
  }

  static String formatPlate(String plate) {
    return plate.toUpperCase();
  }

  static String formatPhone(String phone) {
    // Simple formatting - customize as needed
    return phone.replaceAll(RegExp(r'\D'), '');
  }

  static String formatCurrency(double amount) {
    return '\$${amount.toStringAsFixed(2)}';
  }

  static String formatDate(DateTime date) {
    return '${date.day}/${date.month}/${date.year}';
  }

  static String formatDateTime(DateTime dateTime) {
    final date = '${dateTime.day}/${dateTime.month}/${dateTime.year}';
    final time =
        '${dateTime.hour.toString().padLeft(2, '0')}:${dateTime.minute.toString().padLeft(2, '0')}';
    return '$date $time';
  }
}
