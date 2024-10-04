import 'package:flutter/material.dart';
import 'platform_conditions.dart';
import 'web_login.dart';
import 'mobile_login.dart';

class LoginPage extends StatelessWidget {
  const LoginPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(""),
        automaticallyImplyLeading: false,
      ),
      body: Center(
        child: SizedBox(
          width: isMobile() ? double.infinity : 800,
          height: isMobile() ? double.infinity : 600,
          child: Stack(
            children: [
              Positioned.fill(
                child: Container(
                  padding: const EdgeInsets.all(20.0),
                  decoration: BoxDecoration(
                    color: const Color.fromARGB(255, 140, 211, 255),
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: isMobile() ? const MobileLogin() : const WebLogin(),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}