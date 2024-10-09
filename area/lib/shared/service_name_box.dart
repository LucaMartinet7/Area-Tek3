import 'package:flutter/material.dart';

class ServiceNameBox extends StatelessWidget {
  final String logoPath;
  final String serviceName;
  final VoidCallback onConnect;
  final Color borderColor;

  const ServiceNameBox({
    required this.logoPath,
    required this.serviceName,
    required this.onConnect,
    this.borderColor = Colors.grey, // Default border color
    super.key,
  });

  BoxDecoration _boxDecoration() {
    return BoxDecoration(
      border: Border.all(
        color: borderColor,
        width: 3.0,
      ),
      borderRadius: BorderRadius.circular(8.0),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(8.0),
      height: 150,
      decoration: _boxDecoration(),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Image.asset(
                logoPath,
                height: 50,
              ),
              const SizedBox(width: 10),
              GestureDetector(
                onTap: onConnect,
                child: Text(
                  serviceName,
                  style: const TextStyle(
                    fontSize: 32,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}