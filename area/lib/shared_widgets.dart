import 'package:flutter/material.dart';

class AuthContainer extends StatelessWidget {
  final Widget child;

  const AuthContainer({required this.child, super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 400,
      padding: const EdgeInsets.all(25),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.1),
            blurRadius: 10,
            offset: const Offset(0, 5),
          ),
        ],
      ),
      child: child,
    );
  }
}

class SocialLoginButtons extends StatelessWidget {
  const SocialLoginButtons({super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Expanded(
          child: ElevatedButton.icon(
            onPressed: () {
              // Handle Google login action
            },
            icon: Image.asset(
              'assets/images/google.png',
              height: 24,
              width: 24,
            ),
            label: const Text(""),
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(vertical: 15),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(10),
                side: const BorderSide(color: Colors.black),
              ),
            ),
          ),
        ),
        const SizedBox(width: 10),
        Expanded(
          child: ElevatedButton.icon(
            onPressed: () {
              // Handle Facebook login action
            },
            icon: Image.asset(
              'assets/images/facebook.png',
              height: 24,
              width: 24,
            ),
            label: const Text(""),
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(vertical: 15),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(10),
                side: const BorderSide(color: Colors.black),
              ),
            ),
          ),
        ),
      ],
    );
  }
}

class LoginButton extends StatelessWidget {
  const LoginButton({super.key});

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () {
        Navigator.pushNamed(context, '/dashboard');
      },
      style: ElevatedButton.styleFrom(
        backgroundColor: Colors.black,
        padding: const EdgeInsets.symmetric(horizontal: 50, vertical: 15),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(10),
        ),
      ),
      child: const Text(
        "Login",
        style: TextStyle(
          color: Colors.white,
          fontSize: 16,
        ),
      ),
    );
  }
}

class RegisterLink extends StatelessWidget {
  const RegisterLink({super.key});

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: () {
        Navigator.pushNamed(context, '/register');
      },
      hoverColor: Colors.transparent,
      splashColor: Colors.transparent,
      highlightColor: Colors.transparent,
      child: const Text(
        "No account? Register here!",
        style: TextStyle(
          color: Color.fromRGBO(33, 150, 243, 1),
          decoration: TextDecoration.underline,
        ),
      ),
    );
  }
}

class RegisterButton extends StatelessWidget {
  const RegisterButton({super.key});

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () {
        // Handle registration action
      },
      style: ElevatedButton.styleFrom(
        backgroundColor: Colors.black,
        padding: const EdgeInsets.symmetric(horizontal: 50, vertical: 15),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(10),
        ),
      ),
      child: const Text(
        "Register",
        style: TextStyle(
          color: Colors.white,
          fontSize: 16,
        ),
      ),
    );
  }
}

class CustomTextWidget extends StatelessWidget {
  const CustomTextWidget({super.key});

  @override
  Widget build(BuildContext context) {
  return Stack(
    children: [
      // Stroke text
      RichText(
        text: TextSpan(
          children: [
            TextSpan(
              text: "Connect your favourite apps and ",
              style: TextStyle(
                color: Colors.transparent, // Make this text transparent
                fontSize: 45,
                fontWeight: FontWeight.bold,
                fontFamily: 'ClashGrotesk',
              ),
            ),
            TextSpan(
              text: "automate workflows",
              style: TextStyle(
                fontSize: 45,
                fontWeight: FontWeight.bold,
                fontFamily: 'ClashGrotesk',
                foreground: Paint()
                  ..style = PaintingStyle.stroke
                  ..strokeWidth = 3
                  ..color = Colors.black, // Stroke color
              ),
            ),
            TextSpan(
              text: ".",
              style: TextStyle(
                color: Colors.transparent, // Make this text transparent
                fontSize: 45,
                fontWeight: FontWeight.bold,
                fontFamily: 'ClashGrotesk',
              ),
            ),
          ],
        ),
      ),
      // Fill text
      RichText(
        text: TextSpan(
          children: [
            TextSpan(
              text: "Connect your favourite apps and ",
              style: TextStyle(
                color: Color.fromARGB(255, 0, 0, 0), // Fill color
                fontSize: 45,
                fontWeight: FontWeight.bold,
                fontFamily: 'ClashGrotesk',
              ),
            ),
            TextSpan(
              text: "automate workflows",
              style: TextStyle(
                color: Color.fromARGB(255, 140, 211, 255), // Fill color
                fontSize: 45,
                fontWeight: FontWeight.bold,
                fontFamily: 'ClashGrotesk',
              ),
            ),
            TextSpan(
              text: ".",
              style: TextStyle(
                color: Color.fromARGB(255, 0, 0, 0), // Fill color
                fontSize: 45,
                fontWeight: FontWeight.bold,
                fontFamily: 'ClashGrotesk',
              ),
            ),
          ],
        ),
      ),
    ],
  );
}
}

class InfoContainer extends StatelessWidget {
  final Widget child;

  const InfoContainer({
    required this.child,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
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
              child: CustomTextWidget(
              ),
            ),
          ),
          Expanded(
            child: child, // Placeholder for the authentication form
          ),
        ],
      ),
    );
  }
}