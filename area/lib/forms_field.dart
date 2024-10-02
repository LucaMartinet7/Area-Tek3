import 'package:flutter/material.dart';
import 'validation_utils.dart'; // Import the validation utility

class CustomTextField extends StatelessWidget {
  final TextEditingController controller;
  final String labelText;
  final bool isPassword;
  final String? Function(String?)? validator;

  const CustomTextField({
    required this.controller,
    required this.labelText,
    this.isPassword = false,
    this.validator,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      controller: controller,
      obscureText: isPassword,
      decoration: InputDecoration(
        labelText: labelText,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(10),
        ),
      ),
      autovalidateMode: AutovalidateMode.onUserInteraction,
      validator: validator,
    );
  }
}

class EmailField extends StatefulWidget {
  const EmailField({super.key});

  @override
  EmailFieldState createState() => EmailFieldState();
}

class EmailFieldState extends State<EmailField> {
  final TextEditingController _controller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return CustomTextField(
      controller: _controller,
      labelText: "Email",
      validator: (value) => isValidEmail(value ?? "") ? null : "Please enter a valid email",
    );
  }
}

class PasswordField extends StatefulWidget {
  const PasswordField({super.key});

  @override
  PasswordFieldState createState() => PasswordFieldState();
}

class PasswordFieldState extends State<PasswordField> {
  final TextEditingController _controller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return CustomTextField(
      controller: _controller,
      labelText: "Password",
      isPassword: true,
      validator: (value) => value == null || value.isEmpty ? "Password can't be empty" : null,
    );
  }
}

class NameField extends StatefulWidget {
  const NameField({super.key});

  @override
  NameFieldState createState() => NameFieldState();
}

class NameFieldState extends State<NameField> {
  final TextEditingController _controller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return CustomTextField(
      controller: _controller,
      labelText: "Name",
      validator: (value) => value == null || value.isEmpty ? "Name can't be empty" : null,
    );
  }
}