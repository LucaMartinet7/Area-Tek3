import 'package:flutter/material.dart';
import '../shared/shared_widgets.dart';
import '../shared/forms_field.dart';

class WebRegister extends StatefulWidget {
  const WebRegister({super.key});

  @override
  WebRegisterState createState() => WebRegisterState();
}

class WebRegisterState extends State<WebRegister> {
  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

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
            child: AuthContainer(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text(
                    "Register",
                    style: TextStyle(
                      color: Colors.black,
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 20),
                  NameField(controller: _nameController),
                  const SizedBox(height: 20),
                  EmailField(controller: _emailController),
                  const SizedBox(height: 20),
                  PasswordField(controller: _passwordController),
                  const SizedBox(height: 20),
                  const SocialLoginButtons(),
                  const SizedBox(height: 20),
                  RegisterButton(
                    nameController: _nameController,
                    emailController: _emailController,
                    passwordController: _passwordController,
                  ),
                  const SizedBox(height: 20),
                  const LoginLink(),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}