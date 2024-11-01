import 'package:area/shared/api_service.dart';
import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';
import 'package:tuple/tuple.dart';

const double containerPadding = 25.0;
const double buttonPaddingVertical = 15.0;
const double buttonPaddingHorizontal = 50.0;

final BoxDecoration containerDecoration = BoxDecoration(
  color: Colors.white,
  borderRadius: BorderRadius.circular(20),
  boxShadow: [
    BoxShadow(
      color: Colors.black.withOpacity(0.1),
      blurRadius: 10,
      offset: const Offset(0, 5),
    ),
  ],
);

final ButtonStyle whiteButtonStyle = ElevatedButton.styleFrom(
  backgroundColor: Colors.white,
  padding: const EdgeInsets.symmetric(vertical: buttonPaddingVertical),
  shape: RoundedRectangleBorder(
    borderRadius: BorderRadius.circular(10),
    side: const BorderSide(color: Colors.black),
  ),
);

final ButtonStyle blackButtonStyle = ElevatedButton.styleFrom(
  backgroundColor: Colors.black,
  padding: const EdgeInsets.symmetric(
    horizontal: buttonPaddingHorizontal,
    vertical: buttonPaddingVertical
  ),
  shape: RoundedRectangleBorder(
    borderRadius: BorderRadius.circular(10),
  ),
);

class AuthContainer extends StatelessWidget {
  final Widget child;

  const AuthContainer({required this.child, super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 400,
      padding: const EdgeInsets.all(containerPadding),
      decoration: containerDecoration,
      child: child,
    );
  }
}

class SocialLoginButtons extends StatelessWidget {
  const SocialLoginButtons({super.key});

  Widget _buildSocialButton(String assetPath, VoidCallback onPressed) {
    return Expanded(
      child: ElevatedButton.icon(
        onPressed: onPressed,
        icon: Image.asset(assetPath, height: 24, width: 24),
        label: const Text(""),
        style: whiteButtonStyle,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        _buildSocialButton('assets/images/google.png', () {
          launchURL('http://127.0.0.1:8000/api/auth/google/login/');
        }),
        const SizedBox(width: 10),
        _buildSocialButton('assets/images/facebook.png', () {
          // Handle Facebook login action
        }),
      ],
    );
  }
}

class LoginButton extends StatelessWidget {
  final TextEditingController nameController;
  final TextEditingController passwordController;

  const LoginButton({
    super.key,
    required this.nameController,
    required this.passwordController,
  });

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () {
        login(
          context: context,
          username: nameController.text,
          password: passwordController.text,
        );
      },
      style: blackButtonStyle,
      child: const Text(
        "Login",
        style: TextStyle(color: Colors.white, fontSize: 16),
      ),
    );
  }
}

class LoginLink extends StatelessWidget {
  const LoginLink({super.key});

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: () {
        Navigator.pushNamed(context, '/login');
      },
      hoverColor: Colors.transparent,
      splashColor: Colors.transparent,
      highlightColor: Colors.transparent,
      child: const Text(
        "Already have an account? Login here!",
        style: TextStyle(
          color: Color.fromRGBO(33, 150, 243, 1),
          decoration: TextDecoration.underline,
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
  final TextEditingController nameController;
  final TextEditingController emailController;
  final TextEditingController passwordController;

  const RegisterButton({
    super.key,
    required this.nameController,
    required this.emailController,
    required this.passwordController,
  });

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () {
        register(
          context: context,
          username: nameController.text,
          password: passwordController.text,
          email: emailController.text,
        );
      },
      style: blackButtonStyle,
      child: const Text(
        "Register",
        style: TextStyle(color: Colors.white, fontSize: 16),
      ),
    );
  }
}

class CustomTextWidget extends StatelessWidget {
  const CustomTextWidget({super.key});

  TextStyle _buildTextStyle(Color color) {
    return TextStyle(
      color: color,
      fontSize: 45,
      fontWeight: FontWeight.bold,
      fontFamily: 'ClashGrotesk',
    );
  }

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        // Stroke text
        RichText(
          text: TextSpan(
            children: [
              TextSpan(text: "Connect your favourite apps and ", style: _buildTextStyle(Colors.transparent)),
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
              TextSpan(text: ".", style: _buildTextStyle(Colors.transparent)),
            ],
          ),
        ),
        // Fill text
        RichText(
          text: TextSpan(
            children: [
              TextSpan(text: "Connect your favourite apps and ", style: _buildTextStyle(Colors.black)),
              TextSpan(text: "automate workflows", style: _buildTextStyle(Color.fromARGB(255, 140, 211, 255))),
              TextSpan(text: ".", style: _buildTextStyle(Colors.black)),
            ],
          ),
        ),
      ],
    );
  }
}

class InfoContainer extends StatelessWidget {
  final Widget child;

  const InfoContainer({required this.child, super.key});

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
              child: const CustomTextWidget(),
            ),
          ),
          Expanded(
            child: child,
          ),
        ],
      ),
    );
  }
}

class ActionReactionRectangle extends StatefulWidget {
  final Tuple2<String, String> actionReaction;
  final Color color;

  const ActionReactionRectangle({
    required this.actionReaction,
    required this.color,
    super.key,
  });

  @override
  ActionReactionRectangleState createState() => ActionReactionRectangleState();
}

class ActionReactionRectangleState extends State<ActionReactionRectangle> {
  bool _hovering = false;
  bool _isActive = false;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        if (kDebugMode) {
          print('Action: ${widget.actionReaction.item1}');
          print('Reaction: ${widget.actionReaction.item2}');
        }
      },
      child: MouseRegion(
        onEnter: (_) => setState(() => _hovering = true),
        onExit: (_) => setState(() => _hovering = false),
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 200),
          decoration: BoxDecoration(
            color: _hovering ? widget.color.withOpacity(0.7) : widget.color,
            borderRadius: BorderRadius.circular(10),
          ),
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 8.0),
                  child: Text(
                    widget.actionReaction.item1,
                    textAlign: TextAlign.center,
                    overflow: TextOverflow.ellipsis,
                    maxLines: 2,
                    style: const TextStyle(fontSize: 20, color: Colors.white),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 8.0),
                  child: Text(
                    widget.actionReaction.item2,
                    textAlign: TextAlign.center,
                    overflow: TextOverflow.ellipsis,
                    maxLines: 2,
                    style: const TextStyle(fontSize: 16, color: Colors.white70),
                  ),
                ),
                Switch(
                  value: _isActive,
                  onChanged: (value) => setState(() => _isActive = value),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

