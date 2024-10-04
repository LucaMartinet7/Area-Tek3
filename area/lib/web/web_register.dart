import 'package:flutter/material.dart';
import '../shared/shared_widgets.dart';   // Import shared widgets like SocialLoginButtons
import '../shared/forms_field.dart';      // Import form fields like NameField, EmailField, PasswordField

class WebRegister extends StatelessWidget {
  const WebRegister({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: false,
      ),
      body: Center(
        child: SizedBox(
          width: 800,
          height: 600,
          child: InfoContainer(
            child: const AuthContainer(
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
            ),
        ),
      ),
    );
  }
}