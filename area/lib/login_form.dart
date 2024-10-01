import 'package:flutter/material.dart';
import 'shared_widgets.dart'; // Import shared widgets like SocialLoginButtons
import 'forms_field.dart'; // Import form fields like EmailField and PasswordField

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
          width: 800,
          height: 600,
          child: Stack(
            children: [
              Positioned.fill(
                child: Container(
                  padding: const EdgeInsets.all(20.0),
                  decoration: BoxDecoration(
                    color: const Color.fromARGB(255, 140, 211, 255),
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: Row(
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
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}