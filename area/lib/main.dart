import 'package:flutter/material.dart';
import 'shared/login_form.dart';
import 'shared/register_form.dart';
import 'shared/dashboard_page.dart';
import 'settings_page.dart';
import 'about_page.dart';
import 'shared/spotify_area.dart';
import 'shared/twitch_area.dart';
import 'shared/google_area.dart';
import 'shared/youtube_area.dart';
import 'shared/microsoft_area.dart';
import 'mobile/mobile_account.dart';
import 'web/route_guard.dart';
import 'package:url_strategy/url_strategy.dart';

void main() {
  setPathUrlStrategy();
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
