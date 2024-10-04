import 'package:flutter/material.dart';
import 'shared/login_form.dart';
import 'shared/register_form.dart';
import 'shared/dashboard_page.dart';
import 'settings_page.dart';
import 'about_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute: '/login',
      routes: {
        '/login': (context) => const LoginPage(),
        '/register': (context) => const RegisterPage(),
        '/dashboard': (context) => const DashboardPage(),
        '/settings': (context) => SettingsPage(),
        // '/logout': (context) => LogoutPage(),
        // '/account': (context) => AccountPage(),
        // '/spotify': (context) => SpotifyPage(),
        // '/twitch': (context) => TwitchPage(),
        // '/google': (context) => GooglePage(),
        // '/deezer': (context) => DeezerPage(),
        // '/microsoft': (context) => MicrosoftPage(),
        '/about': (context) => AboutPage(),
      },
    );
  }
}