import 'package:flutter/material.dart';
import '../shared/forms_field.dart';
import '../shared/shared_widgets.dart';

class MobileLogin extends StatefulWidget {
  const MobileLogin({super.key});

  @override
  MobileLoginState createState() => MobileLoginState();
}

class MobileLoginState extends State<MobileLogin> {
  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

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
                color: const Color.fromARGB(255, 140, 211, 255),
                width: 15.0,
              ),
              borderRadius: BorderRadius.circular(30),
            ),
            child: ClipRRect(
              borderRadius: BorderRadius.circular(25),
              child: Container(
                padding: const EdgeInsets.all(20.0),
                color: Colors.white,
                constraints: const BoxConstraints(
                  maxWidth: 400,
                ),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Text(
                      "Login",
                      style: TextStyle(
                        color: Colors.black,
                        fontSize: 24,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 20),
                    NameField(controller: _nameController),
                    const SizedBox(height: 20),
                    PasswordField(controller: _passwordController),
                    const SizedBox(height: 20),
                    const SocialLoginButtons(),
                    const SizedBox(height: 20),
                     LoginButton(
                       nameController: _nameController,
                       passwordController: _passwordController,
                     ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}