import 'package:flutter/material.dart';
import '../shared/api_service.dart';

Widget buildExitButton(BuildContext context) {
  return IconButton(
    onPressed: () async {
      await logout(context);
    },
    icon: Image.asset(
      'assets/vectors/exit.png',
      width: 32,
      height: 32,
      color: const Color.fromARGB(255, 140, 211, 255),
    ),
  );
}