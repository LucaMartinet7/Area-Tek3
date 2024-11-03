import 'package:flutter/material.dart';
import 'shared/login_form.dart';
import 'shared/register_form.dart';
import 'shared/dashboard_page.dart';
import 'web/blue_sky_login.dart';
import 'shared/about_page.dart';
import 'shared/spotify_area.dart';
import 'shared/twitch_area.dart';
import 'shared/google_area.dart';
import 'shared/youtube_area.dart';
import 'mobile/mobile_account.dart';
import 'web/route_guard.dart';
import 'package:url_strategy/url_strategy.dart';
import 'shared/bluesky_area.dart';
import 'shared/api_service.dart' show isLoggedIn;


void main() {
  setPathUrlStrategy();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: FutureBuilder<bool>(
        future: isLoggedIn(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const CircularProgressIndicator();
          } else if (snapshot.hasData && snapshot.data == true) {
            return const DashboardPage();
          } else {
            return const AboutPage();
          }
        },
      ),
      routes: {
        '/login': (context) => const LoginPage(),
        '/register': (context) => const RegisterPage(),
        '/dashboard': (context) => const DashboardPage(),
        '/spotify': (context) => const SpotifyPage(),
        '/twitch': (context) => const TwitchPage(),
        '/google': (context) => const GooglePage(),
        '/youtube': (context) => const YoutubePage(),
        '/about': (context) => const AboutPage(),
        '/account': (context) => const MobileAccount(),
        '/bluesky': (context) => const BlueSkyPage(),
        '/bluesky/login': (context) => const BlueSkyLoginPage(),
      },
    );
  }
}