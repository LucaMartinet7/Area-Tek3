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
        // '/logout': (context) => const LogoutPage(),
        '/spotify': (context) => const SpotifyPage(),
        '/twitch': (context) => const TwitchPage(),
        '/google': (context) => const GooglePage(),
        '/youtube': (context) => const YoutubePage(),
        '/microsoft': (context) => const MicrosoftPage(),
        '/about': (context) => const AboutPage(),
      },
    );
  }
}
