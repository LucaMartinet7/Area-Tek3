import 'package:flutter/material.dart';
import '../shared/forms_field.dart'; // Import form fields like NameField, EmailField, PasswordField
import '../shared/shared_widgets.dart'; // Import shared widgets like SocialLoginButtons
import 'mobile_nav_bar.dart'; // Import the MobileNavBar

class MobileRegister extends StatelessWidget {
  const MobileRegister({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: false,
      ),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(20.0),
          child: Container(
            decoration: BoxDecoration(
              border: Border.all(
                color: const Color.fromARGB(255, 140, 211, 255), // Blue border color
                width: 15.0, // Border width
              ),
              borderRadius: BorderRadius.circular(30), // More rounded border
            ),
            child: ClipRRect(
              borderRadius: BorderRadius.circular(25), // Slightly smaller radius for inner clipping
              child: Container(
                padding: const EdgeInsets.all(20.0),
                color: Colors.white, // Set the background color to white
                constraints: const BoxConstraints(
                  maxWidth: 400,
                  maxHeight: 600,
                ),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: const [
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
                    SizedBox(height: 20),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
      bottomNavigationBar: const MobileNavBar(),
    );
  }
}