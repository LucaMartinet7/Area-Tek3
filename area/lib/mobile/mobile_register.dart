import 'package:flutter/material.dart';
import '../shared/shared_widgets.dart';   // Import shared widgets like SocialLoginButtons
import '../shared/forms_field.dart';      // Import form fields like NameField, EmailField, PasswordField

class MobileRegister extends StatelessWidget {
  const MobileRegister({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: SizedBox(
        width: 350,
        height: 500,
        child: Container(
          padding: const EdgeInsets.all(20.0),
          decoration: BoxDecoration(
            color: const Color.fromARGB(255, 140, 211, 255),
            borderRadius: BorderRadius.circular(20),
          ),
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
    );
  }
}

