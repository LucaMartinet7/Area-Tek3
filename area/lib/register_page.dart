import 'package:flutter/material.dart';
import 'shared_widgets.dart';
import 'forms_field.dart';

class RegisterPage extends StatelessWidget {
  const RegisterPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Register"),
        automaticallyImplyLeading: false,
      ),
      body: const AuthContainer(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              "Register",
              style: TextStyle(
                color: Colors.black,
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),
            SizedBox(height: 20),
            NameField(),
            SizedBox(height: 20),
            EmailField(),
            SizedBox(height: 20),
            PasswordField(),
            SizedBox(height: 20),
            SocialLoginButtons(),
            SizedBox(height: 20),
            RegisterButton(),
          ],
        ),
      ),
    );
  }
}
