import 'package:flutter/material.dart';
import 'login_form.dart';
import 'register_page.dart';

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
        //'/dashboard': (context) => DashboardPage(),
        //'/settings': (context) => SettingsPage(),
        //'/profile': (context) => ProfilePage(),
        //'/about': (context) => AboutPage(),
      },
    );
  }
}
