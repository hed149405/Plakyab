class Validators {
  static String? validateEmail(String? value) {
    if (value == null || value.isEmpty) {
      return 'Email is required';
    }
    const pattern =
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$';
    final regExp = RegExp(pattern);
    if (!regExp.hasMatch(value)) {
      return 'Enter a valid email';
    }
    return null;
  }

  static String? validatePassword(String? value) {
    if (value == null || value.isEmpty) {
      return 'Password is required';
    }
    if (value.length < 8) {
      return 'Password must be at least 8 characters';
    }
    if (!value.contains(RegExp(r'[A-Z]'))) {
      return 'Password must contain uppercase letter';
    }
    if (!value.contains(RegExp(r'[a-z]'))) {
      return 'Password must contain lowercase letter';
    }
    if (!value.contains(RegExp(r'[0-9]'))) {
      return 'Password must contain digit';
    }
    return null;
  }

  static String? validateVIN(String? value) {
    if (value == null || value.isEmpty) {
      return 'VIN is required';
    }
    if (value.length != 17) {
      return 'VIN must be 17 characters';
    }
    final pattern = r'^[A-HJ-NPR-Z0-9]{17}$';
    final regExp = RegExp(pattern);
    if (!regExp.hasMatch(value.toUpperCase())) {
      return 'Invalid VIN format';
    }
    return null;
  }

  static String? validatePlate(String? value) {
    if (value == null || value.isEmpty) {
      return 'Plate number is required';
    }
    if (value.length < 3) {
      return 'Invalid plate number';
    }
    return null;
  }

  static String? validateName(String? value) {
    if (value == null || value.isEmpty) {
      return 'Name is required';
    }
    if (value.length < 2) {
      return 'Name must be at least 2 characters';
    }
    return null;
  }
}
