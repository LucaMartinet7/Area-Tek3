import 'package:flutter/material.dart';
import 'shared_widgets.dart'; // Import shared widgets like SocialLoginButtons
import 'forms_field.dart'; // Import form fields like EmailField and PasswordField

class LoginPage extends StatelessWidget {
  const LoginPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Login"),
        automaticallyImplyLeading: false,
      ),
      body: const AuthContainer(
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
    );
  }
}
