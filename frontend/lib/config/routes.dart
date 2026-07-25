import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

final goRouterProvider = Provider((ref) {
  return GoRouter(
    routes: <RouteBase>[
      GoRoute(
        path: '/',
        name: 'home',
        builder: (BuildContext context, GoRouterState state) {
          return const SizedBox(); // Placeholder - will implement SplashScreen
        },
      ),
      GoRoute(
        path: '/login',
        name: 'login',
        builder: (BuildContext context, GoRouterState state) {
          return const SizedBox(); // Placeholder - will implement LoginScreen
        },
      ),
      GoRoute(
        path: '/register',
        name: 'register',
        builder: (BuildContext context, GoRouterState state) {
          return const SizedBox(); // Placeholder - will implement RegisterScreen
        },
      ),
      GoRoute(
        path: '/vehicles',
        name: 'vehicles',
        builder: (BuildContext context, GoRouterState state) {
          return const SizedBox(); // Placeholder - will implement VehicleSearchScreen
        },
      ),
      GoRoute(
        path: '/vehicles/:id',
        name: 'vehicle-detail',
        builder: (BuildContext context, GoRouterState state) {
          final id = state.pathParameters['id'];
          return const SizedBox(); // Placeholder - will implement VehicleDetailsScreen
        },
      ),
      GoRoute(
        path: '/vin-decoder',
        name: 'vin-decoder',
        builder: (BuildContext context, GoRouterState state) {
          return const SizedBox(); // Placeholder - will implement VINDecoderScreen
        },
      ),
      GoRoute(
        path: '/admin',
        name: 'admin',
        builder: (BuildContext context, GoRouterState state) {
          return const SizedBox(); // Placeholder - will implement AdminDashboardScreen
        },
      ),
      GoRoute(
        path: '/profile',
        name: 'profile',
        builder: (BuildContext context, GoRouterState state) {
          return const SizedBox(); // Placeholder - will implement ProfileScreen
        },
      ),
      GoRoute(
        path: '/settings',
        name: 'settings',
        builder: (BuildContext context, GoRouterState state) {
          return const SizedBox(); // Placeholder - will implement SettingsScreen
        },
      ),
    ],
  );
});
