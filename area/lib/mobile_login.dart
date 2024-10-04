import 'package:flutter/material.dart';
import 'forms_field.dart'; // Import form fields like EmailField and PasswordField
import 'shared_widgets.dart'; // Import shared widgets like SocialLoginButtons

class MobileLogin extends StatelessWidget {
  const MobileLogin({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: const AuthContainer(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              "Login Mobile",
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
    );
  }
}