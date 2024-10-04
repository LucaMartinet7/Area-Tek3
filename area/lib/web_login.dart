import 'package:flutter/material.dart';
import 'forms_field.dart'; // Import form fields like EmailField and PasswordField
import 'shared_widgets.dart'; // Import shared widgets like SocialLoginButtons

class WebLogin extends StatelessWidget {
  const WebLogin({super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Expanded(
          child: Container(
            padding: const EdgeInsets.all(20.0),
            child: const Text(
              "Connect your favourite apps and automate workflows.",
              style: TextStyle(
                color: Colors.black,
                fontSize: 45,
                fontWeight: FontWeight.bold,
              ),
              textAlign: TextAlign.left,
            ),
          ),
        ),
        const Expanded(
          child: AuthContainer(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  "Login",
                  style: TextStyle(
                    color: Colors.black,
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                SizedBox(height: 20),
                EmailField(),
                SizedBox(height: 20),
                PasswordField(),
                SizedBox(height: 20),
                SocialLoginButtons(),
                SizedBox(height: 20),
                LoginButton(),
                SizedBox(height: 20),
                RegisterLink(),
              ],
            ),
          ),
        ),
      ],
    );
  }
}